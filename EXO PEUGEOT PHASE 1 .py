import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

print(lines)

total = 0
nb_jours = int(lines[0])

for prod in range(1, nb_jours):
    a = int(lines[prod])
    total = total + a

# autre methode
for prod in lines[1:]:
    total = total + int(prod)

print(total)

# autre methode
print(sum(int(prod) for prod in lines[1:]))


# import sys
#
# n = int(input())
# print(sum(int(input()) for _ in range(n)))

