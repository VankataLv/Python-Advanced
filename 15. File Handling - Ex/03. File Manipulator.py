import os
cur_cmd_counter = 0
user_cmd = input()
while user_cmd != "End":
    action, file_name, *content = user_cmd.split("-")
    if action == "Create":
        with open(file_name, "w"):
            pass
    elif action == "Add":
        with open(file_name, "a+") as f:
            f.write(f"{content[0]}\n")
    elif action == "Replace":
        try:
            with open(file_name, "r+") as f:
                txt = f.read()
                txt = txt.replace(content[0], content[1])
                f.seek(0)
                f.write(txt)
                txt = ""
        except FileNotFoundError:
            print("An error occurred")
    elif action == "Delete":
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")

    # The following block of code is for easier access the content of file.txt and for debugging purposes
    # try:
    #     with open("file.txt", "r") as f:
    #         cur_cmd_counter += 1
    #         print(f"- After line#:{cur_cmd_counter} | current state of file is: \n{f.read()} ")
    # except FileNotFoundError:
    #     print("File named->'file.txt', does not exist")
    user_cmd = input()
