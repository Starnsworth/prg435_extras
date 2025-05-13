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
        print("Password is valid 1")
        checkPassword(userpass)
    elif len(userpass)>= 14:
        print("Password is valid")
        checkPassword(userpass,3)
    else:
        print("Password too short.")

testList = [
    "Ab!1234567",        # 10 chars: valid all 4
    "Abcdefghij",        # 10 chars: missing number/symbol
    "!bcdefghij",        # 10 chars: missing uppercase
    "1bcdefghij",        # 10 chars: missing uppercase/symbol
    "abcdefghijklmn",    # 14 chars: no upper, no number/symbol
    "ABCdefghijklmn",    # 14 chars: no number/symbol
    "1bcdefghijklmn",    # 14 chars: not enough uppercase
    "!bcdefghijklmn",    # 14 chars: not enough uppercase
    "ABc!defGHIjklmn",   # 15 chars: valid (3+ uppers, 3+ lowers, 1 symbol)
    "Abc!defGhij",       # 11 chars: valid (all 4)
    "AbcdefGhijkl",      # 12 chars: only 2 rules (upper & lower)
]
for pw in testList:
    print(f"testing: {pw}")
    beginComparison(pw)