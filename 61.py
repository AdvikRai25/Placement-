import qrcode
def get_info():
    with open("registrations.txt", "r") as file:
        return file.read().strip()

a = qrcode.QRCode()
text_mg = get_info()
a.add_data(text_mg)
a.make(fit=True)

ad = a.make_image(fill_color="red", back_color="white")
ad.save("adv.png")

print("Saved successfully")
