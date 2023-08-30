#!/usr/bin/python3
import sys
pascal_triangle = __import__('12-pascal_triangle').pascal_triangle


if len(sys.argv) == 1:
    n = 0
elif len(sys.argv) > 2:
    print("Usage: test_pascal <n>", file=sys.stderr)
    sys.exit(1)
elif len(sys.argv) == 2:
    n = int(sys.argv[1])

tri = pascal_triangle(n)
for item in tri:
    print(item)
