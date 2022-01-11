import argparse
from hide import hide
from reveal import decode, decodeEncrypted
from encrypt import encrypt, decrypt, generateKey, loadKey
from PIL import Image

parser = argparse.ArgumentParser(description="Steganographer")
parser.add_argument("image", help="Path to the image")
parser.add_argument("-m", "--message", help="Message to be hidden",
                    action="store", type=str)
parser.add_argument("-g", "--generate-key", dest="generate_key", action="store_true",
                    help="Whether to generate a new key or use existing. if both -g and -k are omitted, the message will be stored in plain text")
parser.add_argument("-k", "--key", action="store_true",
                    help="Use existing key. Key file needs to be in the same folder as the script and named key.key")
parser.add_argument("-e", "--encode", action="store_true",
                    help="Encode the image, only -e or -d can be specified.")
parser.add_argument("-d", "--decode", action="store_true",
                    help="Decode the image, only -e or -d can be specified.")
parser.add_argument("-o", "--output", help="Output file name",
                    type=str)
args = parser.parse_args()

image = args.image
message = args.message
genKey = args.generate_key
key = args.key
dec = args.decode
enc = args.encode
output = args.output

if genKey and key:
    raise TypeError("Use either -g or -k. Not both")
elif dec and enc:
    raise TypeError("Use either -d or -e. Not both")

if enc:
    if message is None:
        raise TypeError("Please provide a message with -m or --message")
    elif output is None:
        raise TypeError("Please provide the output file with -o or --output")

    if genKey or key:
        if genKey:
            generateKey()
        key = loadKey()
        hide(image, encrypt(key, message).decode('utf-8'), output)
    else:
        hide(image, message, output)
elif dec:
    if key:
        key = loadKey()
        print(decodeEncrypted(image, key))
    else:
        print(decode(image))
