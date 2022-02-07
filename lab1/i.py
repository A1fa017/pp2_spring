for x in range(int(input())):
    s = input()
    if s.find('@gmail.com')!=-1:
        s = s.strip('@gmail.com')
        print(s)