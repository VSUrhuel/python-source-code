less20 =["","isa","dalawa","tatlo","apat","lima","anim",
         "pito","walo","siyam","sampo","labing-isa","labindalawa",
         "labintatlo","labing-apat","labinlima","labing-anim","labinpito",
         "labingwalo","labinsiyam"]
tens = ["","","dalawampu","tatlumpu","apatnapu","limampu","animnapu",
        "pitumpu","walumpu","siyamnapu"]

def oneTo19(number):
    #“Handles if number is between 0 to 19”
    return less20[number];

def twentyTo99(number) :
    #“Handles if number is between 0 to 99”
    if number < 20:
        return oneTo19(number)
    else :
        quotient = int(number // 10)
        remainder = number % 10
        if(remainder == 0):
            return tens[quotient]
        else:
            return tens[quotient] +  "'t " + oneTo19(remainder)

def hundreds(number):
    #“Handles if number is between 0 to 999”
    if number < 100:
        return twentyTo99(number)
    else :
        quotient = number // 100
        remainder = number % 100
        if(remainder == 0 and (quotient == 4 or quotient == 6 or quotient == 9)):
            return oneTo19(quotient) + " na daan"
        elif(remainder == 0):
            return oneTo19(quotient) + "ng daan"
        if(quotient == 4 or quotient == 6 or quotient == 9):
             return oneTo19(quotient) + " na daan at " + twentyTo99(remainder)
        else:
            return oneTo19(quotient) + "ng daan at " + twentyTo99(remainder)

def thousands(number) :
    #“Handles if number is between 0 to 999,999”
    if number < 1000:
        return hundreds(number)
    else :
        quotient = int(number // 1000)
        remainder = number % 1000
        if(remainder == 0 and (quotient == 4 or quotient == 6 or quotient == 9)):
            return hundreds(quotient) + " na libo"
        elif(remainder == 0):
            return hundreds(quotient) + "ng libo"
        x = quotient % 10;
        if(x == 4 or x == 6 or x == 9):
            return hundreds(quotient) + " na libo't " + hundreds(remainder)
        else:
            return hundreds(quotient) + "ng libo't " + hundreds(remainder)

def millions(number):
    #“Handles if number is between 0 to 999,999,999”
    if number < 1000000:
        return thousands(number)
    else :
        quotient = int(number // 1000000)
        remainder = number % 1000000
        if(remainder == 0 and (quotient == 4 or quotient == 6 or quotient == 9)):
            return hundreds(quotient) + "na milyon"
        elif(remainder == 0):
            return hundreds(quotient) + "ng milyon"
        x = quotient % 10;
        if(x == 4 or x == 6 or x == 9):
           return hundreds(quotient) + " na milyon at " + thousands(remainder)
        else:
            return hundreds(quotient) + "ng milyon at " + thousands(remainder)

def billions(number):
    #“Handles if number is between 0 to 3999,999,999”
    if number < 1000000000 :
        return millions(number)
    elif number > 4000000000 :
        return "Malaking numero para sa translasyong ito"
    else :
        quotient = int(number / 1000000000)
        remainder = number % 1000000000
        if(remainder == 0 and (quotient == 4 or quotient == 6 or quotient == 9)):
            return hundreds(quotient) + "na bilyon "
        elif(remainder == 0):
            return hundreds(quotient) + "ng bilyon"
        if(quotient == 4 or quotient == 6 or quotient == 9):
             return hundreds(quotient) + " na bilyon at" + millions(remainder)
        else:
            return hundreds(quotient) + "ng bilyon " + millions(remainder)
    
def num2English(number):
    return billions(number)

bignumber = int(input("Enter a number "))
numword = num2English(bignumber)
print(f"Ang {bignumber} sa Filipino ay {numword}")