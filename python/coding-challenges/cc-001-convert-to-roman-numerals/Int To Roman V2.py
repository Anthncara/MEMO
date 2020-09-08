print("###  This program converts decimal numbers to Roman Numerals ###",'\nTo exit the program, please type "exit")')

def InttoRoman(number):
    int_roman_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),\
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    if not number.isdigit():
        return "Not Valid Input !!!"
    number = int(number)
    if (number > 3999) or (number < 1):
        return "Not Valid Input !!!"
    result = ""
    while number > 0:
        for i, roman in int_roman_map:
            while number >= i:
                result += roman
                number -= i
    return result
    
while True:
    number = input("Please enter a number between 1 and 3999, inclusively : ")
    if number == "exit":
        print("Exiting the program... Good Bye")
        break
    print(InttoRoman(number))
