import json

file = open('config.json')

def createArray(D,L,H):
    print(D)

def main():
    data = json.load(file)
    TwoD = (data['2D'])
    ThreeD = (data['3D'])
    length = (data['length'])
    height = (data['height'])



    file.close()

if __name__ == '__main__':
    main()

