class ProductOfNumbers:

    def __init__(self):
        self.number_stream = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.number_stream = [1]
        else:
            self.number_stream.append(self.number_stream[-1]*num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.number_stream):
            return 0
        return self.number_stream[-1] // self.number_stream[-(k+1)]
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)