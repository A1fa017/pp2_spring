import os
for i in os.listdir('.'):
    print('-----',i)
    if os.path.isdir(i):
        for j in os.listdir(i):
            print('-----'*2,j)