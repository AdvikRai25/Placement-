import qrcode
a = qrcode.QRCode()
text_mg = "upi://pay?pa=abhijithp1003@oksbi&pn=Abhijith P&am=1&cu=INR&tn=demo"
a.add_data(text_mg)
a.make(fit=True)
abhijith = a.make_image(fill_color="black", back_color="white")
abhijith.save("gpay.png")
print("Done")