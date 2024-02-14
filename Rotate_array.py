class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        a = nums.copy()
        n = len(nums)

        for i in range(0, n):
            rem = (i+k) % n
            nums[rem] = a[i]
