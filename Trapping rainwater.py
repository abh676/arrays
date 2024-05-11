class Solution:
	def trap(self, height: List[int]) -> int:
		lh, rh = height[0], height[-1]
		l, r = 0, len(height)-1
		res = 0

		while l < r:
			if height[l] < height[r]:
				res += max(lh-height[l] ,0)
				lh = max(lh,height[l])
				l += 1
			else:
				res += max(rh-height[r] ,0)
				rh = max(rh,height[r])
				r -= 1

		return res
