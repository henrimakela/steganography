from PIL import Image


def str2bin(msg):
    return ' '.join(format(ord(x), '08b') for x in msg)


def bin2str(binStr):
    binArr = binStr.split()
    message = ""
    for binVal in binArr:
        message += chr(int(binVal, 2))
    return message


def printLSBFromBChannel(count, img):
    binary = ""
    for i in range(count):
        r, g, b = img.getpixel((i, 0))
        binary += bin(b)[-1:]
    print(binary)


def lsbIsOn(x: int):
    return x & 1 == 1


def genData(data):
    newd = []
    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd


def hide(orig, filename, message):
    delimeter = '111111111100000000'
    img = Image.open(orig)
    msgBinary = str2bin(message) + delimeter
    data = img.getdata()
    newPixelArray = []
    pixelCount = 0
    for item in data:
        if pixelCount < len(msgBinary):
            # create new pixel and change the LSB of the pixels blue channel
            bit = msgBinary[pixelCount]
            r, g, b = item
            if bit == '1' and b % 2 == 0:
                if b != 0:
                    b -= 1
                else:
                    b += 1
            elif bit == '0' and b % 2 != 0:
                b -= 1

            newPix = (r, g, b)
            newPixelArray.append(newPix)
            pixelCount += 1
        else:
            newPixelArray.append(item)
    img.putdata(newPixelArray)
    img.save(filename)


def decode(length, filename):
    delimeter = '111111111100000000'
    img = Image.open(filename)
    data = img.getdata()

    pixelCount = 0
    message = ""
    for pixel in data:
        if pixelCount < length:
            r, g, b = pixel
            if b % 2 == 0:
                message += '0'
            else:
                message += '1'
            pixelCount += 1
        else:
            return ''.join(" " if i % 9 == 0 else char for i, char in enumerate(message, 1))


def printLSB(img, length):
    img = Image.open(img)
    data = img.getdata()
    count = 0
    lsbArr = []
    for item in data:
        if count < length:
            r, g, b = item
            lsbArr.append(bin(b)[-1:])
            count += 1
        else:
            return lsbArr


def isLastBitOn(num: int):
    return num & 1 == 1


def encode(img, message):
    messageData = genData(message)
    data = img.getdata()
    modifiedPixels = []
    pixelCount = 0
    binIndex = 0
    for i in range(0, len(data), 3):
        values = [x for x in data[i] + data[i+1] + data[i+2]]
        # loop through all the bits of a character
        for x in range(8):
            if messageData[binIndex][x] == '1' and values[x] % 2 == 0:
                if values[x] != 0:
                    values[x] -= 1
                else:
                    values[x] += 1
            elif messageData[binIndex][x] == '0' and values[x] % 2 != 0:
                values[x] -= 1
        if (binIndex == len(messageData) - 1):
            print('**** ENDING ****')
            print(i)
            if values[-1] % 2 == 0:
                values[-1] |= 1
            return modifiedPixels
        else:
            if values[-1] % 2 != 0:
                values[-1] &= ~1

        modifiedPixels.append((values[0], values[1], values[2]))
        modifiedPixels.append((values[3], values[4], values[5]))
        modifiedPixels.append((values[6], values[7], values[8]))
        binIndex += 1


def hide2(orig, filename, message):
    img = Image.open(orig)
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
    img.save(filename)
    img.close


def printBin(img, length):
    img = Image.open(img)
    pixels = img.getdata()
    binary = ""
    for i in range(int(length / 3)):
        pix = pixels[i]
        r, g, b = pix
        binary += format(r, '08b')[-1]
        binary += format(g, '08b')[-1]
        binary += format(b, '08b')[-1]
    print(binary)


def decode(img):
    img = Image.open(img)
    message = ""
    pixels = img.getdata()

    for i in range(0, len(pixels), 3):
        msgBin = ""
        values = [x for x in pixels[i] + pixels[i + 1] + pixels[i+2]]
        for value in values:
            if value % 2 == 0:
                msgBin += '0'
            else:
                msgBin += '1'

        message += chr(int(msgBin, 2))
        if values[-1] % 2 != 0:
            return message
