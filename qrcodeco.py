import qrcode

data = 'Hello! My name is Kely :)'

qr = qrcode.QRCode(version= 2, box_size= 10, border= 5)

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color='white', back_color='black')

img.save('C:/Users/User/OneDrive/Documentos/Portfólio/meuqrcode.png')
