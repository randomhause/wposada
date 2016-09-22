def gcd(a, b):
    while b != 0:
        c = b
        b = a % b 
        a = c
    return a
print(gcd(6, 12))

#work with a group
