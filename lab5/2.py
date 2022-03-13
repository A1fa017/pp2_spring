import re

text = input()
result = re.search('ab{2,3}',text)
print(result)