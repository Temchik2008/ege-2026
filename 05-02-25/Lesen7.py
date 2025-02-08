# cтроки
from itertools import count
from operator import index

# получение численного занчения символа
# Строки
from itertools import combinations

# Получение численного значения символа
print(ord('A'))

# Получение символа по числовому значению
print(chr(65))

# При сравнении строк сравниваются только числовые значения первых символов
if 'AZ' < 'ZA':
    print('+')

# Задача
# Считать с клавиатуры строку
# Вывести самый часто встречающийся символ
# Использовать списки, ord, chr

text = input()
counters = [0] * 26
for i in text:
    pos = ord(i) - ord('a')
    counters[pos] += 1

max_num = 0
max_pos = 0
for i in range(26):
    if counters[i] > max_num:
        max_num = counters[i]
        max_pos = i

print(chr(max_pos + ord('a')))

print(chr(counters.index(max(counters)) + ord('a')))

text = input()
count = [0] * 128
for i in text:
    pos = ord(i) - ord("a")
    count[pos] += 1
maax = max(count)
print(chr(count.index(maax) + ord("a")))
