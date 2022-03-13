import re

text = input()
result = re.findall('[A-Z][a-z]*',text)
print(result)