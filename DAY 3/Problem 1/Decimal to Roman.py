def decimal_to_roman(num):
    val = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]
    roman = ''
    for (i, syb) in val:
        while num >= i:
            roman += syb
            num -= i
        if num == 0:
            break
    return roman
num = int(input("Enter a decimal number: "))
print("Roman numeral:", decimal_to_roman(num))