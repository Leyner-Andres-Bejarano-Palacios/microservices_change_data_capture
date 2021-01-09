import asyncio
from azure.eventhub.aio import EventHubConsumerClient
from azure.eventhub.extensions.checkpointstoreblobaio import BlobCheckpointStore


async def on_event(partition_context, event):
    # Print the event data.
    print("Received the event: \"{}\" from the partition with ID: \"{}\"".format(event.body_as_str(encoding='UTF-8'), partition_context.partition_id))

    # Update the checkpoint so that the program doesn't read the events
    # that it has already read when you run it next time.
    await partition_context.update_checkpoint(event)

async def main():
    # Create an Azure blob checkpoint store to store the checkpoints.
    checkpoint_store = BlobCheckpointStore.from_connection_string("DefaultEndpointsProtocol=https;AccountName=sqlva4nai6xe4wyims;AccountKey=0VJjrdlBoYad8bKWikPW7SHkA/oOVT8fNKK77FsqEE3u5C8LmavwQbwc2EFciv1ckwxtVLwdpyqc6O1u5csdgw==;EndpointSuffix=core.windows.net",\
                                                                  "streamingstorage")

    # Create a consumer client for the event hub.
    client = EventHubConsumerClient.from_connection_string("Endpoint=sb://eventhubss1.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=s+gBt9n8Tdkq+2wWBVL4NqDZYBUFaza9/TCdX8NnSC4=",\
                                                           consumer_group="$Default",\
                                                           eventhub_name="firsttopic",\
                                                           checkpoint_store=checkpoint_store)
    async with client:
        # Call the receive method. Read from the beginning of the partition (starting_position: "-1")
        await client.receive(on_event=on_event,  starting_position="-1")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # Run the main method.
    loop.run_until_complete(main())   