class Solution:
    # s字符串
    def isNumeric(self, str):
        # write code here
        sign = False
        decimal = False
        hasE = False
        
        for i in range(0, len(str)):
            if str[i] == 'e' or str[i] == 'E':
                if i == (len(str) - 1):
                    return False
                if hasE:
                    return False
                hasE = True
            elif str[i] == '+' or str[i] == '-':
                if sign and str[i-1] != 'e' and str[i-1] != 'E': 
                    return False
                if not sign and i > 0 and str[i-1] != 'e' and str[i-1] != 'E': 
                    return False
                sign = True
            elif str[i] == '.':
                if hasE or decimal:
                    return False
                decimal = True
            elif str[i] < '0' or str[i] > '9':
                return False
        return True