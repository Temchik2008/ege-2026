data = 'hello'
data2 = [1,12,3,'g', 52]
data6 = (1,1,3,39, (311))
i = iter(data)
#— это объект, в котором реализована функция next(),
#возвращающая следующий элемент последовательности
print(next(i))
# Получить итератор от итерируемого объекта
# можно с помощью функции iter()
# Получить следующий объект итератора
# можно функцией next()
