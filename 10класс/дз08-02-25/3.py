import random
maxx = 0
lenn = 0
s = []
numbers = [random.randint(1, 1000) for x in range(100)]
for i in range(1, len(numbers)):
    if numbers[i] == numbers[i - 1]:
        lenn += 1
        if lenn > maxx: #проверяется стала ли длина текущей цепочки больше чем самая длинная цепочка найденная ранее
            maxx = lenn
            maxx = numbers[i]
        else:
            lenn = 1
print(maxx)
print(lenn)