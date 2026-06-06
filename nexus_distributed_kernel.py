from Distributed_Bus.bus import DistributedEventBus
from Worker_Nodes.worker import WorkerNode
import json

class NexusDistributedKernel:
    def __init__(self):
        self.bus = DistributedEventBus()

        self.router_node = WorkerNode("node-router-1", "router")
        self.rule_node = WorkerNode("node-rules-1", "rules")
        self.plugin_node = WorkerNode("node-plugin-1", "plugins")

    def ingest(self, event):
        self.bus.publish(event)

    def cycle(self):
        msg = self.bus.consume()
        if not msg:
            return None

        _, raw = msg
        event = json.loads(raw)

        event = self.router_node.process(json.dumps(event))
        event = self.rule_node.process(json.dumps(event))
        event = self.plugin_node.process(json.dumps(event))

        return event
