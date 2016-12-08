import numpy as np

def find_possible_verticals(columns):
    valid_triangles = 0
    print columns
    for i in range(2,len(columns),3):
        if (columns[i-2] + columns[i-1] > columns[i]) and (columns[i-1] + columns[i] > columns[i-2]) and (columns[i-2] + columns[i] > columns[i-1]):
            valid_triangles += 1
    print valid_triangles

def main():
    f = open("input.txt","r")
    data = f.readlines()
    triangles = []

    for line in data:
        triangle = line.strip().split()
        triangle = map(int,triangle)
        triangles.append(triangle)
    triangles = np.array(triangles)
    column1 = np.array(triangles[:,0])
    column2 = np.array(triangles[:,1])
    column3 = np.array(triangles[:,2])
    columns = np.concatenate((column1,column2,column3))
    find_possible_verticals(columns)
    

if __name__ == '__main__':
    main()