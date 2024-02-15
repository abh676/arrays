class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        left = 0
        right = (max(price) - min(price)) // (k - 1) + 1
        price.sort()
        def check(x):
            cnt = 1
            prev = price[0]
            for p in price:
                if p >= prev + x:
                    cnt += 1
                    if cnt >= k: return True
                    prev = p
            return False
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid): left = mid + 1
            else: right = mid - 1
        return right
