#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utilities import argparser
from EventSenderApi import EventSenderApi
from EventSenderBL import EventSenderBL
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse, abort




if __name__=='__main__':
    application = Flask(__name__)
    api = Api(application)
    vArgs = argparser.ArgParser.fn_get_args()
    eventSenderBL = EventSenderBL(vArgs)
    api.add_resource(EventSenderApi,'/',resource_class_kwargs={ 'eventSenderBL.': eventSenderBL })
    application.run(debug=True,host='0.0.0.0',port=5000)

