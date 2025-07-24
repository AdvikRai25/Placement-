import qrcode
a = qrcode.QRCode()
text_mg = "https://github.com/AdvikRai25/Placement-.git"
a.add_data(text_mg)
a.make(fit=True)
advik = a.make_image(fill_color="black", back_color="white")
advik.save("git.png")
print("Done")