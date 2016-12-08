import numpy as np
import collections

result = []

def findMostCommonInColumn(data):
    column_index = 0
    while(column_index < len(data[0])):
        column = []
        for i in range(len(data)):
            column.append(data[i][column_index])
        column_index += 1
        result.append(collections.Counter(column).most_common()[-1]) # Remove [-1] to find most common

        


def main():
    data = np.array(np.genfromtxt("input.txt", dtype='str'))
    findMostCommonInColumn(data)
    for letter in result:
        print letter[0][0]


if __name__ == '__main__':
    main()