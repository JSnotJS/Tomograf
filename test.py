import scipy
import numpy as np


"""bychnięte z wikipedi tylko że C"""
def Bresenham(x1, y1, x2, y2):
    output_points = []
    # kierunki rysowaniaw
    xi = 1 if x1<x2 else -1
    dx = abs(x1-x2)

    yi = 1 if y1<y2 else -1
    dy = abs(y1-y2)

    x, y = x1, y1

    output_points.append((x,y))

    # oś wiodąca OX
    if dx > dy:
        ai = (dy - dx) * 2
        bi = dy * 2
        d = bi - dx
        # pętla po x-ach
        while x != x2:
            if d >= 0:
                x += xi
                y += yi
                d += ai
            else:
                d += bi
                x += xi
            output_points.append((x,y))
    else:
        ai = ( dx - dy ) * 2
        bi = dx * 2
        d = bi - dy
        # pętla po kolejnych y
        while y != y2:

            if d >= 0:
                x += xi
                y += yi
                d += ai
            else:
                d += bi
                y += yi
            output_points.append((x,y))
    return output_points


print(*Bresenham(1,1,7,4)[1])