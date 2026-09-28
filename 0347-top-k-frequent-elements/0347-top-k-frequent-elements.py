class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        buckets = [[] for _ in range(len(nums) + 1) ]
        for num, freq in count.items():
            buckets[freq].append(num)
        result = []
        for bucket in reversed(buckets):
            for num in bucket:
                result.append(num)
                if len(result) == k:
                    return result