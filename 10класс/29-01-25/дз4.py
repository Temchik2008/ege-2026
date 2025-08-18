
# Проверка числа на простоту
num = int(input())

start = time()
# Первый способ без оптимизации
for i in range(2, num): # 17
    if num % i == 0:
        print('Число непростое')
        break
else:
    print('Число простое')
print(time() - start)

start = time()
# Второй способ с оптимизацией в два раза
for i in range(2, num // 2 + 1): # 17
    if num % i == 0:
        print('Число непростое')
        break
else:
    print('Число простое')
print(time() - start)

start = time()
# Третий способ самый эффективный
for i in range(2, int(num ** 0.5) + 1): # 17
    if num % i == 0:
        print('Число непростое')
        break
else:
    print('Число простое')
print(time() - start)