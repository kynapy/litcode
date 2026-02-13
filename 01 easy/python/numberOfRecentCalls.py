# 933. Number of Recent Calls
# https://leetcode.com/problems/number-of-recent-calls/description/
# Attempts: 1


class RecentCounter:
    def __init__(self) -> None:
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        for i in range(len(self.requests)):
            if self.requests[i] >= t - 3000:
                self.requests = self.requests[i:]
                break
        return len(self.requests)


### TEST CASES
c1 = RecentCounter()
print(c1.ping(1))
print(c1.ping(100))
print(c1.ping(3001))
print(c1.ping(3002))
