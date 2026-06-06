from API_Edge_Layer.server import app
from Event_Queue.queue import NexusEventQueue
from Execution_Adapters.adapters import StripeAdapter

queue = NexusEventQueue()

async def process(event):
    await queue.push(event)
    return {"status": "queued"}
