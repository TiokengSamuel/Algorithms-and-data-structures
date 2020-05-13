def mult(n):
    return n * n


list = [1, 2, 3, 4, 5]

map = map(mult, list)

print(next(map))
print(next(map))
print(next(map))

print(*map)
