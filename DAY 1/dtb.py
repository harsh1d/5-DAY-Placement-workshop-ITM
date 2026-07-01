def decimal_to_binary_builtin(n):
	return bin(n)[2:]  


def decimal_to_binary_manual(n):
	if n == 0:
		return '0'
	
	binary = ''
	while n > 0:
		binary = str(n % 2) + binary  
		n = n // 2                     
	return binary


if __name__ == '__main__':
	num = int(input("Enter decimal number: "))
	
	# Using built-in method
	print(f"Binary (built-in): {decimal_to_binary_builtin(num)}")
	
	# Using manual method
	print(f"Binary (manual): {decimal_to_binary_manual(num)}")
