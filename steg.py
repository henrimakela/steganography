from hide import hide
from reveal import reveal
from PIL import Image

answer = int(input("Steganography: \n 1. Hide data \n 2. Reveal data"))

if answer == 1:
    hide()
elif answer == 2:
    reveal()
else:
    raise Exception("Invalid input")
