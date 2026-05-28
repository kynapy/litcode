# 901. Online Stock Span
# https://leetcode.com/problems/online-stock-span/description/
# Attempts: 2


class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        num_smaller = 1
        while self.stack and self.stack[-1][0] <= price:
            curr = self.stack.pop(-1)
            num_smaller += curr[1]
        self.stack.append((price, num_smaller))
        return num_smaller


### TEST CASES
def test_stock_spanner(tests):
    ss = StockSpanner()
    results = []
    for test in tests:
        results.append(ss.next(test))
    print(results)


test_stock_spanner([100, 80, 60, 70, 60, 75, 85])
test_stock_spanner([28, 14, 28, 35, 46, 53, 66, 80, 87, 88])
