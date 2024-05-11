import hashlib
password="suyog123"
<<<<<<< HEAD
hash=hashlib.sha256(password.encode('utf-8'))
print(hash.hexdigest()) 
=======
hash=hashlib.sha256(password.encode('utf-8'))# hashing using sha256 alogrithm
print(hash.hexdigest())
#prints the hashes in the password
>>>>>>> branch1
