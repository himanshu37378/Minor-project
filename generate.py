import qrcode

qrcodedata = {"Name": "Himanshu" , 
              "CRN": "2021150" , 
              "URN" : "2104587" , 
              "Batch": "2020-2024"}

qrcodefilename = "C:/Users/ASUS/OneDrive/Desktop/Qr-code/new.png"

qrObject = qrcode.QRCode()

qrObject.add_data(qrcodedata)
qrObject.make()

qrimage = qrObject.make_image(fill_color="black")

qrimage.save(qrcodefilename)