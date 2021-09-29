import qrcode
import image
qr = qrcode.QRCode(
   version = 15,
   box_size = 10,
   border = 5
)

data = "https://github.com/srinaimishareddy"
qr.add_data(data)
qr.maker(fit = True)
img = qr.make_image(fill="black",back_color = "white")
img.save("test.png")