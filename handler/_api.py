# -*- coding: utf-8 -*-

from redis import Redis
import flask

import config

import _decorator as decorator

__author__ = 'deadblue'

@decorator.output_json
def api_keys():
    # 获取服务器配置
    server = flask.request.values.get('server')
    server_config = config.hosts.get(server)
    # 连接redis，查询keys
    rc = Redis(host=server_config['host'])
    ks = rc.keys(server_config['pattren'])
    keys = []
    for k in ks:
        keys.append(k)
    return keys

