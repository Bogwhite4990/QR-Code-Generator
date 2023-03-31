# QR-Code-Generator
Prerequisites
Before using the script, you need to install the required Python packages, qrcode and Pillow, using pip. You can install them using the following command:


```pip install qrcode Pillow```
Using the Script
To use the script, follow the steps below:

Clone the repository: Clone the repository containing the script to your local machine. You can do this by running the following command in the terminal:
bash

```git clone https://github.com/your_username/your_repository.git```
Navigate to the directory: Change into the directory containing the script. You can do this by running the following command:
bash

```cd your_repository```
Modify the script: Open the script in your preferred code editor and modify the following variables to suit your needs:


```url:``` The URL of the image you want to use for the QR code.
```size:``` The desired size of the image (in pixels) you want to paste onto the QR code.
```add_data():``` The data you want to encode in the QR code.
```Run the script:``` Once you have made the necessary modifications, you can run the script by running the following command in the terminal:

```python qr_code_generator.py```
This will generate a QR code with the image pasted onto it and save it as qr_code.png in the data/src directory.

Commands and What They Do
Here's an explanation of what each command in the script does:



```import qrcode```
This line imports the qrcode library, which is used to generate the QR code.



```from PIL import Image```
This line imports the Image module from the Pillow library, which is used to open, manipulate, and save images.



```import requests```
This line imports the requests library, which is used to download the image from the specified URL.



```url = 'https://tinypng.com/images/social/website.jpg'
response = requests.get(url, stream=True)
face = Image.open(response.raw)```

These lines download the image from the specified URL and open it as a PIL image object.


```Copy code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)```

This creates a new QR code object with the specified version, error correction level, box size, and border size.


```
qr.add_data('http://example.com')
qr.make(fit=True)```
These lines add the data you want to encode in the QR code and generate the QR code.


```
img_qr_big = qr.make_image(fill_color="yellow", back_color="black").convert('RGB')```

This generates a PIL image object of the QR code with the specified fill color, background color, and image mode.


```
size = (100, 100)
face = face.resize(size)```
These lines resize the downloaded image to the desired size.


```
pos = ((img_qr_big.size[0] - face.size[0]) // 2, (img_qr_big.size[1] - face.size[1]) // 2)
img_qr_big.paste(face, pos)```
These lines calculate the position where the resized image should be pasted onto the QR code and paste the resized image onto the QR code.

```
img_qr_big.save('data/src/qr_code.png')```
This line saves the final QR code with the pasted image as a PNG file in the data/src directory.

Conclusion
That's it! You now know how to use the script to generate a QR code with an image pasted onto it. Don't forget to modify the script to suit your needs and run it to see the result. If you have any questions or issues, feel free to reach out for further assistance.
