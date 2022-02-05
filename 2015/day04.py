import hashlib

print(hashlib.md5("abcdef609043".encode("UTF-8")).hexdigest())

def is_leading_zero(num):
    s1 = "iwrupvqb"
    md5 = hashlib.md5("{}{}".format(s1, num).encode("UTF-8")).hexdigest()
    return md5.startswith("000000")

for i in range(0, 10000000):
    if is_leading_zero(i):
        print(i)
        break