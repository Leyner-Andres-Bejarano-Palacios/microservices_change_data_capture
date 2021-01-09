import asyncio
from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient

class DataDestinationEventHubs(DataDestination): 

    def __init__(self, data):
        self.__data = data

    async def run(json_data):
        producer = EventHubProducerClient.from_connection_string(conn_str=\
                                                                "Endpoint=sb://eventhubss1.servicebus.windows.net/;"\
                                                                "SharedAccessKeyName=RootManageSharedAccessKey;"\
                                                                "SharedAccessKey=s+gBt9n8Tdkq+2wWBVL4NqDZYBUFaza9/TCdX8NnSC4=",\
                                                                eventhub_name="firsttopic")                                                    
        async with producer:
            event_data_batch = await producer.create_batch()
            event_data_batch.add(EventData(json_data))
            await producer.send_batch(event_data_batch)

    """send...."""
    def send(self, records):
        loop = asyncio.new_event_loop()
        loop.run_until_complete(run(str(self.__data)))
        return None