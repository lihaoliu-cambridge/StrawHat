# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging.config

import tornado.gen
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.httpclient import AsyncHTTPClient
import json

from utils.config_loader import load_log_config, load_mysql_config, save_config_to_redis
from common.errors import *
from common.constants import RET_OK, RET_ERROR
from engine.data.mysql.schema import *
from engine.data.mysql.mysql_connmanager import MysqlConnManager

logging.config.dictConfig(load_log_config())
g_logger = logging.getLogger('api_handler_logger')


class AlterMysqlConfApiHandler(tornado.web.RequestHandler):

    def data_received(self, chunk):
        pass

    AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")

    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        api_return = None
        try:
            # get new mysql_db_name
            param_mysql_db_name = self.get_argument('mysql_db_name', strip=False)

            # check if this db is exist
            check_sign_for_db, return_msg, mysql_conf = self.check_for_new_mysql_db(param_mysql_db_name)

            if check_sign_for_db:
                self.alter_mysql_conf_in_redis(mysql_conf, param_mysql_db_name)
                api_return = {
                    'code': RET_OK,
                }
            else:
                api_return = {
                    'code': RET_ERROR,
                }

        except ApiArgumentMissingError as api_param_missing_error:
            g_logger.error("api_missing_error, message:{0}".format(api_param_missing_error))
            api_return = {
                'code': RET_ERROR,
                'error_code': ERR_CODE_MISSING_PARAMETER,
                'error_msg': api_param_missing_error.message
            }

        except ApiArgumentTypeError as api_type_error:
            g_logger.error("api_type_error, message:{0}".format(api_type_error))
            api_return = {
                'code': RET_ERROR,
                'error_code': ERR_CODE_WRONG_PARAMETER_TYPE,
                'error_msg': api_type_error.message
            }

        except ApiArgumentCheckSignError as api_check_sign_error:
            g_logger.error("api_check_sign_error, message:{0}".format(api_check_sign_error))
            api_return = {
                'code': RET_ERROR,
                'error_code': ERR_CODE_PARAMETER_SIGN_ERROR,
                'error_msg': api_check_sign_error.message
            }

        except Exception as other_error:
            g_logger.error("unknown error occur, message:{0}".format(other_error))
            api_return = {
                'code': RET_ERROR,
                'error_code': ERR_CODE_UNKNOWN,
                'error_msg': other_error.message
            }

        finally:
            # send the result back
            self.write(json.dumps(api_return))
            self.finish()

    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self, *args, **kwargs):
        self.get()

    @staticmethod
    def check_for_new_mysql_db(db_name):
        mysql_config = load_mysql_config()

        # check if the database is the same as the last one
        if mysql_config['db_server']['db'] == db_name:
            alter_info = 'New database is the same as the former one.'
            return False, alter_info, mysql_config

        # check if the new database exist.
        mysql_conn = MysqlConnManager.create_connection(
            host=mysql_config['db_server']['host'],
            port=mysql_config['db_server']['port'],
            db=db_name,
            user=mysql_config['db_server']['user'],
            passwd=mysql_config['db_server']['password'],
            use_unicode=mysql_config['common']['use_unicode'],
            charset=mysql_config['common']['charset'],
            connect_timeout=mysql_config['common']['connect_timeout'],
        )

        # return error kinds
        if not mysql_conn:
            alter_info = 'New database does not exist.'
            return False, alter_info, mysql_config
        else:
            mysql_conn.disconnect()
            alter_info = 'New database exist.'
            return True, alter_info, mysql_config

    @staticmethod
    def alter_mysql_conf_in_redis(mysql_conf, new_db_name):
        mysql_conf['db_server']['db'] = new_db_name
        save_config_to_redis('mysql', mysql_conf)
