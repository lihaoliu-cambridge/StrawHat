#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

__author__ = 'LH Liu'


def main():
    parser = argparse.ArgumentParser(prog='wechat_oa_account_name_classifier',
                                     description='Name classifier for Wechat OA accounts.')
    # parameters for deployment
    group_deployment = parser.add_argument_group('group_deployment', 'Parameters only used for deployment')
    group_deployment.add_argument('--log_folder_path', default='logs', help='the log output position.')
    group_deployment.add_argument('--log_level', default='DEBUG',
                                  choices=['DEBUG', 'INFO', 'ERROR', 'WARNING', 'CRITICAL'], help='the log level.')
    group_deployment.add_argument('--processor_count', type=int, default=4,
                                  help='the count of processors will be used when processing')
    # parameters for calling this plugin
    group_call = parser.add_argument_group('group_call', 'Parameters only used for calling this plugin.')
    group_call.add_argument('infile_path', help='the input file path to be classified by the name classifier.')
    group_call.add_argument('input_schema_path', help='the schema path of input file.')
    group_call.add_argument('outfile_path', help='the output file path of the name classifier result.')
    group_call.add_argument('output_schema_path', help='the schema path of output file.')

    print 'Yse'


if __name__ == '__main__':
    main()
