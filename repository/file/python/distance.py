import math

x1, y1 = eval(input("x1, y1: "))
x2, y2 = eval(input("x2, y2: "))

distance = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
print(f'Distance is {distance}')
