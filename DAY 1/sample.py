def decimal_to_binary(n):
    binary = ""
    while n > 0:
        remainder = n % 2        
        binary = str(remainder) + binary  
        n = n // 2               
    return binary if binary else "0"

# Example usage
num = int(input("Enter a decimal number: "))
print("Binary representation:", decimal_to_binary(num))
