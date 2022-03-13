import re

text = input()
result = re.search('([a-z]_)+',text)
print(result)