
def decimal_to_binary(n_str: str) -> str:
	"""Convert a decimal integer string to a binary string. Raises ValueError on invalid input."""
	s = n_str.strip()
	if not s:
		raise ValueError("empty input")
	# allow optional leading + or -
	try:
		n = int(s)
	except ValueError:
		raise ValueError(f"invalid integer: {s}")
	if n == 0:
		return '0'
	neg = n < 0
	n = abs(n)
	bits = []
	while n:
		bits.append('1' if n & 1 else '0')
		n >>= 1
	bin_str = ''.join(reversed(bits))
	return '-' + bin_str if neg else bin_str


if __name__ == '__main__':
	try:
		s = input("Enter decimal number: ").strip()
		print(decimal_to_binary(s))
	except Exception as e:
		print(f"Error: {e}")
