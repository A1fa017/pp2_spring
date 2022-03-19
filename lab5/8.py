import re

text = input()
result = re.findall('[A-Z][^A-Z]*',text)
print(result)