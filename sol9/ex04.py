from random import randint

def gen_matrix():
    mat_1 = [[randint(0, 100) for _ in range(3)] for _ in range(3)]
    mat_2 = [[randint(0, 100) for _ in range(3)] for _ in range(3)]

    mat_mul = [[mat_1[i][j]*mat_2[i][j] for j in range(3)] for i in range(3)]

    print("matrix 1 :", mat_1)
    print("matrix 2 :", mat_2)
    print("multiply matrix elementwise :", mat_mul)

gen_matrix()