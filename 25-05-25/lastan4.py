# работа с модулями/пакетами/библеотеками

#импорт всех функций из модуля
import random
num = random.randint(1, 10)

#импорт всех функций из модуля через псевдоним
import random as rnd
num2 = rnd.randint(1,10)

#импорт одной функции из модуля к модулю по имени обращаться не надо
from random import randint
num3 = randint(1, 10)

#импорт всех функций из модуля к модулю по имени обращатся не надо
from random import *
num4 =randint(1,10)

from string import ascii_uppercase
print(ascii_uppercase)