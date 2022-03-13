import re

text = input()
result = re.search('a.*b$',text)
print(result)