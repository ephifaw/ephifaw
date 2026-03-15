import qrcode
# Dirección pública de GitHub Pages
data = "https://ephifaw.github.io/ephifaw/plantilla.html"
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr_final.png")
print("✅ ¡QR WEB generado con éxito como qr_final.png!")
