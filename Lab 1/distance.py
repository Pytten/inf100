
x1 = float(input())
print(f"x1 is {x1}")
y1 = float(input())
print(f"y1 is {y1}")
x2 = float(input())
print(f"x2 is {x2}")
y2 = float(input())
print(f"y2 is {y2}")

x = (x2-x1)**2
y = (y2-y1)**2
avstand = (x + y)**0.5

print(f"avstanden mellom de to punktene er: {avstand}")