from datetime import datetime, timedelta

print('Yesterday:',datetime.now()-timedelta(days = 1))
print('Today:',datetime.now())
print('Tomorrow:',datetime.now()+timedelta(days = 1))