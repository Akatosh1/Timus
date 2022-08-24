import sys, math
people = 0
collaborators = []
counter = 0
for line in sys.stdin:
    parsed_line = line.split()
    if counter == 0:
        people = int(parsed_line[0])
    else:
        collaborators.append([])
        for m in parsed_line:
            if int(m) != 0:
                collaborators[counter-1].append(int(m))
    counter += 1
    if counter == (people+1):
        break

first_half = []
visited = []

def calculate():
    global collaborators
    global visited
    global first_half
    for peak in range(1, len(collaborators)+1):
        if peak not in visited:
            find_next(peak, 1)
    if len(visited) != people:
        print(0)
    else:
        print(len(first_half))
        string = ""
        for i in first_half:
            string += str(i) + " "
        print(string)


def find_next(peak, half):
    global collaborators
    global visited
    global first_half
    visited.append(peak)
    if half == 1:
        first_half.append(peak)
        half = 2
    else:
        half = 1
    for i in collaborators[peak-1]:
        if i not in visited:
            find_next(i, half)

calculate()