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
from cache import KEY_TYPE_SYS_CONFIG
from mysql_connmanager import MysqlConnManager
from common.errors import MysqlDataError

logging.config.dictConfig(load_log_config())
g_logger = logging.getLogger('handler_logger')


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
            check_sign_for_db, api_return, mysql_conf = self.check_for_new_mysql_db(param_mysql_db_name)

            if check_sign_for_db:
                self.alter_mysql_conf_in_redis(mysql_conf, param_mysql_db_name)
                api_return += ' Update successfully.'
            else:
                api_return += ' Updata failed.'

        except IOError, e:
            pass

        finally:
            # send the result back
            self.write(api_return)
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
        )
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
        save_config_to_redis(KEY_TYPE_SYS_CONFIG, 'mysql', mysql_conf)
