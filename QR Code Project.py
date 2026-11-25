import qrcode
# Enter the data
data= input("Enter text or URL:")

#Generate QR Code
qr= qrcode.make(data)

#Save the QR code as an image
qr.save("my_qrcode.png")
print("QR Code generated successful!")

