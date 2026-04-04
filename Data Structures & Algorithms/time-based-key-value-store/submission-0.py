class TimeMap:

    def __init__(self):
        self.store=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        res=""
        for item in self.store[key]:
            if item[1]==timestamp:
                return item[0]
            if item[1]<timestamp:
                res=item[0]
            else:
                break
        return res
