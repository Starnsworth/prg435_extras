#    Password checker that does not permit duplicate characters together. These passwords will be detected and blocked. ["0000000000", "aabbccddeeffgg", "abc123@#$$"]

def check_for_duplicates(userpass):
    prev_char = ''
    for char in userpass:
        if char != prev_char :
            prev_char = char
        else:
            return "Found duplicate character"
    return "Password complies with  duplicate character rules"

#userpass = input("Enter password to check: ")
#check_for_duplicates(userpass)