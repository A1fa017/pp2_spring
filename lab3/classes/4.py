class Point():
    def __init__(self, x0, y0):
        self.x0 = x0
        self.y0 = y0
    def show(self):
        print(self.x0, self.y0)
    def move(self):
        x1,y1 = map(int,input().split())
        self.x1 = x1
        self.y1 = y1
    def dist(self):
        d = ((self.x1-self.x0)**2+(self.y1-self.y0)**2)**0.5
        print(d)
p = Point(1, 2)
p.move()
p.dist()


