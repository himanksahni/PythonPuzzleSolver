# """
# Some functions for working with puzzles
# """
# from puzzle import Puzzle
# from collections import deque
# # set higher recursion limit
# # which is needed in PuzzleNode.__str__
# # uncomment the next two lines on a unix platform, say CDF
# # import resource
# # resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
# import sys
# sys.setrecursionlimit(10**6)
#
#
# def depth_first_solve(puzzle):
#     """
#     Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
#     a solution, with each child containing an extension of the puzzle
#     in its parent.  Return None if this is not possible.
#
#     @type puzzle: Puzzle
#     @rtype: PuzzleNode
#
#     """
#     if puzzle.is_solved():
#         return PuzzleNode(puzzle)
#
#     else:
#         list_of_ext = puzzle.extensions()
#         lst = []
#         for puzzles in list_of_ext:
#             if puzzles not in lst:
#                 lst.append(puzzles)
#                 node = solve(puzzles, lst, puzzle)
#
#                 if node is not None:
#                     head = PuzzleNode(puzzle, [node], None)
#                     return head
#
#
# def solve(puzzle, l, parent=None):
#     """
#     Return the child PuzzleNode
#     @type puzzle: Puzzle
#     @type l: list
#     @type parent: PuzzleNode
#     @rtype: PuzzleNode
#     """
#     if puzzle.is_solved():
#         return PuzzleNode(puzzle, [], parent)
#
#     elif puzzle.fail_fast():
#         return None
#
#     else:
#         lst_of_ext = puzzle.extensions()
#
#         for puzzles in lst_of_ext:
#
#             if puzzles not in l:
#                 l.append(puzzles)
#                 nodes = solve(puzzles, l, puzzle)
#
#                 if nodes is not None:
#                     head = PuzzleNode(puzzle, [nodes], parent)
#                     nodes.parent = head
#                     return head
#         return None
#
#
# def breadth_first_solve(puzzle):
#     """
#     Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
#     a solution, with each child PuzzleNode containing an extension
#     of the puzzle in its parent.  Return None if this is not possible.
#
#     @type puzzle: Puzzle
#     @rtype: PuzzleNode
#
#     """
#     if puzzle.is_solved():
#         return PuzzleNode(puzzle)
#
#     else:
#         list_of_ext = puzzle.extensions()
#         visited = []
#         if puzzle not in visited:
#             visited.append(puzzle)
#
#         queue = deque()
#         for puzzles in list_of_ext:
#             queue.append(PuzzleNode(puzzles, None, PuzzleNode(puzzles)))
#
#         if queue:
#                 pop_left_ext = queue.popleft()
#                 ext_puzzle = pop_left_ext.puzzle
#                 ext_parent = pop_left_ext.parent.puzzle
#
#                 if pop_left_ext not in visited:
#                     visited.append(pop_left_ext)
#                     node = solve2(ext_puzzle, visited, queue, ext_parent)
#                     if node is not None:
#                         head = PuzzleNode(puzzle,[node],None)
#                         return head
#
# # Helper ftn for breadth
# def solve2(puzzle, visited, queue, parent=None):
#
#         """
#         Return the child PuzzleNode
#         Returns a child PuzzleNode
#         @type puzzle: Puzzle
#         @type visited: list
#         @type queue: deque
#         @type parent: PuzzleNode
#         @rtype: PuzzleNode
#         """
#         if puzzle.is_solved():
#             return PuzzleNode(puzzle, [], parent)
#
#         else:
#             lst_of_ext = puzzle.extensions()
#             puzzle.children=lst_of_ext
#
#             for ext in lst_of_ext:
#                 queue.append(PuzzleNode(ext, None, PuzzleNode(puzzle)))
#
#             while True:
#                 pop_left_ext = queue.popleft()
#                 ext_puzzle = pop_left_ext.puzzle
#                 ext_parent = pop_left_ext.parent.puzzle
#
#                 if pop_left_ext not in visited:
#                     visited.append(pop_left_ext)
#                     node = solve2(ext_puzzle, visited, queue, ext_parent)
#                     if node is not None:
#                         head = PuzzleNode(puzzle, [node], None)
#                         return head
#
#
# # Class PuzzleNode helps build trees of PuzzleNodes that have
# # an arbitrary number of children, and a parent.
# class PuzzleNode:
#     """
#     A Puzzle configuration that refers to other configurations that it
#     can be extended to.
#     """
#
#     def __init__(self, puzzle=None, children=None, parent=None):
#         """
#         Create a new puzzle node self with configuration puzzle.
#
#         @type self: PuzzleNode
#         @type puzzle: Puzzle | None
#         @type children: list[PuzzleNode]
#         @type parent: PuzzleNode | None
#         @rtype: None
#         """
#         self.puzzle, self.parent = puzzle, parent
#         if children is None:
#             self.children = []
#         else:
#             self.children = children[:]
#
#     def __eq__(self, other):
#         """
#         Return whether PuzzleNode self is equivalent to other
#
#         @type self: PuzzleNode
#         @type other: PuzzleNode | Any
#         @rtype: bool
#
#         >>> from word_ladder_puzzle import WordLadderPuzzle
#         >>> pn1 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "no", "oo"}))
#         >>> pn2 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "oo", "no"}))
#         >>> pn3 = PuzzleNode(WordLadderPuzzle("no", "on", {"on", "no", "oo"}))
#         >>> pn1.__eq__(pn2)
#         True
#         >>> pn1.__eq__(pn3)
#         False
#         """
#         return (type(self) == type(other) and
#                 self.puzzle == other.puzzle and
#                 all([x in self.children for x in other.children]) and
#                 all([x in other.children for x in self.children]))
#
#     def __str__(self):
#         """
#         Return a human-readable string representing PuzzleNode self.
#
#         # doctest not feasible.
#         """
#         return "{}\n\n{}".format(self.puzzle,
#                                  "\n".join([str(x) for x in self.children]))




"""
Some functions for working with puzzles
"""
from puzzle import Puzzle
from collections import deque
# set higher recursion limit
# which is needed in PuzzleNode.__str__
# uncomment the next two lines on a unix platform, say CDF
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
import sys
sys.setrecursionlimit(10**6)


def depth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child containing an extension of the puzzle
    in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode

    """
    if puzzle.is_solved():
        return PuzzleNode(puzzle)

    else:
        list_of_ext = puzzle.extensions()
        visited = []
        for puzzles in list_of_ext:
            if puzzles not in visited:
                visited.append(puzzles)
                node = solve(puzzles,visited, PuzzleNode(puzzle))

                if node is not None:
                    head = PuzzleNode(puzzle, [node], None)
                    return head


def solve(puzzle,visited, parent=None):
    """
    Return the child PuzzleNode
    @type puzzle: Puzzle
    @type l: list
    @type parent: PuzzleNode
    @rtype: PuzzleNode
    """
    if puzzle.is_solved():
        return PuzzleNode(puzzle, [], parent)

    elif puzzle.fail_fast():
        return None

    else:
        lst_of_ext = puzzle.extensions()

        for puzzles in lst_of_ext:

            if puzzles not in visited:
                visited.append(puzzles)
                nodes = solve(puzzles,visited, PuzzleNode(puzzle))

                if nodes is not None:
                    head = PuzzleNode(puzzle, [nodes], parent)
                    nodes.parent = head
                    return head
        return None


def breadth_first_solve(puzzle):
    """
    Return a path from PuzzleNode(puzzle) to a PuzzleNode containing
    a solution, with each child PuzzleNode containing an extension
    of the puzzle in its parent.  Return None if this is not possible.

    @type puzzle: Puzzle
    @rtype: PuzzleNode

    """
    if puzzle.is_solved():
        return PuzzleNode(puzzle)

    else:
        list_of_ext = puzzle.extensions()
        visited = []
        if puzzle not in visited:
            visited.append(puzzle)

        queue = deque()
        for puzzles in list_of_ext:
            queue.append(PuzzleNode(puzzles, None, PuzzleNode(puzzles)))

        if queue:
                pop_left_ext = queue.popleft()
                ext_puzzle = pop_left_ext.puzzle
                ext_parent = pop_left_ext.parent.puzzle

                if pop_left_ext not in visited:
                    visited.append(pop_left_ext)
                    node = solve2(ext_puzzle, visited, queue, ext_parent)
                    if node is not None:
                        head = PuzzleNode(puzzle,[node],None)
                        return head

# Helper ftn for breadth
def solve2(puzzle, visited, queue, parent=None):

        """
        Return the child PuzzleNode
        Returns a child PuzzleNode
        @type puzzle: Puzzle
        @type visited: list
        @type queue: deque
        @type parent: PuzzleNode
        @rtype: PuzzleNode
        """
        if puzzle.is_solved():
            return PuzzleNode(puzzle, [], parent)

        else:
            lst_of_ext = puzzle.extensions()
            puzzle.children=lst_of_ext

            for ext in lst_of_ext:
                queue.append(PuzzleNode(ext, None, PuzzleNode(puzzle)))

            while True:
                pop_left_ext = queue.popleft()
                ext_puzzle = pop_left_ext.puzzle
                ext_parent = pop_left_ext.parent.puzzle

                if pop_left_ext not in visited:
                    visited.append(pop_left_ext)
                    node = solve2(ext_puzzle, visited, queue, ext_parent)
                    if node is not None:
                        head = PuzzleNode(puzzle, [node], None)
                        return head


# Class PuzzleNode helps build trees of PuzzleNodes that have
# an arbitrary number of children, and a parent.
class PuzzleNode:
    """
    A Puzzle configuration that refers to other configurations that it
    can be extended to.
    """

    def __init__(self, puzzle=None, children=None, parent=None):
        """
        Create a new puzzle node self with configuration puzzle.

        @type self: PuzzleNode
        @type puzzle: Puzzle | None
        @type children: list[PuzzleNode]
        @type parent: PuzzleNode | None
        @rtype: None
        """
        self.puzzle, self.parent = puzzle, parent
        if children is None:
            self.children = []
        else:
            self.children = children[:]

    def __eq__(self, other):
        """
        Return whether PuzzleNode self is equivalent to other

        @type self: PuzzleNode
        @type other: PuzzleNode | Any
        @rtype: bool

        >>> from word_ladder_puzzle import WordLadderPuzzle
        >>> pn1 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "no", "oo"}))
        >>> pn2 = PuzzleNode(WordLadderPuzzle("on", "no", {"on", "oo", "no"}))
        >>> pn3 = PuzzleNode(WordLadderPuzzle("no", "on", {"on", "no", "oo"}))
        >>> pn1.__eq__(pn2)
        True
        >>> pn1.__eq__(pn3)
        False
        """
        return (type(self) == type(other) and
                self.puzzle == other.puzzle and
                all([x in self.children for x in other.children]) and
                all([x in other.children for x in self.children]))

    def __str__(self):
        """
        Return a human-readable string representing PuzzleNode self.

        # doctest not feasible.
        """
        return "{}\n\n{}".format(self.puzzle,
                                 "\n".join([str(x) for x in self.children]))