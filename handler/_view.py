# -*- coding: utf-8 -*-

import logging

from redis import Redis
import flask

import config

import _decorator as decorator

__author__ = 'deadblue'

def view_root():
    return 'Hello, world!'

@decorator.output_html('index.html')
def view_index():
    server = flask.request.values.get('server')
    return {'server':server}

@decorator.output_html('value.html')
def view_value():
    server = flask.request.values.get('server')
    key = flask.request.values.get('key')
    # 连接redis
    server_config = config.hosts.get(server)
    rc = Redis(host=server_config['host'])
    # 查询信息
    value_type = rc.type(key)
    value_ttl = rc.ttl(key)
    if value_type == 'string':
        value = rc.get(key)
    elif value_type == 'hash':
        value = rc.hgetall(key)
    elif value_type == 'list':
        value = rc.lrange(key, 0, -1)
    elif value_type == 'set':
        value = rc.smembers(key)
    elif value_type == 'zset':
        value = rc.zrange(key, 0, 1, withscores=True)
    else:
        value = ''
    return {
        'key': key,
        'type': value_type,
        'ttl': value_ttl,
        'value': value
    }