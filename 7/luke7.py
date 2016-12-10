IPS = 0
SSLs = 0

def findIPs(ip):
    global IPS
    abba = 0
    for i in range(len(ip)):
        if isAbba(ip[i]):
            if i % 2 != 0:
                abba = 0
                break
            else:
                abba += 1
    IPS += abba

def findSSL(ip):
    global SSLs
    supernet = []
    hypernet = []
    for i in range(len(ip)):
        if i % 2 == 0:
            supernet.extend(returnBAB(ip[i]))
        else:
            hypernet.extend(returnBAB(ip[i]))
    #print "s", supernet, "h", hypernet

    if len(hypernet) > 0 and len(supernet) > 0:
        for bab in supernet:
            aba = bab[1] + bab[0] + bab[1]
            if aba in hypernet:
                #print "bab", bab, "aba", aba
                SSLs +=1    

                

def returnBAB(s):
    bab = []
    for p in zip(s[:-2], s[1:-1], s[2:]):
        if p[0] == p[-1] and p[0] != p[1]:
            bab.append(p[1]+p[0]+p[1])
    return bab

def isAbba(s):
    for p in zip(s[:-3], s[1:-2], s[2:-1], s[3:]):
        if p[0] == p[-1] and p[1] == p[2] and s[0] != s[1]:
            return True
    return False


def main():
    f = open("input.py")
    data_from_file = f.readlines()
    f.close()
    for line in data_from_file:
        line.strip()
        findSSL(line.replace("["," ").replace("]"," ").split())
    print "IP:", IPS
    print "SSL:",SSLs


if __name__ == '__main__':
    main()