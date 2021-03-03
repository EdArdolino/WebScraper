import hashlib

flag = 0
counter = 0;

pass_hash = input ("Enter MD5 hash: ")

wordlist = input ("File name: ")

try:
    pass_file = open (wordlist, "r")
except:
    print("File not found")
    quit()

for word in pass_file:

    enc_word = word.encode('utf-8')
    digest = hashlib.md5(enc_word.strip()).hexdigest()

    counter += 1

    if digest == pass_hash:
        print("Password found")
        print("Password: " + word)
        print(counter)
        flag = 1
        break

if flag == 0:
    print("Password not in the list")