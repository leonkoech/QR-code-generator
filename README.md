# QR code generator
A mini python script that creates QR codes for you. The only variable it takes is your string.

## Requirements
1. [qrcode package](https://pypi.org/project/qrcode/)
2. [pillow](https://pypi.org/project/Pillow/)
3. python 3.6+

## How To
1. The program asks for an input text
2. select whether you want the background of the qr code to be transparent or not
2a. If you want a tranpsarent background the code proceeds
2b. if you want to set a background you'll follow input prompts for the RGB values
3. Select whether you want the color for the qr code to be transparent or not
3a. If you want a transparent qr code, it will be generated and stored under processed.png
3b. If you want to set the color or the qr code, you'll have to input the RGB values by following the prompts 