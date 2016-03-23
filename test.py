# -*- coding: utf-8 -*-

import redis

__author__ = 'deadblue'

def _test():
    rc = redis.Redis('10.8.10.217')
    print rc.type('common:message:kchina_message_6:136760')
    print rc.ttl('common:message:kchina_message_6:136760')

if __name__ == '__main__':
    _test()