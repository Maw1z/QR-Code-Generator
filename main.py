import qrcode
import qrcode.image.svg

def generate_qrcode():
    while True:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=15,
            border=2
        )

        data = input("Enter your data to turn into QR code: ")
        qr.add_data(data)
        qr.make(fit=True)
        file_name = input("Enter name of file without output type: ")

        output_type = input("Enter output type (jpg, png, svg): ").lower()
        while output_type not in ("jpg", "png", "svg"):
            print("Invalid output type, please enter again")
            output_type = input("Enter output type (jpg, png, svg): ").lower()

        if output_type == "svg":
            svg_image_factory = qrcode.image.svg.SvgPathImage
            svg_image = qr.make_image(image_factory=svg_image_factory)
            with open(f"{file_name}.{output_type}", "wb") as f:
                svg_image.save(f)
            print(f"QR code saved as {file_name}.{output_type}")
        else:
            img = qr.make_image(fill_color="#4b99fe", back_color="white")
            img.save(f'{file_name}.{output_type}')
            print(f"QR code saved as {file_name}.{output_type}")

        print()

        rerun = input("Generate another QR code? Enter 1 for Yes, 0 for No: ")
        if rerun == '0':
            print("Thank you for using this application :)")
            break
        elif rerun != '1':
            print("Invalid input. Exiting application.")
            break

generate_qrcode()