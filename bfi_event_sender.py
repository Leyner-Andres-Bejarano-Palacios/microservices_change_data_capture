import asyncio
from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient

server = 'theserversql.database.windows.net'
database = 'thedatabase'
username = 'A123456ACa'
password = '123456AC#a'   
driver= '{ODBC Driver 17 for SQL Server}'




async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
    # the event hub name.
    producer = EventHubProducerClient.from_connection_string(conn_str="Endpoint=sb://eventhubss1.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=s+gBt9n8Tdkq+2wWBVL4NqDZYBUFaza9/TCdX8NnSC4=",\
                                                             eventhub_name="firsttopic")
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        event_data_batch.add(EventData('First event '))
        event_data_batch.add(EventData('Second event'))
        event_data_batch.add(EventData('Third event'))

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
