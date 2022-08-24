import sys, math

pairs = []
first_half = 0
second_half = 0
collabs = 0
counter = 0
for line in sys.stdin:
    parsed_line = line.split()
    if counter == 0:
        first_half = int(parsed_line[0])
        second_half = int(parsed_line[1])
        collabs = int(parsed_line[2])
    else:
        pairs.append([])
        pairs[counter-1].append(parsed_line[0])
        pairs[counter-1].append(parsed_line[1])
    counter += 1
    if counter == (collabs+1):
        break
print(first_half)
print(second_half)
print(pairs)