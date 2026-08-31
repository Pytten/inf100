

print('x1 =', end='')
x1 = int(input())
print('y1 =', end='')
y1 = int(input())
print('x2 =', end='')
x2 = int(input())
print('y2 =', end='')
y2 = int(input())

x = (x2-x1)**2
y = (y2-y1)**2
avstand = (x + y)**0.5

print(f"avstanden mellom ({x1}, {y1}) og ({x2}, {y2}) er {avstand}")