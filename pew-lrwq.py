import math
import os
import time

# Размеры экрана
width = 80
height = 40

# Константы для быстрого вычисления
A = 0
B = 0
while True:
    # Очистка экрана
    os.system('cls' if os.name == 'nt' else 'clear')

    # Параметры
    z = [0] * width * height
    b = [' '] * width * height

    # Рисуем тор
    for j in range(0, 628, 7):  # шаг по углу для оси Y (от 0 до 2*pi)
        for i in range(0, 628, 2):  # шаг по углу для оси X (от 0 до 2*pi)
            # Математика для 3D координат
            c = math.sin(i)
            d = math.cos(j)
            e = math.sin(A)
            f = math.sin(j)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(i)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(width / 2 + width / 8 * D * (l * h * m - t * n))
            y = int(height / 2 - height / 8 * D * (l * h * n + t * m))
            o = int(x + width * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if 0 <= y < height and 0 <= x < width and D > z[o]:
                z[o] = D
                b[o] = '.,-~:;=!*#$@'[N if N > 0 else 0]

    # Выводим 3D пончик
    for k in range(width * height):
        print(b[k], end='' if k % width else '\n')

    A += 0.04
    B += 0.02
    time.sleep(0.05)  # Задержка для плавности анимации






