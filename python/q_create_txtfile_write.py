def create_file_write(filename,content):
    with open(filename, "w") as file:
        file.write(content)

def read_file(filename):
    with open(filename, "r") as file:
        return print(file.read())

try:
    create_file_write("output.txt",'"Hello, World!"')
    read_file("output.txt")
except FileNotFoundError as e:
    print(f"Error: File not found | {e}")
except IOError as e:
    print(f"Error: An I/O error occurred | {e}")
except Exception as e:
    print(f"Error: {e}")