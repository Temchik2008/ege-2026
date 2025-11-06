from re import finditer
with open('regexp-practice-1.txt') as file:
    data = file.read()
pattern = r'\b[Cc][Aa][Tt]\b'
matches  = [match.group() for match in finditer(pattern, data)]
print(matches)