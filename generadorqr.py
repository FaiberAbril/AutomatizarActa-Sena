import qrcode
from PIL import Image

QR_VERSION = 1
ERROR_CORRECTION = "L"
BOX_SIZE = 10
BORDER = 4

def generate_qr_code(url,nombreqrn, color="green"):
    qr = qrcode.QRCode(
        version=QR_VERSION,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=BOX_SIZE,
        border=BORDER,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color, back_color="white")
    img.save(f"{nombreqr}.png")



url = input("Enter the URL to generate QR code: ")
color = "green"
nombreqr = input("Enter the Name document: ")
generate_qr_code(url, nombreqr,color)
print(f"QR code has been saved as '{nombreqr}.png'")