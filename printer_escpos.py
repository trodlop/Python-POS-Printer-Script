from escpos.printer import Serial
from PIL import Image

def image_resize(path, target_width):
    image = Image.open("printer/" + path)
    scaling_factor = (target_width / float(image.size[0]))
    target_height = int((float(image.size[1]) * float(scaling_factor)))
    resized_image = image.resize((target_width, target_height), Image.LANCZOS)
    resized_image_path = "printer/" + "resized_" + path
    resized_image.save(resized_image_path)
    return resized_image_path

p = Serial(devfile="COM1",
           baudrate=9600,
           bytesize=8,
           parity="N",
           stopbits=1,
           timeout=1.00)
print("Intructions on use:")
print("Simply type in the file name into the prompt and press enter")
print("\nNote: that the file extension is also needed (for example, image1.jpeg)\nMaximum width for images is 500px")

file_name = str(input("File name: "))
resized_file_path = image_resize(file_name, 500)

print("Printing {}...".format(file_name))

p.image(resized_file_path)
p.cut()

print("Print complete...")
