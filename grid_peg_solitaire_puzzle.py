from puzzle import Puzzle


class GridPegSolitairePuzzle(Puzzle):
    """
    Snapshot of peg solitaire on a rectangular grid. May be solved,
    unsolved, or even unsolvable.
    """

    def __init__(self, marker, marker_set):
        """
        Create a new GridPegSolitairePuzzle self with
        marker indicating pegs, spaces, and unused
        and marker_set indicating allowed markers.

        @type marker: list[list[str]]
        @type marker_set: set[str]
                          "#" for unused, "*" for peg, "." for empty
        """
        assert isinstance(marker, list)
        assert len(marker) > 0
        assert all([len(x) == len(marker[0]) for x in marker[1:]])
        assert all([all(x in marker_set for x in row) for row in marker])
        assert all([x == "*" or x == "." or x == "#" for x in marker_set])
        self._marker, self._marker_set = marker, marker_set

    def __eq__(self, other):
        """
        Return whether GridPegSoltairePuzzle self is equivalent to other.
        @type self: GridPegSolitairePuzzle
        @type other: GridPegSolitairePuzzle | Any
        @rtype: bool
        >>> grid = [["*", "*", "*", "*", "*"]]
        >>> grid+= [["*", "*", "*", "*", "*"]]
        >>> grid+= [["*", "*", "*", "*", "*"]]
        >>> grid+= [["*", "*", ".", "*", "*"]]
        >>> grid+= [["*", "*", "*", "*", "*"]]
        >>> s=GridPegSolitairePuzzle(grid,{"#","*","."})
        >>> prid = [[".", ".", ".", ".", "."]]
        >>> prid+= [[".", ".", ".", ".", "."]]
        >>> prid+= [[".", ".", ".", ".", "."]]
        >>> prid+= [[".", ".", "*", ".", "."]]
        >>> prid+= [[".", ".", ".", ".", "."]]
        >>> r=GridPegSolitairePuzzle(prid,{"#","*","."})
        >>> s == r
        False
        >>> grid = [["*", "*", "*", "*", "*"]]
        >>> grid+= [["*", "*", "*", "*", "*"]]
        >>> grid+= [["*", "*", "*", "*", "*"]]
        >>> grid+= [["*", "*", ".", "*", "*"]]
        >>> grid+= [["*", "*", "*", "*", "*"]]
        >>> sp = GridPegSolitairePuzzle(grid,{"#","*","."})
        >>> prid = [["*", "*", "*", "*", "*"]]
        >>> prid+= [["*", "*", "*", "*", "*"]]
        >>> prid+= [["*", "*", "*", "*", "*"]]
        >>> prid+= [["*", "*", ".", "*", "*"]]
        >>> prid+= [["*", "*", "*", "*", "*"]]
        >>> sr = GridPegSolitairePuzzle(prid,{"#","*","."})
        >>> sp == sr
        True

        """
        return (type(other) == type(self) and
                self._marker == other._marker and self._marker_set == other._marker_set)

    def __str__(self):

        """
        Return a human-readable string representation of GridPegSoltairePuzzle self.

        >>> grid = [["*", "*", "*", "*", "*"]]
        >>> grid+= [["*", "*", "*", "*", "*"]]
        >>> grid+= [["*", "*", "*", "*", "*"]]
        >>> grid+= [["*", "*", ".", "*", "*"]]
        >>> grid+= [["*", "*", "*", "*", "*"]]
        >>> s=GridPegSolitairePuzzle(grid,{"#","*","."})
        >>> print(s)
        * * * * *
        * * * * *
        * * * * *
        * * . * *
        * * * * *
        >>> prid = [[".", ".", ".", ".", "."]]
        >>> prid+= [[".", ".", ".", ".", "."]]
        >>> prid+= [[".", ".", ".", ".", "."]]
        >>> prid+= [[".", ".", "*", ".", "."]]
        >>> prid+= [[".", ".", ".", ".", "."]]
        >>> r=GridPegSolitairePuzzle(prid,{"#","*","."})
        >>> print(r)
        . . . . .
        . . . . .
        . . . . .
        . . * . .
        . . . . .

        """
        rep = ""
        for row in self._marker:
            for pegs in row:
                rep += pegs + " "
            rep = rep[:-1]
            rep += "\n"
        rep = rep[:-1]
        return rep

    def extensions(self):
        """
        Return a list of puzzle configurations from the current puzzle configuration.

        @type self: GridPegSolitairePuzzle
        @rtype: list[GridPegSolitairePuzzle]

        >>> grid = [["*","*","*","*","*"]]
        >>> grid += [["*","*","*","*","*"]]
        >>> grid += [["*","*",".","*","*"]]
        >>> grid += [["*","*","*","*","*"]]
        >>> grid += [["*","*","*","*","*"]]
        >>> peg = GridPegSolitairePuzzle(grid,{"#",".","*"})
        >>> list = list(peg.extensions())
        >>> print(len(list))
        4
        """
        marker, marker_set = self._marker, self._marker_set
        row = len(marker)-1
        column = len(marker[0])-1
        ext_list = []

        if self.is_solved():
            return ext_list

        else:
            for y in range(len(marker)):
                for x in range(len(marker[y])):
                    new_marker = [x[:] for x in marker]
                    if marker[y][x] == '*':

                        # check up
                        if (y-2) >= 0 and marker[y-1][x] == '*' and marker[y-2][x] == '.':
                                new_marker[y][x], new_marker[y-1][x], new_marker[y-2][x] = '.', '.', '*'
                                ext_list.append(GridPegSolitairePuzzle(new_marker, marker_set))
                        # check down
                        elif (y+2) <= row and marker[y+1][x] == '*' and marker[y+2][x] == '.':
                                new_marker[y][x], new_marker[y+1][x], new_marker[y+2][x] = '.', '.', '*'
                                ext_list.append(GridPegSolitairePuzzle(new_marker, marker_set))
                        # check left
                        elif (x-2) >= 0 and marker[y][x-1] == '*' and marker[y][x-2] == '.':
                                new_marker[y][x], new_marker[y][x-1], new_marker[y][x-2] = '.', '.', '*'
                                ext_list.append(GridPegSolitairePuzzle(new_marker, marker_set))
                        # check right
                        elif (x+2) <= column and marker[y][x+1] == '*' and marker[y][x+2] == '.':
                                new_marker[y][x], new_marker[y][x+1], new_marker[y][x+2] = '.', '.', '*'
                                ext_list.append(GridPegSolitairePuzzle(new_marker, marker_set))
            return ext_list

    def is_solved(self):

        """
        Return True if the current Puzzle configuration is solved, False otherwise.

        @type self: SudokuPuzzle
        @rtype: bool

        >>> grid = [["*", "*", "*", "*", "*"]]
        >>> grid+= [["*", "*", "*", "*", "*"]]
        >>> grid+= [["*", "*", "*", "*", "*"]]
        >>> grid+= [["*", "*", ".", "*", "*"]]
        >>> grid+= [["*", "*", "*", "*", "*"]]
        >>> s=GridPegSolitairePuzzle(grid,{"#","*","."})
        >>> s.is_solved()
        False
        >>> prid = [[".", ".", ".", ".", "."]]
        >>> prid+= [[".", ".", ".", ".", "."]]
        >>> prid+= [[".", ".", ".", ".", "."]]
        >>> prid+= [[".", ".", "*", ".", "."]]
        >>> prid+= [[".", ".", ".", ".", "."]]
        >>> r=GridPegSolitairePuzzle(prid,{"#","*","."})
        >>> r.is_solved()
        True
        """
        marker = self._marker

        count = 0
        for row in marker:
            for piece in row:
                if piece == "*":
                    count += 1
        if count == 1:
            return True
        else:
            return False

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    from puzzle_tools import depth_first_solve

    grid = [["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", ".", "*", "*"],
            ["*", "*", "*", "*", "*"]]
    gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
    gpsp.extensions()
    import time

    start = time.time()
    solution = depth_first_solve(gpsp)
    end = time.time()
    print("Solved 5x5 peg solitaire in {} seconds.".format(end - start))
    print("Using depth-first: \n{}".format(solution))
