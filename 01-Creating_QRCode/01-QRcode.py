import qrcode as qr

# img1 = qr.make("https://www.youtube.com/@wscubetech")

# img1.save("WScube_youtube.png")



# using PIL
from PIL import Image

img2 = qr.QRCode(version=1,
                 error_correction=qr.constants.ERROR_CORRECT_H,
                 box_size=10, border=4)

img2.add_data("https://www.youtube.com/@MagnetBrainsEducation")
img2.make(fit=True)

image = img2.make_image(fill_color="green", back_color="white")

image.save("MagnetBrains_youtube.png")
