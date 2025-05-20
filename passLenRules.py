#    A strong password needs any 2 of the following rules and 12 characters. One upper case, one lower case, one number, one symbol.
#    A password must have 10 characters and meet all 4 basic rules of One upper case, one lower case, one number, one symbol.
#    Alternatively it can have 14 characters and only 3 lowers, 3 uppers and one from either symbols or numbers.

def containsUpper(passtocheck, passcount=1):
    countUpper = 0
    for char in passtocheck:
        if char.isupper():
            countUpper += 1
    if countUpper < passcount:
        return False
    else:
        return True


def containsLower(passtocheck, passcount=1):
    countLower = 0
    for char in passtocheck:
        if char.islower():
            countLower += 1
    if countLower == 0:
        return False
    else:
        return True


def containsNumber(passtocheck, passcount=1):
    countNumber = 0
    for char in passtocheck:
        if char.isdigit():
            countNumber += 1
    if countNumber < passcount:
        return False
    else:
        return True


def containsSymbol(passtocheck, passcount=1):
    countSymbol = 0
    symbols = ["~","!","#","$","%","^","&","*","(",")","_","-","+","=","{","}",";",":","'",'"',"<",">",",","?","/","\\","|"]
    for char in passtocheck:
        if char in symbols:
            countSymbol += 1
    if countSymbol < passcount:
        return False
    else:
        return True

def checkPassword(passtocheck, passcount=1, rulespass=4):
    rulespassed = 0
    if containsUpper(passtocheck, passcount):
        rulespassed += 1
    else:
        print("Password should contain atleast 1 uppercase letter")
    if containsLower(passtocheck, passcount):
        rulespassed += 1
    else:
        print("Password should contain atleast 1 lowercase letter")
    if containsNumber(passtocheck, passcount):
        rulespassed += 1
    else:
        print("Password should contain atleast 1 number")
    if containsSymbol(passtocheck, passcount):
        rulespassed += 1
    else:
        print("Password should contain atleast 1 symbol")
    if rulespassed >= rulespass:
        print(f"Password is valid and passed {rulespassed} rules")
    elif rulespassed < rulespass:
        print(f"Password is invalid and passed {rulespassed} rules")

minlength = 10
#userpass = input("Enter your password: ")

def beginComparison(userpass):
    if 14 > len(userpass) >= minlength :
        return "Password is good length"
        checkPassword(userpass)
    elif len(userpass)>= 14:
        return "Password is very good length"
        checkPassword(userpass,3)
    else:
        return "Password too short."

