#    MD5 hash a password entered by the user.
import hashlib


def gen_md5(password):

    md5 = hashlib.md5(password.encode('utf-8'))
    return md5.hexdigest()

#print(gen_md5(input("Enter Password to Hash: ")))