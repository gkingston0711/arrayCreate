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
    arr = [[(random.randint(1, 100))] * cols] * rows

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

