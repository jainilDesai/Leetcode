class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        s = set()
        for i in range(len(nums)):
            if len(s) and nums[i] in s:
                return True
            s.add(nums[i])
            if len(s) > k:
                s.remove(nums[i - k])
        return False