class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # This could also be done in python
        #count = collections.Counter(nums)
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        # using list method with index as frequency and value as actual number
        freq_arr = [[] for _ in range(len(nums)+ 1)] 
        for num, freq in count.items():
            freq_arr[freq].append(num)
        result = []
        for bucket in freq_arr[::-1]:
            for num in bucket:
                result.append(num)
                if len(result) == k:
                    return result
        

        
