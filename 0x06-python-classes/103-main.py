#!/usr/bin/python3

MagicClass = __import__('103-magic_class').MagicClass

mc1 = MagicClass(12)

mc2 = MagicClass()

# mc3 = MagicClass("3")

mc = MagicClass(10)
print("{:.2f}".format(mc.area()))

