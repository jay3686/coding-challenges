"""Solution for the towers of hanoi problem.

Ex:

 1                               1
 2                               2
 3                               3
 4                               4
 5                               5
 6                               6
 7                               7
--- --- ---  should become  --- --- ---

Constraints:
3 Columns. Discs start on col 1 and must end up in col 2
Every element in a column must be smaller than the oens below it.
Only one item can be moved at a time
"""

import unittest


def hanoi(num_rings):
    """Pick a random element and partition around it to find kth."""
    def move_rings(nrings, col_a, col_b, col_c):
        pass

    cols = [range(num_rings)[::-1], [], []]

    return cols


def solution(num_rings):
    """Print steps for solving towers of hanoi.

    Params:
    arr:    num of rings to initialize with
    """
    # generate all primes up to A
    return hanoi()


class Tests(unittest.TestCase):
    """Test runner to prove solution works."""

    def test_base(self):
        """Unit tests."""
        self.assertEqual(solution(0), [[], [], []])
        self.assertEqual(solution(1), [[], [1], []])
        self.assertEqual(solution(2), [[], [1, 2], []])

    def test_normal(self):
        """Unit tests."""
        self.assertEqual(solution(7), None)

if __name__ == '__main__':
    unittest.main()
