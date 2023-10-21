class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        dist = 0
        mileage = None
        index = 0
        for i in range(len(gas)):
            val = gas[i]-cost[i]
            dist += val
            if val < 0:
                if mileage is not None:
                    mileage+=val

            else:
                if mileage is None or mileage < 0:
                    mileage = val
                    index = i
                else:
                    mileage += val
        if dist >= 0 : return index
        else: return -1

        
