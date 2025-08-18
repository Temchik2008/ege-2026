import random
num = random.randint(0, 100)
if num % 3 == 0:
    result = num // 3
else:
    result = num * 2
print("Результат:", result)