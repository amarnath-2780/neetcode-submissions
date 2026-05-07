class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        values = {}

        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in values:
                return [values[temp], i ]
            else:
                values[nums[i]] = i
                
