import json

class DistributedLedger:
    def __init__(self, path):
        self.path = path

    def append(self, event):
        try:
            with open(self.path, "r") as f:
                data = json.load(f)
        except:
            data = []

        data.append(event)

        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)
