def gcd(a, b):
    if (b == 0):
        return a

    return gcd(b, a%b)

print(gcd(17, 2))
print(gcd(6, 3))
print(gcd(42, 63))