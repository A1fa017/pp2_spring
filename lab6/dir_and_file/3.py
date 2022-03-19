import os
path = r"C:\pp2\lab6\dir_and_file\text.txt"
if os.path.exists(path):    
    print(os.path.basename(path))
    print(os.path.dirname(path))