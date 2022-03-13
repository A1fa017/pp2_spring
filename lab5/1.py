import re

text = input()
result = re.search('ab*',text)
print(result)