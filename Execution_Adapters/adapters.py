class PluginAdapter:
    async def execute(self, event: dict):
        raise NotImplementedError


class StripeAdapter(PluginAdapter):
    async def execute(self, event: dict):
        if event.get("event_type") == "PAYMENT":
            return {
                "provider": "stripe",
                "status": "simulated_charge_success",
                "amount": event["payload"].get("amount", 0)
            }
