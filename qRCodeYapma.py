import qrcode

while True:
    print("""
    0-Çıkıs
    1-Instagram
    2-Twitter
    3-Facebook
    """)
    sec = int(input("Lütfen işlemi giriniz: "))
    if sec == 0:
        break
    elif sec == 1:
        id = input("kullanıcı adını girin: ")
        code = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=100,
            border=4
        )
        code.add_data(f"https://www.instagram.com/{id}")
        code.make(fit=True)
        image = code.make_image(fill_color=(0,0,0),back_color="white")
        image.save(f"instagram{id}.png")
    elif sec == 2:
        id = input("kullanıcı adını girin: ")
        code = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=100,
            border=4
        )
        code.add_data(f"https://www.twitter.com/{id}")
        code.make(fit=True)
        image = code.make_image(fill_color=(0,0,0),back_color="white")
        image.save(f"twitter{id}.png")
    elif sec == 3:
        id = input("kullanıcı adını girin: ")
        code = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=100,
            border=4
        )
        code.add_data(f"https://www.facebook.com/{id}")
        code.make(fit=True)
        image = code.make_image(fill_color=(0,0,0),back_color="white")
        image.save(f"facebook{id}.png")
