# Steganography

## About

Here's some scripts that use LSB (Least Significant Bit) based steganography for hiding data inside images. The encode function loops through the image pixels starting from top left corner. It takes three pixels simultaneously getting 9 available LSBs per iteration (RGB image has three color channels). 8 for the bits of a character and the 9th to indicate if the message ended or not. If the message ended, set 9th LSB on and otherwise off.

```bash
python3 steg.py
```
