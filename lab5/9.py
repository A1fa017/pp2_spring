import re

text = input()
result = re.findall('[A-Z][a-z]*',text)
for sub in result:
    print(sub,end = ' ')