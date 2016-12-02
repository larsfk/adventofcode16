key = 5
keys = []

def u():
    if (key - 3) > 0:
        return key - 3
    else:
        return key
def r():
    if (key + 1) < 10:
        if not(key == 3 or key == 6):
            return key + 1
        else: 
            return key
    else:
        return key
def d():
    if (key + 3) < 10:
        return key + 3
    else:
        return key
def l():
    if (key - 1) > 0:
        if not(key == 4 or key == 7):
            return key - 1
        else:
            return key
    else:
        return key

instructions = {"U":u(), "R":r(), "D":d(), "L":l()}


def findCode(data):
    global key

    for letter in data:
        if not(letter == "\n"):
            instructions = {"U":u(), "R":r(), "D":d(), "L":l()}
            key = instructions[letter]
            print letter, key
    keys.append(key)

def main():
    global key
    key = 5

    f = open("input.txt","r")
    data = f.readlines()
    for line in data:
        findCode(line)
        print "line done"
    print keys


if __name__ == '__main__':
    main()