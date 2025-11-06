from re import finditer
with open('regexp-practice-3.txt') as file:
    data = file.read()
pattern = r'\d+(\.\d+)?'
matches  = [match.group() for match in finditer(pattern, data)]
print(matches)