from getHtml import getHtml
import server
import pathlib
import qrcode

path = "molecules"
adderess ="10.0.4.141:8000"

welcome=open("welcome.txt", "r").read()
print(welcome)

task = input("> ")
while task!="q" and task!="Q":
    if task == "a" or task == "add":
        #html
        smiles = input("SMILES molekule: ")
        notes = input("Opis: ")
        name=pathlib.Path(smiles)
        with open(f"{path}/html/{name}.html", "w") as f:
            f.write(getHtml(smiles=smiles,width="100%",height="50%",scale=0.3))
            f.write(notes)
        
        #qr
        url = f"http://{adderess}/{name}.html"
        
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR code (1-40)
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,  # Size of each box in pixels
            border=4,     # Thickness of the border
            )
        qr.add_data(url)
        qr.make(fit=True)
        img = qr.make_image()
        img.save(f"{path}/qrCodes/{name}.png")
        print (f"QR kod spremljen kao {path}/qrCodes/{name}.png")


    elif task == "s" or task == "start":
        server.start()
    task = input("> ")
    print(welcome)
