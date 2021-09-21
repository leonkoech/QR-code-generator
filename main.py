from PIL import Image
import qrcode
def backgroundColor(r,g,b,a):
    image=Image.open('unprocessed.png')
    # transform image to RGBA
    image = image.convert('RGBA')
    print(image)
    print(image.mode)
    # print(image.getdata()[2])
    newImage = []
    for item in image.getdata():
        if item[:3] == (255,255,255):
            # enter the new color here
            # choose whether transparent or other ccolors
            if a==0:
                newImage.append((255,255,255,0))
            else:
                newImage.append((r,g,b))
        
        else:
            newImage.append(item)
    image.putdata(newImage)
    image.save('unprocessed.png')

def codeColor(r,g,b,a):
    image=Image.open('unprocessed.png')
    # transform image to RGBA
    image = image.convert('RGBA')
    print(image)
    print(image.mode)
    # print(image.getdata()[2])
    newImage = []
    for item in image.getdata():
        if item[:3] == (0,0,0):
            # enter the new color here
            # choose whether transparent or other colors
            if a==0:
                newImage.append((255,255,255,0))
            else:
                newImage.append((r,g,b))
        
        else:
            newImage.append(item)
    image.putdata(newImage)
    image.save('processed.png')



def main():
    inputtext=input("enter the text you want to turn into a qr code: ")
    img = qrcode.make(inputtext)
    type(img)  
    img.save("unprocessed.png")
    bgcolor = input("is your background transparent: (y/N)")
    if bgcolor == '' or bgcolor == 'y' or bgcolor == 'Y':
        backgroundColor(255,255,255,0)
    else:
        bgr = input("enter the R value of RGB: ")
        bgg = input("enter the B value of RGB: ")
        bgb = input("enter the A value of RGB: ")
        backgroundColor(int(bgr),int(bgg),int(bgb),1)
    codecolor = input("is your qr code transparent: (y/N)")
    if codecolor == '' or codecolor == 'y' or codecolor == 'Y':
        codeColor(255,255,255,0)
    else:
        ccr = input("enter the R value of RGB: ")
        ccg = input("enter the B value of RGB: ")
        ccb = input("enter the A value of RGB: ")
        codeColor(int(ccr),int(ccg),int(ccb),1)
  
   
if __name__ == '__main__':
    main()