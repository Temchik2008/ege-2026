import random

maxx = [0, 0]
numbers = [random.randint(1, 1000) for _ in range(1000)]
for i in range(len(numbers)):
    if maxx[1] < numbers[i]:
        maxx[1] = numbers[i]
        if maxx[0] < numbers[i]:
            maxx[1] = maxx[0]
            maxx[0] = numbers[i]
print(numbers)
print(sorted(numbers)[-2:])
print(maxx)
