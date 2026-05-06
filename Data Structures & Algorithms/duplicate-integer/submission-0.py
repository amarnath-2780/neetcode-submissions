class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = []
        for item in nums:
            if item in values:
                return True
            values.append(item)
        return False