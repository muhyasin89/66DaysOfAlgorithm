hash = "827ccb0eea8a706c4c34a16891f84e7b"

def crack(hash):
    import hashlib

    for i in range(100000):
        password = f"{i:05d}" #str.zfill(5) #number zero
        print(password)
        if hashlib.md5(password.encode()).hexdigest() == hash:
           return password

# crack(hash)