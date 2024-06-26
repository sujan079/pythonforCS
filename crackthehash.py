import hashlib
usernamehash={}
with open('password.txt','r') as f:
    passwords=f.read().splitlines()

with open ('hashed.txt','r') as file:
    hashes=file.read().splitlines()
    for text in hashes:
        username = text.split(":")[0] #takes the line infront of :
        hash =text.split(":")[1] # takes the lines right side of the :
        usernamehash[username]=hash

for password in passwords:
    passhash=hashlib.sha256(password.encode('utf-8'))
    for username, hash in usernamehash.items():
        if hash==passhash.hexdigest():
            print(f"MAtch found\n{username}:{password}")