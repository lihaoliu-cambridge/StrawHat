#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from utils.config_helper import ConfigHelper
from utils.redis_cache import RedisCacheService
import logging.config
import logging
import codecs
import json
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

__author__ = 'LH Liu'

logging.config.dictConfig(ConfigHelper.load_config('log'))
logger = logging.getLogger()


def process(keyword):
    # 1.load classification order
    classification_category = ConfigHelper.load_config('classification_category.yaml')

    # 2. load redis conf
    redis_config = ConfigHelper.load_config('redis')
    cache_service = RedisCacheService(redis_config['server'], redis_config['ttl'])

    # 3.determine if this word belong to this category
    default_category = 5
    keyword_category = default_category
    for category_name, category_detail in classification_category.items():
        sign_for_this_category, category_number = check_the_category_of_keyword(keyword, category_detail, cache_service)
        if sign_for_this_category:
            keyword_category = category_number
            break
    # return cate
    return_value = json.dumps({keyword: keyword_category})
    return keyword_category


def check_the_category_of_keyword(keyword, category_detail, cache_service):
    estimate_method = category_detail.get('estimate_method')
    params = category_detail.get('params')
    if estimate_method == 'redis':
        if check_the_category_of_keyword_from_redis(keyword, params.get('key_type'), cache_service):
            return True, params.get('category_value')
        else:
            return False, None
    elif estimate_method == 'regular_expression':
        if check_the_category_of_keyword_by_re_pattern(keyword, params.get('re_pattern'), params.get('threshold')):
            return True, params.get('category_value')
        else:
            return False, None
    else:
        raise ValueError('The estimate_method is not redis or regular_expression')


def check_the_category_of_keyword_from_redis(keyword, key_type, cache_service):
    return cache_service.sread(key_type, keyword)


def check_the_category_of_keyword_by_re_pattern(keyword, re_pattern, threshold):
    if len(keyword) > threshold:
        return True
    else:
        re_for_id = re.compile(eval(re_pattern))
        match_sign = re_for_id.match(keyword)
        if match_sign:
            return True


b = []
with codecs.open('E:\\PythonProject\\Work\\work_5\\query_classification\\data\\test_data.tsv', mode='r',
                 encoding='utf-8') as f:
    qw = {1: '地域', 2: '类别', 3: '名称', 4: 'Id', 5: '其他'}
    for xxx in f:
        a = xxx.strip()
        if a is not '':
            print '{"' + a + '": ' + str(process(a)) + '}'
