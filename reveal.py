from PIL import Image


def reveal():
    path = input("File name and path\n")
    print(decode(path))


def decode(image):
    img = Image.open(image)
    pixels = iter(img.getdata())
    binar = ""
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
        binar += msgBin + " "
        message += chr(int(msgBin, 2))
        if (pixValues[-1] % 2 != 0):
            return message
