# -*- coding: utf-8 -*-

import json

from flask import make_response, render_template

__author__ = 'deadblue'

def output_json(func):
    def invoker(*args, **kwargs):
        result = func(*args, **kwargs)
        resp = make_response( json.dumps(result) )
        resp.headers['Content-Type'] = 'application/json'
        return resp
    return invoker

def output_html(tpl_name):
    def invoker_creator(func):
        def invoker(*args, **kwargs):
            data = func(*args, **kwargs)
            resp = make_response( render_template(tpl_name, **data) )
            resp.headers['Content-Type'] = 'text/html; charset=utf-8'
            return resp
        return invoker
    return invoker_creator