class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        lens = len(nums)-k+1
        res = [0 for i in range(lens)]
        for i in range(lens):
            res[i] = max(nums[i:i+k])
        return res