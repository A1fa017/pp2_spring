from datetime import datetime

l = list(map(int,input().split()))
dt = datetime(l[0],l[1],l[2],l[3],l[4],l[5],l[6])
print(dt.strftime('%Y-%m-%d %H:%M:%S'))