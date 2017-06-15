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
        if nrings <= 0:
            return
        # move from A to C, B is buffer
        move_rings(nrings - 1, col_a, col_c, col_b)

        cols[col_b].append(cols[col_a].pop())
        # print('Move from ', col_a, ' to ', col_b)

        # move from C to B, A is buffer
        move_rings(nrings - 1, col_c, col_b, col_a)

    cols = [range(num_rings)[::-1], [], []]

    move_rings(num_rings, 0, 1, 2)
    return cols


def solution(num_rings):
    """Print steps for solving towers of hanoi.

    Params:
    arr:    num of rings to initialize with
    """
    return hanoi(num_rings)


class Tests(unittest.TestCase):
    """Test runner to prove solution works."""

    def test_base(self):
        """Unit tests."""
        self.assertEqual(solution(0), [[], [], []])
        self.assertEqual(solution(1), [[], [0], []])
        self.assertEqual(solution(2), [[], [1, 0], []])

    def test_normal(self):
        """Unit tests."""
        for i in range(3, 10):
            cols = [[], range(i)[::-1], []]
            self.assertEqual(solution(i), cols)

if __name__ == '__main__':
    unittest.main()
