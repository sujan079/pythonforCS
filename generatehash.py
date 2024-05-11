import hashlib
password="suyog123"
hash=hashlib.sha256(password.encode('utf-8'))
print(hash.hexdigest())
#prints the hashes in the password