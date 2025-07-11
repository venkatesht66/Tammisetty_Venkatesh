n = int(input())

l = []
for i in range(n):
    l.append(2 * i + 1)

print(", ".join(map(str, l)))
