# -*- coding: utf-8 -*-

import _api as api
import _view as view

__author__ = 'deadblue'

def register_handlers(app):
    app.add_url_rule('/', 'view_index', view.view_index)
    app.add_url_rule('/value', 'view_value', view.view_value)
    app.add_url_rule('/api/keys', 'api_keys', api.api_keys)
