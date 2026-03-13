def generateQr(name, domain):
    import qrcode
    from os import getcwd

    #qr
    url = f"http://{domain}/moleclules/html/{name}.html"
    
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1-40)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Size of each box in pixels
        border=4,     # Thickness of the border
        )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image()

    img.save(f"./../../molecules/qrCodes/{name}.png")
    print (f"QR kod spremljen kao molecules/qrCodes/{name}.png")

generateQr("Adrenalin","localhost:8080")
