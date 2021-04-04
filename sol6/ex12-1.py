def sumall(*args):
    result = 0
    for elem in args:
        result += elem
    return result

print(sumall(1, 2, 3))
print(sumall(1, 4, 7, 10))
print(sumall(25, 75, 100, 200))