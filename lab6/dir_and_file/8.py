import os

if os.path.exists(r"C:\pp2\lab6\dir_and_file\text.txt"):
  os.remove("C:\pp2\lab6\dir_and_file\text.txt")
else:
  print("The file does not exist")