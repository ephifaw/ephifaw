import qrcode
# Dirección de la subcarpeta del cliente
data = "https://ephifaw.github.io/ephifaw/cevicheria_costa_brava/"
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="#0077b6", back_color="white") # Azul marino para el cliente
img.save("qr_costa_brava.png")
print("✅ ¡QR de Costa Brava generado con éxito!")
