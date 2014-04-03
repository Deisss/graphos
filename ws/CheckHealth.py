#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web

class CheckHealthHandler(tornado.web.RequestHandler):
    ''' Manage checkhealth haproxy check '''
    def get(self):
        self.set_status(200)
    def post(self):
        self.set_status(200)
    def put(self):
        self.set_status(200)
    def delete(self):
        self.set_status(200)
    def head(self):
        self.set_status(200)
    def options(self):
        self.set_status(200)
