import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

affiche = int(lines[0])

for line in lines[2:]:
    affiche -= int(line)

print(affiche)

# autre version inline

print(int(lines[0]) - sum(int(line) for line in lines[2:]))

#
# x = int(input())
# n = int(input())
# for i in range(n):
#     x -= int(input())
# print(x)
#
