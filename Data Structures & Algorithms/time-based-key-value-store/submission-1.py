class TimeMap:

    def __init__(self):
        self.keyStore = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        
        self.keyStore[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2
            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return res

        


# Are the timestimestamps defined by integers or DateTime
# Would there be instances where set() is called with the same key (also same value) and datetime.
# What are the constraints on the provided timestamp, since it's python it should fit reasonably within int
# Can there be no timestamp or no value? aka None


# length of key and value strs
# lowercase, uppercase or mixed case for key and value strs
# range of timestamp
# Are all the timestamps of set() always increasing in order
# How many calls would be made to get and set?

# {}

# str: [(timestamp, value)]
# str: [(1, str), (2, str), (3, str), (4, str), (5, str)]