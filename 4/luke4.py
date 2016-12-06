import collections, string

TOTAL_ID = 0
realRooms = []

def findRooms(line):
    global TOTAL_ID
    code = line.split('-')
    sector_id = int(code[-1][:3])
    checksum = code[-1][3:].strip('[]')
    s = "".join(code[:-1])
    wc = collections.Counter(s).most_common(20)
    for i in range(len(wc)-1):
        if wc[i][1] == wc[i+1][1]:
            if wc[i][0] > wc[i+1][0]:
                c = i + 1
                while(wc[c][0] < wc[c-1][0] and wc[c][1] == wc[c-1][1] and c > 0):
                    temp = wc[c]
                    wc[c] = wc[c-1]
                    wc[c-1] = temp
                    c -= 1
    room = ""
    for i in range(5):
        room += wc[i][0]
    if room == checksum:
        TOTAL_ID += sector_id
        temp = code[:-1]
        temp.append(sector_id)
        realRooms.append(temp)
    
def printRealRoom():
    for room in realRooms:
        print room

def decryptRealRooms(room):
    alphabet = list(string.ascii_lowercase)
    key = room[-1] % 26
    new_letters = []
    for i in range(len(room)-1):
        for j in range(len(room[i])):
            index_of_letter = alphabet.index(room[i][j])
            new_letters.append(alphabet[(index_of_letter + key)%26])
    s = "".join(new_letters)

    if 'north' in s:
        print s,room[-1] 

def main():
    f = open("input.txt", "r")
    data = f.readlines()
    for line in data:
        findRooms(line.strip())
    f.close()

    for room in realRooms:
        decryptRealRooms(room)
    

if __name__ == '__main__':
    main()