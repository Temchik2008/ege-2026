num = input()
product = 1 #это будет переменная для хранения произведения цифр
for digit in num:
    product *= int(digit)
print(product)
