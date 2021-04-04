from math import sqrt as module_sqrt

epsilon = 0.000000001

def newton_sqrt(a):
    x = a
    while True:

        y = (x + a/x) / 2
        if (abs(y - x) < epsilon):
            return y
        x = y

n = 1.0
while (n <= 9.0):

    n_sqrt = newton_sqrt(n)
    m_sqrt = module_sqrt(n)
    print('{:<5} {:<20} {:<20} {:<20}'.format(n, n_sqrt, m_sqrt, abs(n_sqrt - m_sqrt)))
    n = n + 1