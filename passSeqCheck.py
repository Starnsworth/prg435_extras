#    Password checker that detects and blocks passwords with an increasing or decreasing sequence of 3 characters or more. Block passwords such as: ["1234567", "abc12"]


def checkPassSeq(string, length=3):
    for i in range(len(string) - length + 1):
        chunk = string[i:i + length]
        asc = all(ord(chunk[j+1]) - ord(chunk[j]) == 1 for j in range(length - 1))
        dsc = all(ord(chunk[j+1]) - ord(chunk[j]) == -1 for j in range(length - 1))
        if asc or dsc:
            return True, chunk
    return False, None

userPass = input("Enter your password : ")
print(checkPassSeq(userPass))