class EventReplayEngine:
    def __init__(self, ledger):
        self.ledger = ledger

    def replay(self, filter_fn=None):
        for event in self.ledger:
            if filter_fn and not filter_fn(event):
                continue
            yield event
