class TimeMap:

    def __init__(self):
        self.md = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.md:
            self.md[key] = []
        self.md[key].append((value,timestamp))
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.md:
            return ""
        pair = self.md[key]
        l = 0 
        r = len(pair)-1
        while l<=r:
            mid = (l+r)//2
            if pair[mid][1] == timestamp:
                return pair[mid][0]
            elif pair[mid][1] > timestamp:
                r = mid-1
            else:
                l = mid+1
        return pair[r][0] if r>=0 else ""
        
        


# key: sorted array of tuples. set is o(1), timestamp always increasing. 
# woohoo, Note: For all calls to set, the timestamps are in strictly increasing order., that means mere append will be o(1)