class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        sign_multiplier = 1
        neg_bound = pow(-2, 31) # -2147483648
        pos_bound = pow(2, 31) - 1 # 2147483647 

        s = s.strip()
        if len(s) == 0:
            return res

        if s[0] in ["-", "+"] :
            sign_multiplier = int(s[0] + "1") # int(-1) or int(+1)
            s = s[1:]

        
        for num in s:
            if not num.isnumeric():
                break
            # handles leading zeros !
            res = res * 10 + int(num)

        if res > pos_bound:
            return pos_bound if sign_multiplier == 1 else neg_bound

        return res * sign_multiplier