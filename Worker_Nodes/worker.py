import json

class WorkerNode:
    def __init__(self, node_id, role):
        self.node_id = node_id
        self.role = role

    def process(self, event):
        event = json.loads(event)

        if self.role == "router":
            event["route"] = "ai_assigned"

        elif self.role == "rules":
            if event.get("event_type") == "PAYMENT":
                if event["payload"].get("amount", 0) > 5000:
                    event["state"] = "BLOCKED"

        elif self.role == "plugins":
            event["plugin_executed"] = True

        event["processed_by"] = self.node_id
        return event
