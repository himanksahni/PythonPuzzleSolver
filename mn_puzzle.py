from puzzle import Puzzle


class MNPuzzle(Puzzle):
    """
    An nxm puzzle, like the 15-puzzle, which may be solved, unsolved,
    or even unsolvable.
    """

    def __init__(self, from_grid, to_grid):
        """
        MNPuzzle in state from_grid, working towards
        state to_grid

        @param MNPuzzle self: this MNPuzzle
        @param tuple[tuple[str]] from_grid: current configuration
        @param tuple[tuple[str]] to_grid: solution configuration
        @rtype: None
        """
        # represent grid symbols with letters or numerals
        # represent the empty space with a "*"
        assert len(from_grid) > 0
        assert all([len(r) == len(from_grid[0]) for r in from_grid])
        assert all([len(r) == len(to_grid[0]) for r in to_grid])
        self.n, self.m = len(from_grid), len(from_grid[0])
        self.from_grid, self.to_grid = from_grid, to_grid

    def __eq__(self, other):
        """

        Return True if self equals other, False otherwise.

        @type self: MNPuzzle
        @type other: MNPuzzle
        @rtype: bool
        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid = (("*", "2", "3"), ("1", "4", "5"))
        >>> MN1 = MNPuzzle(start_grid, target_grid)
        >>> MN2 = MNPuzzle(target_grid, start_grid)
        >>> MN1 == MN2
        False
        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid = (("*", "2", "3"), ("1", "4", "5"))
        >>> MN1 = MNPuzzle(start_grid, target_grid)
        >>> MN2 = MNPuzzle(start_grid, target_grid)
        >>> MN1 == MN2
        True
        """

        return (self.from_grid == other.from_grid and self.to_grid == other.to_grid)

    def __str__(self):

        """
        Return a human-readable string representation of the current Puzzle configuration
        @type self: MNPuzzle
        @rtype: str

        Example:
        target_grid = (("1", "2", "3"), ("4", "5", "*"))
        start_grid = (("*", "2", "3"), ("1", "4", "5"))
        w = MNPuzzle(start_grid, target_grid)
        print(w)

        Output:
            * 2 3
            1 4 5

              to

            1 2 3
            4 5 *
        """
        from_grid = ""
        to_grid = ""
        for row in self.from_grid:
            for pieces in row:
                from_grid += pieces + " "
            from_grid += "\n"
        from_grid = from_grid[:-1]

        for rows in self.to_grid:
            for piece in rows:
                to_grid += piece + " "
            to_grid += "\n"
        to_grid = to_grid[:-1]

        return (from_grid + "\n" + "\n" + "  " + "to" + "\n" +"\n" + to_grid)

    def extensions(self):
        """
        Return a list of extensions from the current Puzzle configuration

        @type self: MNPuzzle
        @rtype: list[MNPuzzle]
        """

        start_tuple, target_tuple = self.from_grid, self.to_grid
        row = len(start_tuple)-1
        col = len(start_tuple[0])-1
        ext_list = []

        if self.is_solved():
            return ext_list
        for y in range(len(start_tuple)):
            for x in range(len(start_tuple[0])):
                if start_tuple[y][x] == "*":

                    # right
                    if (x+1) <= col:
                        new_tuple = start_tuple
                        new_tuple = list(new_tuple)
                        new_tuple[y] = list(new_tuple[y])
                        new_tuple[y][x], new_tuple[y][x+1] = new_tuple[y][x+1], "*"
                        new_tuple[y] = tuple(new_tuple[y])
                        new_tuple = tuple(new_tuple)
                        ext_list.append(MNPuzzle(new_tuple,target_tuple))
                    # left
                    if (x-1) >= 0:
                        new_tuple = start_tuple
                        new_tuple = list(new_tuple)
                        new_tuple[y] = list(new_tuple[y])
                        new_tuple[y][x], new_tuple[y][x-1] = new_tuple[y][x-1], "*"
                        new_tuple[y] = tuple(new_tuple[y])
                        new_tuple = tuple(new_tuple)
                        ext_list.append(MNPuzzle(new_tuple,target_tuple))
                    # top
                    if (y-1) >= 0:
                        new_tuple = start_tuple
                        new_tuple = list(new_tuple)
                        new_tuple[y] = list(new_tuple[y])
                        new_tuple[y-1] = list(new_tuple[y-1])
                        new_tuple[y][x], new_tuple[y-1][x] = new_tuple[y-1][x], "*"
                        new_tuple[y-1] = tuple(new_tuple[y-1])
                        new_tuple[y] = tuple(new_tuple[y])
                        new_tuple = tuple(new_tuple)
                        ext_list.append(MNPuzzle(new_tuple,target_tuple))
                    # bottom
                    if (y+1) <= row:
                        new_tuple = start_tuple
                        new_tuple = list(new_tuple)
                        new_tuple[y] = list(new_tuple[y])
                        new_tuple[y+1] = list(new_tuple[y+1])
                        new_tuple[y][x], new_tuple[y+1][x] = new_tuple[y+1][x], "*"
                        new_tuple[y+1] = tuple(new_tuple[y+1])
                        new_tuple[y] = tuple(new_tuple[y])
                        new_tuple = tuple(new_tuple)
                        ext_list.append(MNPuzzle(new_tuple,target_tuple))
        return ext_list

    def is_solved(self):

        """
        Return True if the current Puzzle configuration is solved, False otherwise.

        @type self:MNPuzzle
        @rtype:bool

        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid = (("*", "2", "3"), ("1", "4", "5"))
        >>> w = MNPuzzle(start_grid, target_grid)
        >>> w.is_solved()
        False
        >>> target_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> start_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> w = MNPuzzle(start_grid, target_grid)
        >>> w.is_solved()
        True
        """

        if self.from_grid == self.to_grid:
            return True
        return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    target_grid = (("1", "2", "3"), ("4", "5", "*"))
    start_grid = (("*", "2", "3"), ("1", "4", "5"))
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    start = time()
    solution = breadth_first_solve(MNPuzzle(start_grid, target_grid))
    end = time()
    print("BFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
    start = time()
    solution = depth_first_solve((MNPuzzle(start_grid, target_grid)))
    end = time()
    print("DFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))




