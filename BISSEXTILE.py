import sys

lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

for line in lines[1:]:
    if (int(line) % 4 == 0 and int(line) % 100 != 0) or (int(line) % 400 == 0):
        print("BISSEXTILE")
    else:
        print("NON BISSEXTILE")
#
# si (line est divisible par 4 mais non divisible par 100) OU si(line est divisible par 400) alors:
# afficher:BISSEXTILE
# sinon
# afficher:NON BISSEXTILE
#
# import sys
#
# lines = []
# for line in sys.stdin:
# 	lines.append(line.rstrip('\n'))
#
# for i, l in enumerate(lines):
# 	if i != 0:
# 		y = int(l)
# 		if y % 4 == 0 and y % 100 != 0:
# 			print("BISSEXTILE")
# 		elif y % 400 == 0:
# 			print("BISSEXTILE")
# 		else:
# 			print("NON BISSEXTILE")
#
#
