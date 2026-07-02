class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string into words, using split() which automatically handles multiple spaces
        words = s.split()
        # Reverse the list of words
        words.reverse()
        # Join the reversed words with a single space
        return ' '.join(words)