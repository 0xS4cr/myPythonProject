class CSSGenerator:
    def __init__(self, class_name, x, y, width, height, z_index):
        self.class_name = class_name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.z_index = z_index

    def generate_css(self):
        return f".{self.class_name} {{\n" + \
               f"    position: absolute;\n" + \
               f"    left: {self.x}px;\n" + \
               f"    top: {self.y}px;\n" + \
               f"    width: {self.width}px;\n" + \
               f"    height: {self.height}px;\n" + \
               f"    display: flex;\n" + \
               f"    flex-direction: row;\n" + \
               f"    justify-content: center;\n" + \
               f"    align-items: center;\n" + \
               f"    z-index: {self.z_index};\n" + \
               "}"

def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")

MAX_PAGE_WIDTH = 1920
MAX_PAGE_HEIGHT = 1080

css_code = ""
while True:
    class_name = input("Enter class name (or 'q' to quit): ")
    if class_name == 'q':
        break

    x = get_integer_input("Enter x position: ")
    y = get_integer_input("Enter y position: ")
    width = get_integer_input("Enter width: ")
    while width > MAX_PAGE_WIDTH:
        print(f"Width cannot exceed {MAX_PAGE_WIDTH} pixels. Please enter a smaller value.")
        width = get_integer_input("Enter width: ")

    height = get_integer_input("Enter height: ")
    while height > MAX_PAGE_HEIGHT:
        print(f"Height cannot exceed {MAX_PAGE_HEIGHT} pixels. Please enter a smaller value.")
        height = get_integer_input("Enter height: ")

    z_index = get_integer_input("Enter z-index: ")

    css_gen = CSSGenerator(class_name, x, y, width, height, z_index)
    css_code += css_gen.generate_css() + "\n"
    if css_code:
        print("CSS Code:")
        print(css_code)
    else:
        print("No CSS code generated.")

    continue_choice = input("Do you want to create another box? (y/n)")
    if continue_choice.lower() != 'y':
        break


