def roman_to_decimal(roman):
    values = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
        'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
        'C': 100, 'CD': 400, 'D': 500, 'CM': 900,
        'M': 1000
    }
    decimal = 0
    i = 0
    while i < len(roman):
        if i + 1 < len(roman) and values[roman[i]] < values[roman[i + 1]]:
            decimal += values[roman[i + 1]] - values[roman[i]]
            i += 2
        else:
            decimal += values[roman[i]]
            i += 1
    return decimal

roman_numeral = str(input("enter roman number"))  # Example input
print(f"Decimal value of {roman_numeral} is {roman_to_decimal(roman_numeral)}")
