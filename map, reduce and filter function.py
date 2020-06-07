from functools import reduce

num = [3, 2, 6, 8, 4, 6, 2, 9]

evens = list(filter(lambda n: n % 2 == 0, num))

doubles = list(map(lambda n: n * 2, evens))

sum = reduce(lambda a, b: a + b, doubles)

print(sum)
