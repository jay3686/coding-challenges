"""Print the spiral order of a matrix.

ex:
    [[1, 2, 3],
    [[4, 5, 6],
    [[7, 8, 9]]
    Should be this in spiral order:
    [1, 2, 3, 6 ,9, 8, 7, 4, 5]
"""


def spiral(a):
    """Return the spiral order of a 2d matrix."""
    l, r, u, d = 0, len(a) - 1, 0, len(a[0]) - 1
    ret = []
    while l <= r and u <= d:
        for i in xrange(l, r + 1):
            ret.append(a[u][i])
        u += 1
        for i in xrange(u, d + 1):
            ret.append(a[i][r])
        r -= 1
        for i in xrange(r, l - 1, -1):
            ret.append(a[d][i])
        d -= 1
        for i in xrange(d, u - 1, -1):
            ret.append(a[i][l])
        l += 1
    return ret


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print spiral(a)
