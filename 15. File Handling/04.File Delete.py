import os

# solution 1
# if os.path.exists("my_first_file.txt"):
#     os.remove("my_first_file.txt")
# solution 2
try:
    os.remove("my_first_file.txt")
except FileNotFoundError:
    print("File already deleted!")
