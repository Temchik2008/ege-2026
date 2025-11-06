from re import finditer
with open('regexp-practice-5.txt', encoding='utf-8') as file:
    data = file.read()
pattern = r'\b[A-ZA-ЯЁ][a-za-яё]*\b'
matches  = [match.group() for match in finditer(pattern, data)]
print(matches)


