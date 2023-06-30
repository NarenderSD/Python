import qrcode

def generate_qr_code(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Example usage
url = "https://www.linkedin.com/in/narender-singh-561a53200/"
filename = "qrcode.png"
generate_qr_code(url, filename)
print(f"QR code saved as {filename}")
