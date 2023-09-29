import os

with open("text.txt", "w") as f:
    f.write("-I was quick to judge him, but it wasn't his fault.\n")
    f.write("-Is this some kind of joke?! Is it?\n")
    f.write("-Quick, hide here. It is safer.")

illegal_symbols = ("-", ",", ".", "!", "?")
line_to_print = ""
with open("text.txt", "r") as f:
    txt = f.readlines()
    for line_count in range(0, len(txt) + 1, 2):
        cur_line = txt[line_count]
        for el in cur_line:
            if el in illegal_symbols:
                el = el.replace(el, "@")
            line_to_print += el
        line_to_print = line_to_print.split()[::-1]
        lst_to_print = []
        for word in line_to_print:
            lst_to_print.append(word)
        print(" ".join(lst_to_print))
        lst_to_print.clear()
        line_to_print = ""

# Remove comment to delete files
# os.remove("text.txt")
