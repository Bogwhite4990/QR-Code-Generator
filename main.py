import qrcode
from PIL import Image
import requests

# Here you can put any link from any image
url = 'https://tinypng.com/images/social/website.jpg'
response = requests.get(url, stream=True)
face = Image.open(response.raw)

# Resize the image
size = (20, 20)  # Specify the desired size
face = face.resize(size)

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('http://examplee.com')
qr.make(fit=True)

img_qr_big = qr.make_image(fill_color="yellow", back_color="black").convert('RGB')
pos = ((img_qr_big.size[0] - face.size[0]) // 2, (img_qr_big.size[1] - face.size[1]) // 2)

img_qr_big.paste(face, pos)
img_qr_big.save('data/src/qr_code.png')
