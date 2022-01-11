# Steganography CLI Tool

## About

This is a simple CLI tool that use LSB (Least Significant Bit) based steganography for hiding data inside images. The encode function loops through the image pixels starting from top left corner. It takes three pixels simultaneously getting 9 available LSBs per iteration (RGB image has three color channels). 8 for the bits of a character and the 9th to indicate if the message ended or not. If the message ended, set 9th LSB on and otherwise off.

## Usage

### Encode

#### Plain text

```bash
python3 steg.py test.png -em "This is an example" -o example.png
```

#### Generate a key and encrypt

```bash
python3 steg.py test.png -egm "This is an example" -o example.png
```

#### Use existing key and encrypt. See `python3 steg.py --help ` for more details.

```bash
python3 steg.py test.png -ekm "This is an example" -o example.png
```

### Decode

#### Without decryption

```bash
python3 steg.py example.png -d
```

#### Decrypt with key

```bash
python3 steg.py example.png -dk
```
