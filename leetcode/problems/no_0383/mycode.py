"""383. Ransom Note

URL: https://leetcode.com/problems/ransom-note/

## Description

Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.
Each letter in `magazine` can only be used once in `ransomNote`.

difficulty: Easy
"""

from collections import Counter
from typing import Dict, List, Union


# my code.
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_ransome_note = Counter(ransomNote)
        counter_magazine = Counter(magazine)
        return all(
            [
                counter_magazine[character] >= counter_ransome_note[character]
                for character in set(counter_ransome_note.elements())
            ]
        )


class SolutionModelAnswer:
    """
    {URL}
    """

    pass


class SolutionExampleAnswer01:
    """
    https://leetcode.com/problems/ransom-note/solutions/294576/easy-understand-python-solution/?languageTags=python3
    """

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_ransome_note = Counter(ransomNote)
        counter_magazine = Counter(magazine)
        return list(counter_ransome_note - counter_magazine) == []


if __name__ == "__main__":
    import pkg_resources

    if any([str(i).startswith("icecream") for i in pkg_resources.working_set]):
        import icecream

        _debug = icecream.ic
    else:
        _debug = print

    global debug
    debug = _debug

    debug(Counter("abcabc"))  # ic| Counter("abcabc"): Counter({'a': 2, 'b': 2, 'c': 2})
    debug(Counter("abcabc")["a"])  # ic| Counter("abcabc")["a"]: 2
    debug(len(Counter("abcabc")))  # ic| len(Counter("abcabc")): 3
    debug(
        list(Counter("abcabc").elements())
    )  # ic| list(Counter("abcabc").elements()): ['a', 'a', 'b', 'b', 'c', 'c']
    debug(
        set(Counter("abcabc").elements())
    )  # ic| set(Counter("abcabc").elements()): {'c', 'a', 'b'}
    debug(
        Counter("abcabc").items()
    )  # ic| Counter("abcabc").items(): dict_items([('a', 2), ('b', 2), ('c', 2)])
    debug(
        [(c, v) for c, v in Counter("abcabc").items()]
    )  # [('a', 2), ('b', 2), ('c', 2)]
