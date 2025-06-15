from escpos.printer import Serial
from PIL import Image
import os

# Set the width of the print area, ie. width of recipt
print_area_width = 500

def image_resize(path, target_width):
    image = Image.open(path)
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

# Print image:
def print_image(file_name, path):
    
    resized_file_path = image_resize(path, print_area_width)
    
    print("Printing {}...".format(file_name))
    p.image(resized_file_path)
    p.cut()
        

# Print txt file:
def print_txt(file_name, path):

    with open(path, "r", encoding = "utf-8") as file:
        text = file.read()

    print("Printing {}...".format(file_name))
    p.text(text)
    p.cut()

    
# Select file:
def select_file(file_type):
    
    valid_file_name = False
    
    while valid_file_name == False:
        file_name = str(input("File name: "))
        full_path = "printer/" + file_name

        if os.path.exists(full_path):
            print(file_type)
            if file_type == "image":
                print_image(file_name, full_path)
            elif file_type == "text":
                print_txt(file_name, full_path)
                
            valid_file_name = True
                
        else:
            print(f"Entered file does not exist. You entered '{file_name}'")
            valid_file_name == False


# Select file type and print
def print_file():

    valid_file_type = False

    while valid_file_type == False:

        print("Please select file type:\n- Image\n- Text")
        file_type = str(input(""))
        
        lower_file_type = file_type.lower()

        if lower_file_type == "image":
            select_file(lower_file_type)
            valid_file_type = True
        elif lower_file_type == "text":
            select_file(lower_file_type)
            valid_file_type = True
        else:
            print(f"Entered file type is incorrect. You typed in '{file_type}'") 
            valid_file_type = False


if __name__ == "__main__":
    print("Intructions on use:")
    print("Simply type in the file name into the prompt and press enter")
    print("\nNote: that the file extension is also needed (for example, image1.jpeg)\nMaximum width for images is 500px")

    print_file()

    print("Print complete...")
