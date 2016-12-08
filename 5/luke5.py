import hashlib

def find_door_passord():
    result = [""]*8
    i = 0
    found = 0
    while(found != len(result)):
        streng = "wtnhxymk" + str(i)
        m = hashlib.md5()
        m.update(streng)
        h = m.hexdigest()
        if h[0:5] == '00000':
            if isInt(h[5]):
                index = int(h[5])
                if index < 8 and result[index] == "":
                    result[index] = h[6]
                    found += 1
        i += 1
    return result

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def main():
    print find_door_passord()

if __name__ == '__main__':
    main()
