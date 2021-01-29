#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio
from azure.eventhub.aio import EventHubProducerClient

class Sender:
    def __init__(self):
        self._vName = self.__class__.__name__
        self._json_data = ""


    async def accummulate (self):
        producer = EventHubProducerClient.from_connection_string(conn_str="Endpoint=sb://eventhubss1.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=q1gy+i097l8UKkTJ0Png8qjO2jOXGyRCgxz59p0GSwY=",\
                                                                eventhub_name="firsttopic")                                                    
        async with producer:
            event_data_batch = await producer.create_batch()
            event_data_batch.add(EventData(self._json_data))
            await producer.send_batch(event_data_batch)

    def send (self,json_data):
        self._json_data = str(json_data)
        loop = asyncio.new_event_loop()
        loop.run_until_complete(accummulate())
