
def is_palindrome_number(x: int) -> bool:
	"""Return True if integer x is a palindrome (reads same forwards/backwards)."""
	if x < 0:
		return False
	s = str(x)
	return s == s[::-1]


if __name__ == '__main__':
	try:
		n = int(input().strip())
	except Exception:
		print('Invalid input')
	else:
		print(is_palindrome_number(n))
