#!/usr/bin/python3
"""nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""

from sys import argv

if __name__ == "__main__":
    x = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    N = int(argv[1])
    if N < 4:
        print("N must be at least 4")
        exit(1)

    # initialize the answer list
    for i in range(N):
        x.append([i, None])

    def already_exists(y):
        """check that a queen does not already exist in that y value"""
        for x in range(N):
            if y == x[x][1]:
                return True
        return False

    def reject(x, y):
        """determines whether or not to reject the solution"""
        if (already_exists(y)):
            return False
        i = 0
        while (i < x):
            if abs(x[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(x):
        """clears the answers from the point of failure on"""

        for i in range(x, N):
            x[i][1] = None

    def nqueens(x):
        """recursive backtracking function to find the solution"""

        for y in range(N):
            clear_a(x)
            if reject(x, y):
                x[x][1] = y
                if (x == N - 1):
                    print(x)
                else:
                    nqueens(x + 1)

    nqueens(0)
