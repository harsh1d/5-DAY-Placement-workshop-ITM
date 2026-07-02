class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        
        write_index = 0
        i = 0
        
        while i < len(chars):
            char = chars[i]
            count = 0
            
            # Count the number of consecutive occurrences of 'char'
            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1
            
            # Write the character to the result array
            chars[write_index] = char
            write_index += 1
            
            # If the count is more than 1, write the count as digits
            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1
        
        return write_index