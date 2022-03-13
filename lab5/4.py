import re

text = input()
result = re.search('[A-Z][a-z]+',text)
print(result)