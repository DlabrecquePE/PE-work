fibolist = [1, 2]
max_value = 4 * 10 ** 6

current = sum(fibolist[-2:])
while current < max_value:
    fibolist.append(current)
    current = sum(fibolist[-2:])

print(sum([x for x in fibolist if not x % 2]))
