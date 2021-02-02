#!/usr/bin/env python
# -*- coding: utf-8 -*-


from EventSenderBL import EventSenderBL
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse, abort

class EventSenderApi(Resource):
    def __init__(self, **kwargs):
        self.__eventSenderBL = kwargs['eventSenderBL']

    def get(self):
        return "working"

    def post(self):
        json_data = request.data
        self.__eventSenderBL.send(json_data)
        return "nada"