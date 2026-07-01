print("Check for number is prime or not")

i = int(input("Enter a value = "))

if i < 0:
    print("Error: Negative numbers cannot be prime")

elif i == 0 or i == 1:
    print(f"{i} is NOT a prime number")

else:
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{i} is a PRIME number")
    else:
        print(f"{i} is NOT a prime number")