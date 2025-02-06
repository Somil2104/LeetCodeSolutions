class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        diff1 = []
        diff2 = []
        
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1
                diff1.append(s1[i])
                diff2.append(s2[i])   
        if count == 0:
            return True
        elif count == 2:
            return diff1[0] == diff2[1] and diff1[1] == diff2[0]
        else:
            return False
