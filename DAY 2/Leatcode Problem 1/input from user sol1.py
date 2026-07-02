class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        limit = len1 if len1 < len2 else len2

        result = []
        append = result.append

        for index in range(limit):
            append(word1[index])
            append(word2[index])

        if len1 > limit:
            append(word1[limit:])
        if len2 > limit:
            append(word2[limit:])

        return "".join(result)

# Get input from the user
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

# Create an instance of the Solution class and call the method
solution = Solution()
merged_word = solution.mergeAlternately(word1, word2)

# Output the result
print("Merged word:", merged_word)