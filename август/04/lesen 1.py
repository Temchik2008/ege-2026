with open('UserData.txt', encoding='utf-8') as file:
    data = file.readline()
# data = list(data)
# numbers = []
# for i in  data:
#     if i == '+':
#         start = data.index(i)
#         number = data[start:start+18]
#         numbers.append(''.join(number))
#         data[start] = ' '
# print(numbers)
numbers = []
for i in range(len(data)):

    if data[i] == "+":
        number = data[i:i+18]
        numbers.append(number)
print(numbers)




