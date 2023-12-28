less20 =["","one","two","three","four","five","six",
         "seven","eight","nine","ten","eleven","twelve",
         "thirteen","fourteen","fifteen","sixteen","seventeen",
         "eighteen","nineteen"]
tens = ["","","twenty","thirty","forty","fifty","sixty",
        "seventy","eighty","ninety"]

def oneTo19(number):
    "Handles if number is between 0 to 19"
    return less20[number];

def twentyTo99(number) :
    "Handles if number is between 0 to 99"
    if number < 20:
        return oneTo19(number)
    else :
        quotient = number // 10
        remainder = number % 10
        return tens[quotient] + " " + oneTo19(remainder);

def hundreds(number):
    "Handles if number is between 0 to 999"
    if number < 100:
        return twentyTo99(number)
    else :
        quotient = number // 100
        remainder = number % 100
        return oneTo19(quotient) + " hundred " + twentyTo99(remainder)

def thousands(number) :
    "Handles if number is between 0 to 999,999"
    if number < 1000:
        return hundreds(number)
    else :
        quotient = number // 1000
        remainder = number % 1000
        return hundreds(number) + " thousand " + hundreds(remainder)

def millions(number):
    "Handles if number is between 0 to 999,999,999"
    if number < 1000000:
        return thousands(number)
    else :
        quotient = number // 1000000
        remainder = number % 1000000
        return hundreds(quotient) + " million " + thousands(remainder)

def billions(number):
    "Handles if number is between 0 to 3999,999,999"
    if number < 1000000000 :
        return millions(number)
    elif number > 4000000000 :
        return "Too big for translation"
    else :
        quotient = number // 1000000000
        remainder = number % 1000000000
        return hundreds(quotient) + " billion " + millions(remainder)
    
def num2English(number):
    return billions(number)

bignumber = int(input("Enter a number "))
numword = num2English(bignumber)
print(f"The number {bignumber} in English word is {numword}")
