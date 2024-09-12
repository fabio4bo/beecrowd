"""
BEE 1247 - Coast Guard - Level 2 - Mathematics
"""

import math

while True:
    try:
        D, VF, VG = map(int, input().split())

        G_to_limite = math.hypot(D, 12) # or math.sqrt(D ** 2 + 144)

        G_time_to_limite = G_to_limite / VG
        F_time_to_limite = 12 / VF

        if G_time_to_limite <= F_time_to_limite:
            print("S")
        else:
            print("N") 
    except EOFError:  # eof
        break