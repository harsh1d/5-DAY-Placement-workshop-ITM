# Method 1: Using Python's built-in int() function (Simplest)
def binary_to_decimal_builtin(binary_str):
	return int(binary_str, 2)  # int(string, base) - base 2 for binary


# Method 2: Using Manual Calculation (Educational)
def binary_to_decimal_manual(binary_str):
	decimal = 0
	power = 0
	
	# Traverse from right to left
	for digit in reversed(binary_str):
		if digit == '1':
			decimal += 2 ** power  # Add 2^power if digit is 1
		power += 1
	
	return decimal


# Method 3: Using Bit Shifting (Advanced but simple)
def binary_to_decimal_bitshift(binary_str):
	decimal = 0
	for digit in binary_str:
		decimal = (decimal << 1) | int(digit)  # Shift left and add digit
	return decimal


if __name__ == '__main__':
	binary = input("Enter binary number: ").strip()
	
	# Using built-in method
	print(f"Decimal (built-in): {binary_to_decimal_builtin(binary)}")
	
	# Using manual method
	print(f"Decimal (manual): {binary_to_decimal_manual(binary)}")
	
	# Using bit shift method
	print(f"Decimal (bit shift): {binary_to_decimal_bitshift(binary)}")
