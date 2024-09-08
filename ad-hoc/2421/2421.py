"""
BEE 2421 - Álbum de Fotos - Level 8 - Ad-hoc
"""

x,y = [int(i) for i in input().strip().split(" ")]
l0, h0 = [int(i) for i in input().strip().split(" ")]
l1, h1 = [int(i) for i in input().strip().split(" ")]

condiction = (
    l0 + l1 <= x and max(h0, h1) <= y or
    l0 + h1 <= x and max(h0, l1) <= y or
    l0 + l1 <= y and max(h0, h1) <= x or
    l0 + h1 <= y and max(h0, l1) <= x or
    max(l0, l1) <= x and h0+h1 <= y or
    max(l0, h1) <= x and h0+l1 <= y or
    max(l0, l1) <= y and h0+h1 <= x or
    max(l0, h1) <= y and h0+l1 <= x
    )

if condiction:
    print("S")
else:
    print("N")
