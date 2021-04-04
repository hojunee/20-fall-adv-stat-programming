def is_power(a, b):
    if (a == 0):
        return False
    if (a == 1):
        return True

    if ((a % b == 0) and is_power(a/b, b)):
        return True
    else:
        return False

print(is_power(4, 2))
print(is_power(1, 10))
print(is_power(3, 2))
print(is_power(16, -4))