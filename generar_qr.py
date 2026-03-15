import qrcode
# Ahora apunta a la carpeta principal, que abrirá index.html automáticamente
data = "https://ephifaw.github.io/ephifaw/"
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_final.png")
print("✅ ¡QR actualizado para index.html generado con éxito!")
