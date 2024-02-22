class Solution:
    def myPow(self, x: float, n: int) -> float:
        myPow = (x,n//2)

        if n == 0:

            return 1

        elif n < 0:

            return 1 / self.myPow(x, -n)

        elif n % 2 == 0:

            half_power = self.myPow(x, n // 2)

            return half_power * half_power

        else:

            return x * self.myPow(x, n - 1)

        
