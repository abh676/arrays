class Solution:
    def mySqrt(self, x: int) -> int:
        sr =1

        while True:

            if x < sr*sr:

                return sr-1

            else:

                sr +=1
