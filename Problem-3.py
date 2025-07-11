n = int(input())

if n % 2 != 0:
    number_of_ele = n
else:
    number_of_ele = n - 1

l = []

for i in range(number_of_ele):
    odd_number = 2 * i + 1
    l.append(odd_number)

print(", ".join(str(i) for i in l))
