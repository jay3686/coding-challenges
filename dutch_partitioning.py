"""Rearrange an array such that elements < p are left of p.

Duplicates of p are consecutive and elements > p are right of p.
"""


def dutch(a, p):
    """Rearrange a s.t. a[i] < p is left of p and a[i] > p is right."""
    smallest, largest, i, j = 0, len(a) - 1, 0, len(a) - 1
    while i < j:
        if a[i] < p:
            a[smallest], a[i] = a[i], a[smallest]
            i += 1
            smallest += 1
        elif a[j] > p:
            a[largest], a[j] = a[j], a[largest]
            j -= 1
            largest -= 1
        elif a[i] > p:
            a[largest], a[i] = a[i], a[largest]
            largest -= 1
            j -= 1
        elif a[j] < p:
            a[smallest], a[j] = a[j], a[smallest]
            smallest += 1
            i += 1
        elif a[i] == p:
            i += 1
        else:
            j -= 1


def dutch2(a, p):
    """Rearrange a s.t. a[i] < p is left of p and a[i] > p is right."""
    smallest, i, j = 0, 0, len(a) - 1
    while i < j:
        if a[i] < p:
            a[smallest], a[i] = a[i], a[smallest]
            i += 1
            smallest += 1
        elif a[i] > p:
            a[j], a[i] = a[i], a[j]
            j -= 1
        elif a[i] == p:
            i += 1
    print smallest, j


a = [2, 4, 6, 0, 1, 4, 4, 4, 7, 8, 6]

print a
dutch(a, 4)
print a


a = [2, 4, 6, 0, 1, 4, 4, 4, 7, 8, 6]

print a
dutch2(a, 4)
print a
