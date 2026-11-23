class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]
        self.last_zero = -1
    def add(self, num: int) -> None:
        if num == 0:
            self.last_zero = len(self.prefix)
            self.prefix.append(1)
        else:
            self.prefix.append(self.prefix[-1] * num)
    def getProduct(self, k: int) -> int:
        if len(self.prefix) - k <= self.last_zero:
            return 0
        return self.prefix[-1] // self.prefix[-1 - k]