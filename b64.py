import base64

img_path = "img/icon.PNG"

with open(img_path, "rb") as img_file:
    b64_string = base64.b64encode(img_file.read())

print(b64_string)