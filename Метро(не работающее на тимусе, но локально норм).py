import sys, math
width = 0
height = 0
counter = 0
canGoStraight = 0
start = (1, 1)
canGoStraightCoordinates = []
bestLength = -1
for line in sys.stdin:
    parsedLine = line.split()
    if counter == 0:
        width = int(parsedLine[0])
        height = int(parsedLine[1])
    elif counter == 1:
        canGoStraight = int(parsedLine[0])
    else:
        coord = (int(parsedLine[0]), int(parsedLine[1]))
        canGoStraightCoordinates.append(coord)
    counter += 1
    if(counter == canGoStraight + 2 and counter != 1):
        break

end = (start[0] + width, start[1] + height)



def next(length, currentWidth, currentHeight, canGoStraight):
    global width
    global height
    global start
    global end
    global bestLength
    if(length >= bestLength & bestLength != -1):
        return
    currentCoordinate = (currentWidth, currentHeight)
    if(currentCoordinate == end):
        if(length < bestLength or bestLength == -1):
            bestLength = round(length)
            return
    elif(canGoStraight == 0):
        bestLength = 100 * (end[0] - currentWidth) + 100 * (end[1] - currentHeight) + length
    elif(currentCoordinate in canGoStraightCoordinates):
        next(length + math.sqrt(20000), currentWidth + 1, currentHeight + 1, canGoStraight-1)
    elif(currentWidth == end[0]):
        curr = round(length + (100 * (end[1] - currentHeight)))
        if(curr < bestLength or bestLength == -1):
            bestLength = curr
    elif(currentHeight == end[1]):
        curr = round(length + (100 * (end[0] - currentWidth)))
        if(curr < bestLength or bestLength == -1):
            bestLength = curr
    else:
        next(length + 100, currentWidth + 1, currentHeight, canGoStraight)
        next(length + 100, currentWidth, currentHeight + 1, canGoStraight)

next(0, 1, 1, canGoStraight)
print(bestLength)