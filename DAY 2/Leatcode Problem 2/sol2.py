class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Compute the GCD of the lengths of the two strings
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        len1, len2 = len(str1), len(str2)
        gcd_len = gcd(len1, len2)

        # Check if the substring of length gcd_len divides both strings
        candidate = str1[:gcd_len]
        if candidate * (len1 // gcd_len) == str1 and candidate * (len2 // gcd_len) == str2:
            return candidate
        else:
            return ""