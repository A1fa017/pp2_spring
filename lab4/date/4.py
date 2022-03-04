from datetime import datetime as d
import math

l1 = list(map(int,input().split()))
d1 = d(l1[0],l1[1],l1[2],l1[3],l1[4],l1[5],l1[6])

l2 = list(map(int,input().split()))
d2 = d(l2[0],l2[1],l2[2],l2[3],l2[4],l2[5],l2[6])

dt = abs(d1-d2)
print(dt.seconds + dt.days*86400)