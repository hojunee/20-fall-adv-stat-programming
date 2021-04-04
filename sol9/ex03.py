import matplotlib.pyplot as plt
import random

sample_size = 100000

domain = [i + 1 for i in range(sample_size)]
sample = [random.uniform(0, 1) for _ in range(sample_size)]

cumul_sum = 0
cumul_sample = []
for i in sample:
    cumul_sample.append(cumul_sum + i)
    cumul_sum += i

plt.plot(domain, cumul_sample)
plt.grid()
plt.show()