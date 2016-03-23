#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# config logging
import logging
logging.basicConfig(
    level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S',
    format='[%(asctime)s] %(levelname)s - %(message)s'
)

import os

from flask import Flask, send_from_directory

import handler

def _main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--bind', default='127.0.0.1')
    parser.add_argument('-l', '--listen', default='10998')
    opts, args = parser.parse_known_args()
    # 注册监听器
    app = Flask('PATCHOULI')
    handler.register_handlers(app)

    # 图标处理
    @app.route('/favicon.ico')
    def get_favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.png')

    # 启动服务器
    app.run(host=opts.bind, port=int(opts.listen))

if __name__ == '__main__':
    _main()