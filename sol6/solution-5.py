def get_abs():
    try:
        ipt = int(input())
        print(abs(ipt))
    except ValueError:
        print("Your input is not integer")

get_abs()