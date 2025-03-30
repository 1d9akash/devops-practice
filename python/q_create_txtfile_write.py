def create_file_write(filename,content):
    with open(filename, "w") as file:
        file.write(content)
        return file
    
def read_file(filename):
    with open(filename, "r") as file:
        return print(file.read())

create_file_write("output.txt",'"Hello, World!"')
read_file("output.txt")