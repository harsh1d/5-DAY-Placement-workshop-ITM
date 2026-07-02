class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s_list = list(s)
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s_list[left] in vowels:
                if s_list[right] in vowels:
                    s_list[left], s_list[right] = s_list[right], s_list[left]
                    left += 1
                    right -= 1
                else:
                    right -= 1
            else:
                left += 1
        
        return ''.join(s_list)