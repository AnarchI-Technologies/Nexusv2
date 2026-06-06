from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="LumenCore Nexus API Edge")

class Event(BaseModel):
    tenant_id: str
    event_type: str
    payload: dict

@app.post("/ingest")
async def ingest(event: Event):
    return {
        "status": "received",
        "tenant": event.tenant_id,
        "type": event.event_type,
        "payload": event.payload
    }
