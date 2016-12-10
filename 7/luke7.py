import re

IPS = 0
SSLs = 0

def findIPs(liste):
    global IPS
    abba = 0
    for i in range(len(liste)):
        if isAbba(liste[i]):
            if i % 2 != 0:
                abba = 0
                break
            else:
                abba += 1
    IPS += abba

def findSSL(liste):
    global SSLs
    aba = []
    for i in range(len(liste)):
        aba.append(returnSSL(liste[i]))
    for i in range(len(aba)-1):
        for j in range(len(aba[i])):
            if len(aba[i]) > 0:
                rev = aba[i][j][1] + aba[i][j][0] + aba[i][j][1]
                if rev in aba[i+1]:
                    SSLs += 1
                    #print rev, aba

                

def returnSSL(s):
    aba = []
    for p in zip(s[:-2], s[1:-1], s[2:]):
        if p[0] == p[-1] and p[0] != p[1]:
            aba.append(p[1]+p[0]+p[1])
    return aba

def isReverse(s,q):
    if s[0] == q[1] and q[0] == s[1] and s[0] != q[0]:
        return True
    return False

def isAbba(s):
    for p in zip(s[:-3], s[1:-2], s[2:-1], s[3:]):
        if p[0] == p[-1] and p[1] == p[2] and s[0] != s[1]:
            return True
    return False


def lineToList(line):
    line.strip()
    liste = line.replace("["," ").replace("]"," ").split()
    findSSL(liste)

def main():
    f = open("input.py")
    data = f.readlines()
    f.close()
    for line in data:
        lineToList(line)
    print "IP:", IPS
    print "SSL:",SSLs


if __name__ == '__main__':
    main()