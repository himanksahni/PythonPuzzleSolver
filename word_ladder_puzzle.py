from puzzle import Puzzle


class WordLadderPuzzle(Puzzle):
    """
    A word-ladder puzzle that may be solved, unsolved, or even unsolvable.
    """

    def __init__(self, from_word, to_word, ws):
        """
        Create a new word-ladder puzzle with the aim of stepping
        from from_word to to_word using words in ws, changing one
        character at each step.

        @type from_word: str
        @type to_word: str
        @type ws: set[str]
        @rtype: None
        """
        (self._from_word, self._to_word, self._word_set) = (from_word,
                                                            to_word, ws)
        # set of characters to use for 1-character changes
        self._chars = "abcdefghijklmnopqrstuvwxyz"

    def __eq__(self, other):
        """
        Return whether WordLadderPuzzle self is equivalent to other.

        @param other: WordLadderPuzzle
        @return: bool
        >>> words = open("words.txt","r")
        >>> Word_set = set(words.read().split())
        >>> Word1 = WordLadderPuzzle("sad","bad",Word_set)
        >>> Word2 = WordLadderPuzzle("sad","bad",Word_set)
        >>> Word1.__eq__(Word2)
        True
        """
        return (type(other) == type(self) and self._from_word == other._from_word
                and self._to_word == other._to_word and self._word_set == other._word_set)

    def __str__(self):
        """
        Return a human-readable string representation of WordLadderPuzzle self.

        >>> words = open("words.txt","r")
        >>> Word_set = set(words.read().split())
        >>> from_word = "sad"
        >>> to_word = "cat"
        >>> Word = WordLadderPuzzle(from_word,to_word,Word_set)
        >>> print(Word)
        sad --> cat
        """
        return (self._from_word + " --> " + self._to_word)

    def extensions(self):
        """
        Return a list of puzzle configurations from the current configuration.

        @type self: WordLadderPuzzle
        @rtype: list[WordLadderPuzzle]
        """
        from_word, to_word, ws, chars = self._from_word, self._to_word, self._word_set, self._chars
        ext_list = []
        for i in range(len(from_word)):
            for char in chars:
                new_word = ""
                if char != from_word[i]:
                    new_word += from_word[:i] + char + from_word[i+1:]
                    if new_word in ws:
                         ext_list.append(WordLadderPuzzle(new_word, to_word, ws))
        return ext_list

    def is_solved(self):
        """
        Return True if from_word equals to_word, False otherwise.

        @type self: WordLadderPuzzle
        @rtype: bool
        >>> words = open("words.txt", "r")
        >>> word_set = set(words.read().split())
        >>> from_word="dog"
        >>> to_word="cat"
        >>> w = WordLadderPuzzle(from_word,to_word,word_set)
        >>> w.is_solved()
        False
        >>> words = open("words.txt", "r")
        >>> word_set = set(words.read().split())
        >>> from_word="camel"
        >>> to_word="camel"
        >>> w = WordLadderPuzzle(from_word,to_word,word_set)
        >>> w.is_solved()
        True

        """
        if self._from_word == self._to_word:
            return True
        return False

#
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    with open("words.txt", "r") as words:
        word_set = set(words.read().split())
    w = WordLadderPuzzle("same", "cost", word_set)
    start = time()
    sol = breadth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using breadth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
    start = time()
    sol = depth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using depth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))



