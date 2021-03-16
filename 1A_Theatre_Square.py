import math
n, m, a = map(int, input().split())
length=-(-n//a)
width=math.ceil(m/a)
print(length*width)
