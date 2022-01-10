from PIL import Image


def genData(data):
    newd = []
    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd


def encode(img, message):
    data = genData(message)
    pixels = iter(img.getdata())
    newPixArr = []
    for i in range(len(data)):
        pixValues = [value for value in pixels.__next__() +
                     pixels.__next__() +
                     pixels.__next__()]
        for j in range(8):
            if data[i][j] == '1' and pixValues[j] % 2 == 0:
                if pixValues[j] != 0:
                    pixValues[j] -= 1
                else:
                    pixValues[j] += 1
            elif data[i][j] == '0' and pixValues[j] % 2 != 0:
                pixValues[j] -= 1

        # check the 9th bit
        if (i == len(data) - 1):
            if pixValues[-1] % 2 == 0:
                pixValues[-1] |= 1
        else:
            if pixValues[-1] % 2 != 0:
                pixValues[-1] &= ~1

        pix = tuple(pixValues)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]


def hide():

    answer = int(
        input('Select an image: \n 1. Local image \n 2. Image from the web'))

    path = ""
    message = ""
    output = ""

    if answer == 1:
        path = input(
            'Provide relative image path and file name with file extension \n')
        output = input(
            'Provide path and file name with extension for the output file \n'
        )
        answer = int(input(
            'Create the message \n 1. By typing \n 2. From text file'))
        if answer == 1:
            message = input("Type message to be encoded\n")
        elif answer == 2:
            raise Exception('Not yet implemented')
        else:
            raise Exception("Invalid input")

    elif answer == 2:
        raise Exception('Not yet implemented')
    else:
        raise Exception('Invalid input')

    img = Image.open(path)
    modPixels = encode(img, message)
    width = img.size[0]
    x = 0
    y = 0

    for pix in modPixels:
        img.putpixel((x, y), pix)
        if x == width - 1:
            x = 0
            y += 1
        else:
            x += 1

    img.save(output)
    img.close()
