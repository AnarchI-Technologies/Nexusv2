class SchemaRegistry:
    def __init__(self):
        self.schemas = {
            "v1": {
                "fields": ["event_id", "tenant_id", "event_type", "payload"]
            }
        }

    def resolve(self, version: str):
        return self.schemas.get(version, None)
