class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        print(pairs)
        fleet = []
        for position, speed in pairs:
            time = (target - position) / speed #per/car
            if not fleet or time > fleet[-1]:
                fleet.append(time)
            

        res = len(fleet)
        return res
            
            

            