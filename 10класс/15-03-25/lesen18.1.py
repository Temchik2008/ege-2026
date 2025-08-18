import random

n = [random.randint(0, 1000) for i in range(100)]
n[0], n[-1] = n[-1], n[0]
print(n)