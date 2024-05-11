import hashlib
passoword="suyog123"
hash=hashlib.sha256(passoword.encode('utf-8'))
print(hash.hexdigest())