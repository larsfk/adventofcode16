# AoC day 2 - part 2. 
# Got some help by looking at Bildzeitung's solution https://github.com/bildzeitung/2016adventofcode/blob/master/02/code2.py

instructions = {"U":(-1,0), "R":(0,1), "D":(1,0), "L":(0,-1)}
keys = []
key = (2, 0) #Starts at 5


KEY_PAD = [
    ['x','x','1','x','x'],
    ['x','2','3','4','x'],
    ['5','6','7','8','9'],
    ['x','A','B','C','x'],
    ['x','x','D','x','x']
]

def findCode(data):
    global key
    nxtKey = key
    print KEY_PAD[nxtKey[0]][nxtKey[1]]

    for letter in data:
        if not(letter == "\n"):
            nxtKey = (max(0, min(key[0] + instructions[letter][0],4)), max(0,min(key[1] + instructions[letter][1],4)))
            if (KEY_PAD[nxtKey[0]][nxtKey[1]] != 'x'):
                key = nxtKey
    keys.append(KEY_PAD[key[0]][key[1]])

def main():
    global key
    key = (2, 0) #Starts at 5
    f = open("input.txt","r")
    data = f.readlines()
    for line in data:
        findCode(line)
        print "line done"
    print keys


if __name__ == '__main__':
    main()