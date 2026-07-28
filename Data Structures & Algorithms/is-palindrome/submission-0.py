class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = s.strip().lower().replace(" ", "")
        
        cleaned_s = "".join(char for char in cleaned_s if char.isalnum())

        left_idx = 0
        right_idx = len(cleaned_s)-1

        while left_idx < right_idx:
            if cleaned_s[left_idx] == cleaned_s[right_idx]:
                left_idx += 1
                right_idx -= 1
            else:
                return False
        return True

