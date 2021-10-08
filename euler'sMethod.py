
h = 0.1; x = 1; y = 1
for i in range(4):
    y1 = y + h*((3*y)+(3*x*y))
    print(y1)
    y = y1
    x +=0.1
print(y)
