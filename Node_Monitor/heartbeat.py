import time

class Heartbeat:
    def __init__(self, node_id):
        self.node_id = node_id

    def ping(self):
        return {
            "node": self.node_id,
            "status": "alive",
            "timestamp": time.time()
        }
