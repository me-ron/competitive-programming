class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        cars.sort()

        stack = []
        for pos, fast in cars:
            distance = (target - pos) / fast
            while stack and stack[-1] <= distance:
                stack.pop()
            stack.append(distance)

        return len(stack)