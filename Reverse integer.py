def reverse(self, x):
        r=int(`abs(x)`[::-1]);return(r<2**31)*r*cmp(x,0)
