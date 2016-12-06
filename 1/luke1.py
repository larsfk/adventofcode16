import math

coordinates = [(0,0)]

currentx = 0
currenty = 0

facing = 0 # N, E, S, W => 0, 1, 2, 3


def find_path(dir):
    global facing, currentx, currenty
    steps = int(dir[1:])

    if dir[0] == "R":
        facing = ((facing + 1 + 4) % 4)
    else:
        facing = ((facing - 1 + 4) % 4)

    add_step = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in xrange(steps):
        currentx += add_step[facing][0]
        currenty += add_step[facing][1]
        if (currentx, currenty) not in coordinates:
            coordinates.append((currentx,currenty))
        else:
            print "Twice:", abs(currentx) + abs(currenty)

    
def main():
    map = []
    file = open("input.py","r")
    data = file.readlines()

    for line in data:
        words = line.split(",")
        for word in words:
            map.append(word.strip())

    for i in range(len(map)):
        find_path(map[i])
    print "Last destination:",currentx, currenty
    print "Distance:", math.fabs(currentx) + math.fabs(currenty)

if __name__ == '__main__':
    main()