import qrcode

def main():
    song = "https://www.youtube.com/watch?v=gIiQSIKksGg"
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size= 5,
    border= 5,
)

    qr.add_data(song)
    qr.make(fit=True)

    img = qr.make_image(fill_color="blue", back_color="white")
    img.save("my-qrcode.png")



if __name__=="__main__":
    main()
