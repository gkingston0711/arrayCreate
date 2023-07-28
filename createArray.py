import json
import random

file = open('config.json')

def createArray(D,L,H):

    myArray =[]
    #2D array
    for i in range(L):
        myArray.append(random.randint(1, 100))


    return myArray


def main():
    data = json.load(file)
    TwoD = (data['2D'])
    ThreeD = (data['3D'])
    length = int(data['length'])
    height = (data['height'])

    if TwoD:
        myArray=createArray(TwoD,length,height)
    else:
        createArray(ThreeD,length,height)

    print(myArray)

    file.close()

if __name__ == '__main__':
    main()

