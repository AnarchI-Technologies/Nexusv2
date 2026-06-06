import redis
import json

class DistributedEventBus:
    def __init__(self, host='localhost', port=6379):
        self.client = redis.Redis(host=host, port=port, decode_responses=True)
        self.channel = "nexus_event_stream"

    def publish(self, event: dict):
        self.client.lpush(self.channel, json.dumps(event))

    def consume(self):
        return self.client.brpop(self.channel, timeout=5)
