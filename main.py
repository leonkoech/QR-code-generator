import qrcode
def main():
    link="https://fnutechclub.web.app/"
    img = qrcode.make(link)
    type(img)  
    img.save("fnutechclub.png")
if __name__ == '__main__':
    main()
