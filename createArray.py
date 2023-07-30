import json
import random

file = open('config.json')

def createArray2D(col):

    myArray =[]

    for i in range(col):
        myArray.append(random.randint(1, 100))
    return myArray

def createArray3D(col,row):
    rows, cols = (row, col)
    arr = [[(0)] * cols] * rows

    for i in range(len(arr)):
        for k in range (len(arr[i])):
            arr[i][k] = (random.randint(1, 100))

    return arr


def main():
    data = json.load(file)
    TwoD = (data['2D'])
    ThreeD = (data['3D'])
    col = int(data['col'])
    row = int(data['row'])

    if TwoD:
        myArray=createArray2D(col)
    else:
        myArray = createArray3D(col,row)

    print(myArray)

    file.close()

if __name__ == '__main__':
    main()

