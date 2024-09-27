import qrcode
def QR_img_generator(txt_str, name, file_format):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(txt_str)
    qr.make(fit=True)
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    # Save the image
    return img.save(f"{name}.{file_format}")

# --------------------------------------------------------------------------------------

link = 'Enter Your Data'
File_name = 'Qr'
file_format = 'jpeg'

# --------------------------------------------------------------------------------------

QR_img_generator(link, File_name,file_format)

# --------------------------------------------------------------------------------------