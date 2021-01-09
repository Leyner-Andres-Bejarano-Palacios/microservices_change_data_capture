import json
import DataDestination.*
# import asyncio
# from azure.eventhub import EventData
from flask import Flask, jsonify, request
# from azure.eventhub.aio import EventHubProducerClient
from flask_restful import Resource, Api, reqparse, abort





application = Flask(__name__)
api = Api(application)


class EventhubsApi(Resource):
    def get(self):
        return "working"


    def post(self):
        
        json_data = request.data
        dataDestinationEventHubs = DataDestinationEventHubs(json_data)
        return "nada"#resultado.tolist()

api.add_resource(EventhubsApi,'/EventhubsApi')

if __name__=='__main__':
    application.run(debug=True,host='0.0.0.0',port=5000)

