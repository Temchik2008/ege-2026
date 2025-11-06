from re import match
with open('regexp-practice-2.txt') as file:
    data = file.readlines()
pattern = r'\b[Aa].*'
a = []
for line in data:
    res = match(pattern, line)
    if res != None:
        print(res.group())
