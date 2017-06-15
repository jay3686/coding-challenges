"""Solution for the N queens problem.

Ex:

For N = 4, two solutions:

    *Q**    **Q*
    ***Q    Q***
    Q***    ***Q
    **Q*    *Q**

Constraints:
N queens must be placed on an N x N board.
They should not be able to attack each other horizontally, verticlaly
or diagonally.

"""

import unittest


def nqueens(n):
    """Return list of Unique Queen placements."""
    def solve(row, cols):
        if row >= n:
            res.append(cols)
            return
        for col in range(n):
            # check diagonal (abs(Ai - Aj) == abs(Bi - Bj))
            for i, c in enumerate(cols):
                if col == c or abs(col - c) == row - i:
                    break
            else:
                solve(row + 1, cols + [col])

    res = []
    solve(0, [])
    return res


def solution(n):
    """Return list of Unique Queen placements.

    Params:
    n:    num of queens and size of board
    """
    return nqueens(n)


class Tests(unittest.TestCase):
    """Test runner to prove solution works."""

    def test_base(self):
        """Unit tests."""
        self.assertEqual(solution(0), [[]])
        self.assertEqual(solution(1), [[0]])
        self.assertEqual(solution(4), [[1, 3, 0, 2], [2, 0, 3, 1]])

    # def test_normal(self):
    #     """Unit tests."""
    #     for i in range(3, 10):
    #         expected = []
    #         self.assertEqual(solution(i), expected)

if __name__ == '__main__':
    unittest.main()
