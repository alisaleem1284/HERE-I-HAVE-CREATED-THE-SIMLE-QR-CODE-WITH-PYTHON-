import qrcode 

url = input("enter the url:").strip()
# HERE IN THE FILE PATH YOU HAVE TO PUT THE PATH OF THE FLODER WHERE YOU NEED TO STORE THE QR CODE
file_path = "qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path )

print("the qr code is created")

