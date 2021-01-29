#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from sender import Sender
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse, abort


sender = Sender()
application = Flask(__name__)
api = Api(application)

class HelloWorld(Resource):
    def get(self):
        return "working"


    def post(self):
        json_data = request.data
        sender.send(json_data)
        return "nada"

api.add_resource(HelloWorld,'/')

if __name__=='__main__':
    application.run(debug=True,host='0.0.0.0',port=5000)

