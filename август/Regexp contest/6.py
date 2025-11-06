from re import finditer
with open('regexp-practice-6.txt', encoding='utf-8') as file:
    data = file.read()
pattern = r'\b[A-ZA-ЯЁ]{2}-[0-9]{4}'
matches  = [match.group() for match in finditer(pattern, data)]
print(matches)