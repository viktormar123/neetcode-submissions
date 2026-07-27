class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        diff_dict = {}

        if len(s) != len(t):
            return False
        n = len(s)

        for i in range(n):
            char_s = s[i]
            char_t = t[i]
            if char_s in diff_dict:
                diff_dict[char_s] += 1
            else:
                diff_dict[char_s] = 1
            
            if char_t in diff_dict:
                diff_dict[char_t] -= 1
            else:
                diff_dict[char_t] = -1
            
        for i in diff_dict:
            if diff_dict[i] != 0:
                return False
        else:
            return True