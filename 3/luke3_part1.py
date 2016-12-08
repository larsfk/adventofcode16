
def find_valid_triangles(triangles):
    valid_triangles = []
    for triangle in triangles:
        if (triangle[0] + triangle[1] > triangle[2]) and (triangle[1] + triangle[2] > triangle[0]) and (triangle[0] + triangle[2] > triangle[1]):
            valid_triangles.append(triangle)
    return len(valid_triangles)

def main():
    f = open("input.txt","r")
    data = f.readlines()
    triangles = []

    for line in data:
        triangle = line.strip().split()
        triangle = map(int,triangle)
        triangles.append(triangle)
    
    number_of_valid_triangles = find_valid_triangles(triangles)
    print "Nr of valid triangles", number_of_valid_triangles
    print "Total nr of triangles", len(triangles)

if __name__ == '__main__':
    main()
