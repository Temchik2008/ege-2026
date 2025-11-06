from re import finditer
with open('regexp-practice-4.txt') as file:
    data = file.read()
pattern = r'\d{1,2}-\d{1,2}-\d{4}'
matches  = [match.group() for match in finditer(pattern, data)]
print(matches)