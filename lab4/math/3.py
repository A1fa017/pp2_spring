import math

n = int(input())
length = float(input())
perimeter = length*n
apothem = length/(2*math.tan(math.radians(180/n)))
area = (perimeter*apothem)/2

print(int(area))