#!/usr/bin/python3
"""triangle prints"""


def pascal_triangle(n):
    """return n's triangle"""
    if n <= 0:
        return []
    tri = [[1]]
    for i in range(1, n):
        prev = tri[i - 1]
        new = [1]
        for j in range(len(prev) - 1):
            new.append(prev[j] + prev[j + 1])

        new.append(1)
        tri.append(new)

    return tri
