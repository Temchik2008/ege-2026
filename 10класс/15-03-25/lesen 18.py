# эксперимент: мы сравнивали две функции f1 и f2, измеряя их производительность с помощью timeit.
# 1. f1(data) → использует метод reverse(), который изменяет список на месте.
# 2. f2(data) → создаёт новый список data[::-1], не изменяя оригинальный.
# Затем мы запускали каждую функцию **10 миллионов раз** и измеряли время их выполнения.
#  Вывод:
#  reverse() быстрее, так как меняет список без создания нового.
#  [::-1] медленнее, так как требует выделения памяти для нового списка.
from timeit import timeit
from random import randint


def f1(data):
    data.reverse()


def f2(data):
    data = data[::-1]


data = []
for i in range(1000):
    data.append(randint(1, 1_000_000))

print(timeit('f1(data)', globals=globals(), number=10_000_000))
print(timeit('f2(data)', globals=globals(), number=10_000_000))
