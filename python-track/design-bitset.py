class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bit = [0 for i in range(size)]
        self.bit_n = [1 for i in range(size)]
        self.ones = 0
        self.zero = size

    def fix(self, idx: int) -> None:
        self.zero -= not self.bit[idx]
        self.ones += not self.bit[idx]
        self.bit[idx] = 1
        self.bit_n[idx] = 0

    def unfix(self, idx: int) -> None:
        self.zero += self.bit[idx]
        self.ones -= self.bit[idx]
        self.bit[idx] = 0
        self.bit_n[idx] = 1

    def flip(self) -> None:
        self.ones,self.zero = self.zero,self.ones
        self.bit,self.bit_n = self.bit_n,self.bit

    def all(self) -> bool:
        return self.ones == self.size

    def one(self) -> bool:
        return bool(self.ones)

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        return "".join(["1" if bit else "0" for bit in self.bit])