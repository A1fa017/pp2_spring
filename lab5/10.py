import re

text = input()
camel = re.findall('[A-Z][a-z]*',text)
if text[0].isupper():
    snake = ''
else:
    text1 = re.split('[A-Z]',text)
    snake = text1[0]
for sub in camel:
    snake += re.sub(sub[0],'_'+sub[0].lower(),sub)
print(snake)