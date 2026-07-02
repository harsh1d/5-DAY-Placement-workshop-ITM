class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Compute the GCD of the lengths of the two strings
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        len1, len2 = len(str1), len(str2)
        gcd_len = gcd(len1, len2)

        # Candidate substring of length gcd_len
        candidate = str1[:gcd_len]

        # Check if candidate divides both strings
        if candidate * (len1 // gcd_len) == str1 and candidate * (len2 // gcd_len) == str2:
            return candidate
        else:
            return ""

def main():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    solution = Solution()
    result = solution.gcdOfStrings(str1, str2)
    print("The GCD of the two strings is:", result)

if __name__ == "__main__":
    main()
