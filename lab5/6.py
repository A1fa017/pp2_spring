import re
import random

l = [',',':']
s = random.choice(l)
text = input()
result = re.sub(' ',s,text)
print(result)