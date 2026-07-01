num = input().strip()
total = 0

for ch in num:
	if ch.isdigit():
		total += int(ch)

print(total)
