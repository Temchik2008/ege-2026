
text = input('Введите строку: ')
old = input('Введите подстроку, которую нужно заменить: ')
new = input('Введите подстроку, которой нужно заменить: ')
count = int(input())
lenn = len(old)
while count:
    if old in text:
        index_old = text.index(old)
        g = text[:index_old ]
        text = text[index_old + lenn:]
        text = g + new + text

        count -= 1

    else:
        print('Нет такой подстроки в строке')
        count = 0
if count == 0:
    print(text)