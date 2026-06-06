import asyncio
from collections import deque

class NexusEventQueue:
    def __init__(self):
        self.queue = deque()
        self.lock = asyncio.Lock()

    async def push(self, event: dict):
        async with self.lock:
            self.queue.append(event)

    async def pop(self):
        async with self.lock:
            if self.queue:
                return self.queue.popleft()
            return None
