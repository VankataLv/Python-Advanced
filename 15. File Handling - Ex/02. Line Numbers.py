import os

with open("text.txt", "w") as f:
    f.write(
        "-I was quick to judge him, but it wasn't his fault.\n-Is this some kind of joke?! Is it?\n-Quick, hide here. It is safer.")

output = open("output.txt", "w")
punctuation_marks = ("-", ",", ".", "!", "?", "'")
with open("text.txt", "r") as f:
    txt = f.read().split("\n")
    line_count = 0
    for line in txt:
        punctuation_marks_count = 0
        letters_count = 0
        line_count += 1
        for symbol in line:
            if symbol == " ":
                continue
            elif symbol in punctuation_marks:
                punctuation_marks_count += 1
            elif symbol.isalpha():
                letters_count += 1
        output.write(f"Line {line_count}: {line} ({letters_count})({punctuation_marks_count})\n")

# Remove comment to delete files
# os.remove("text.txt")
# os.remove("output.txt")

