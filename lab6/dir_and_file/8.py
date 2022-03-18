import os

path = open('text.txt')

if os.path.exists(path):
  os.remove(path)
else:
  print("The file does not exist")