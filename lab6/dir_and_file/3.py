import os
path = r"C:\pp2\text.txt"
if os.path.exists(path):    
    print(os.path.basename(path))
    print(os.path.dirname(path))