#!/usr/bin/python3
""" Pascal triangle"""


def pascal_triangle(n):
    """triangle"""

    if n <= 0:
        return []
    triangle = [[] for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if (j < i):
                if (j == 0):
                    triangle[i].append(1)
                else:
                    triangle[i].append(triangle[i - 1][j] +
                                       triangle[i - 1][j - 1])
            elif (j == i):
                triangle[i].append(1)
    return triangle
