import re

text = input()
result = re.findall('[A-Z][^A-Z]*',text)
for sub in result:
    print(sub,end = ' ')