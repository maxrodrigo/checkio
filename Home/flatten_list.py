#!/usr/bin/env checkio --domain=py run flatten-list
# https://py.checkio.org/mission/flatten-list/
#
# END_DESC
import re


# Classic solution
def flat_list_classic(array):
    result = []

    def flat(list):
        for i in list:
            if type(i) is int:
                result.append(i)
            else:
                flat(i)
        return result

    return flat(array)


# Creative solution
def flat_list(array):
    array = [int(c) for c in re.findall(r"-?\d+", str(array))]
    return array


if __name__ == "__main__":
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [
        2,
        4,
        5,
        6,
        6,
        6,
        6,
        6,
        7,
    ], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print("Done! Check it")
