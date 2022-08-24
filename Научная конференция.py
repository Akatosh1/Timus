import sys, math
kolvo_dokladov = 0
dokladi = []
amount = 0
counter = 0
for line in sys.stdin:
    parsed_line = line.split()
    if counter == 0:
        kolvo_dokladov = int(parsed_line[0])
    else:
        dokladi.append([])
        dokladi[counter-1].append(parsed_line[0])
        dokladi[counter-1].append(parsed_line[1])
    counter += 1
    if counter == (kolvo_dokladov+1):
        break

def sort_by_me(input):
    return int(input[0]) * 1000 + int(input[1])

dokladi.sort()
dokladi.sort(key=sort_by_me)
dokladi.reverse()
flag = 100000
for i in dokladi:
    if(int(i[1])<flag):
        amount += 1
        flag = int(i[0])
print(amount)