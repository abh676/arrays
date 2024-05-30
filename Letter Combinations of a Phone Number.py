class Solution:
    def letterCombinations(self, digits):
        result = []
        digitLetters = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
        }
        digits = list(str(digits))
        if len(digits) == 0:
            return []
        else:
            i = 0
            while i<len(digits):
                if len(result) == 0:
                    result = self.permutation(digitLetters[digits[i]], result)
                else:
                    result = self.permutation(result, digitLetters[digits[i]])
                i += 1
        return result
        
    def permutation(self, list1, list2):
        result = []
        for i in list1:
            if len(list2)>0:
                for j in list2:
                    result.append(i+j)
            else:
                result.append(i)                
        return result
