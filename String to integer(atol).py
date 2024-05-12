def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        match = re.match(r'^\s*([+|-]?\d+)', string)
        
        if match:
            integer = int(match.group())
            return max(-(1 << 31), min(integer, (1 << 31) - 1))
        
        return 0
