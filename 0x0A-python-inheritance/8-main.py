#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

r = Rectangle(3, 5)

print(r)
print(dir(r))

print(r.width)
print(r.height)

try:
    print("Rectangle: {} - {}".format(r.width, r.height))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    r2 = Rectangle(4, True)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
