import math

Point = int(input ("Enter number of polygon edges: "))

while Point < 3:
    Point = int(input("Please insert a value higher than two: "))

i = 0 
x = []
y = []

while i < Point:
    i = i + 1
    x.append (int(input(f"input coordinate x{i}: ")))
    y.append (int(input(f"input coordinate y{i}: ")))
    

print(f"{'Point':>3} {'x':>10} {'y':>10}")


j = 0
A = 0
Sx = 0
Sy = 0

while j < (Point-1):

    A = 1 / 2 * ((x [j + 1] + x[j]) * (y [j + 1] - y [j])) + A

    Sx = - 1 /6 * (x [j + 1] - x [j]) * (y[j+1] **2 + y [j] * y [j+1] + y[j] **2) + Sx
    Sy = 1 / 6 * (y [j + 1] - y [j]) * (x[j+1] **2 + x [j] * x [j+1] + x[j] **2) + Sy

    Ix = 1 / 12 * (x[j+1] - x[j])

    j = j + 1

print ("Area of the polygon", A)
print ("Static x Moment", Sx)
print ("Static y Moment", Sy)

