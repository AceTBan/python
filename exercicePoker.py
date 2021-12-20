import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

total = int(lines[0])

for line in lines[2:]:
    element = line.split(" ")
    mise = int(element[0])
    gain = int(element[1])
    total = total - mise + gain

    # autre version
    elem = line.split()
    total = total - int(elem[0]) + int(elem[1])

    # autre version
    total = total - int(line.split()[0]) + int(line.split()[1])

print(total)