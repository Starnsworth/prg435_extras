#    Password checker that does not permit duplicate characters together. These passwords will be detected and blocked. ["0000000000", "aabbccddeeffgg", "abc123@#$$"]

def checkforduplicates(userpass):
    prevChar = ''
    for char in userpass:
        if char != prevChar :
            prevChar = char
        else:
            print("Found duplicate character")
            return False
    print("Password complies with rules")

userpass = input("Enter password to check: ")
checkforduplicates(userpass)