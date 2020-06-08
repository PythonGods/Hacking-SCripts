import hashlib

word=input("What is the word you wish to encode")
to_do=input("What do you wan to convert it into")

if to_do=="md5":
    enc=word.encode("utf-8")
    digest=hashlib.md5(enc.strip()).hexdigest()
    print(digest)
if to_do=="md2":
    enc=word.encode("utf-8")
    digest=hashlib.md2(enc.strip()).hexdigest()
    print(digest)
if to_do=="sha-1":
    enc=word.encode("utf-8")
    digest=hashlib.sha1(enc.strip()).hexdigest()
    print(digest)
if to_do=="sha3-256":
    enc=word.encode("utf-8")
    digest = hashlib.sha3_256
    print(digest)
if to_do=="sha3-512":
    enc=word.encode("utf-8")
    digest = hashlib.sha3_512(enc.strip()).hexdigest()
    print(digest) 
if to_do=="sha-256":
    enc=word.encode("utf-8")
    digest = hashlib.sha_256(enc.strip()).hexdigest()
    print(digest)
if to_do=="sha-512":
    enc=word.encode("utf-8")
    digest = hashlib.sha512(enc.strip()).hexdigest()
    print(digest)