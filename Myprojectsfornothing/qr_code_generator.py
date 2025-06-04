import qrcode

def create_qr(text):
    img = qrcode.make(text)
    img.save("qrcode.png")
    print("QR Code saved as qrcode.png")

if __name__ == '__main__':
    data = input("Enter text or URL: ")
    create_qr(data)
