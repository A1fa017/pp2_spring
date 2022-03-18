import os
path = open('text.txt')
print(path.readable())
print(path.writable())
if os.path.exists("C:\pp2\text.txt"):
    print("True")
else:
    print("False")
print(os.access('C:\pp2\text.txt', os.X_OK))