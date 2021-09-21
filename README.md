# QR code generator
A mini python script that creates QR codes for you. The only variable it takes is your string.

## Requirements
1. [qrcode package](https://pypi.org/project/qrcode/)
2. [pillow](https://pypi.org/project/Pillow/)
3. python 3.6+

## How To
- The program asks for an input text
- select whether you want the background of the qr code to be transparent or not
  - If you want a tranpsarent background the code proceeds
  - If you want to set a background you'll follow input prompts for the RGB values
- Select whether you want the color for the qr code to be transparent or not
  - If you want a transparent qr code, it will be generated and stored under processed.png
  - If you want to set the color or the qr code, you'll have to input the RGB values by following the prompts 
## Pictures
I have a habit of displaying the code in action

![code in action](https://user-images.githubusercontent.com/39020723/134251696-6502183a-0016-4a65-acb5-05c234295841.png)

This is the output when the code is scanned <br><br>
<img src="https://user-images.githubusercontent.com/39020723/134251717-a0c7c790-7906-49ee-8f33-cd6b66fdeb6d.jpeg" alt="Output when code is scanned" width="240"/>
