class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        new = sorted(nums)
        for i in range(len(new)):
            if new[i] > 0:
                break
            if i > 0 and new[i] == new[i-1]:
                continue
            j = i + 1
            k = len(new) - 1
            while j < k:
                current_sum = new[i] + new[j] + new[k]
                if current_sum == 0:
                    result.append([new[i], new[j], new[k]])
                    j += 1
                    k -= 1
                    while j < k and new[j] == new[j - 1]:
                        j += 1
                elif current_sum < 0:
                    j += 1
                else: 
                    k -= 1
        return result
