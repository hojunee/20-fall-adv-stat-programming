## Index is based on KOR version
## Ex 5.3

# prevent namespace conflict
def do_twice(f):
    f()
    f()

# Solution 1
def print_spam():
    print("spam")

do_twice(print_spam)

# Solution 2
def do_twice(func, arg):
    func(arg)
    func(arg)

# Soltion 3
def print_twice(arg):
    print(arg)
    print(arg)
print_twice("Sol 3")

# Solution 4
do_twice(print_twice, "spam")

# Solution 5
def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)

do_four(print, "Sol 5")

## Ex 5.3.

# Solution 1
def check_fermat(a, b, c, n):
    if (n > 2) and ((a ** n) + (b ** n) == (c ** n)):
        print("페르마가 틀렸다!")
    else:
        print("아냐, 그건 아니지.")

check_fermat(3, 4, 5, 2)

# Solution 2
def check_fermat_with_input():
    a = int(input("a를 입력하세요: "))
    b = int(input("b를 입력하세요: "))
    c = int(input("c를 입력하세요: "))
    n = int(input("n를 입력하세요: "))
    check_fermat(a, b, c, n)

check_fermat_with_input()