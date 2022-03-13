import re

text = input().split('_')
camel = text[0]
text.remove(text[0])
for snake in text:
    camel += re.sub('^.',snake[0].upper(),snake)
print(camel)