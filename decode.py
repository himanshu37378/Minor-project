import cv2

# read the QRCODE image
filename = "C:/Users/ASUS/OneDrive/Desktop/Qr-code/new.png"
image = cv2.imread(filename)
detector = cv2.QRCodeDetector()

data, vertices_array, binary_qrcode = detector.detectAndDecode(image)
# if there is a QR code
# print the data

if vertices_array is not None:
  print("QRCode data:")
  print(data)
else:
  print("There was some error")
