
from collections import Counter


def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = Counter()
    for c in str1:
        counter[c] += 1
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1

    return len([x for x in counter if counter[x] != 0]) == 0

if __name__ == "__main__":
    assert(check_permutation("abc", "cba") == True)
    assert(check_permutation("abc", "cbd") == False)