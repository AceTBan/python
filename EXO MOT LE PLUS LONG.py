import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

maxi = 1

for line in lines[1:]:
    if len(line) > maxi:
        maxi = len(line)

print(maxi)

# autre version inline

print(max(len(x) for x in lines[1:]))
#
# N = int(input())
# l = []
# for _ in range(N):
#     l.append(len(input()))
# print(max(l))
#

