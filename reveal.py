from PIL import Image
from encrypt import decrypt, loadKey


def decodeEncrypted(image, key):
    img = Image.open(image)
    pixels = iter(img.getdata())
    message = buildMessage(pixels)
    return decrypt(key, message).decode('utf-8')


def decode(image):
    img = Image.open(image)
    pixels = iter(img.getdata())
    return buildMessage(pixels)


def buildMessage(pixels):
    message = ""
    while(True):
        pixValues = [value for value in pixels.__next__() +
                     pixels.__next__() +
                     pixels.__next__()]

        msgBin = ""

        for value in pixValues[:8]:
            if value % 2 == 0:
                msgBin += '0'
            else:
                msgBin += '1'
        message += chr(int(msgBin, 2))
        if (pixValues[-1] % 2 != 0):
            return message
