### String permutaion

from collections import deque


def letterCombinationsUtil(number, n, table):
    list = []
    q = deque()
    q.append("")

    while len(q) != 0:
        s = q.pop()

        # if complete word is generated
        # push it in the list
        if len(s) == n:
            list.append(s)
        else:
            # Try all possible letters for current digit in number[]
            for letter in table[number[len(s)]]:
                q.append(s + letter)

    return list


# functions that creates the mapping and call letterCombinationUtil
def letterCombinations(number, n):
    # table[i] stores all characters that corresponds to ith digit in phone
    table = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    list = letterCombinationsUtil(number, n, table)

    s = ""
    for word in list:
        s += word + " "

    print(s)
    return


# Driver program
number = [2, 3]
n = len(number)

letterCombinations(number, n)
