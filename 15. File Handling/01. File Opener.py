try:
    text_file = open("text.txt")
    print("File found")
    # print(text_file.read())
except FileNotFoundError:
    print("File not found")