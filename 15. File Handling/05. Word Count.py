import os

file_1 = open("words.txt", "w")
file_1.write("quick is fault")
file_1.close()
file_2 = open("input.txt", "w")
file_2.write("-I was quick to judge him, but it wasn't his fault.")
file_2.write("-Is this some kind of joke?! Is it?")
file_2.write("-Quick, hide here…It is safer.")
file_2.close()

content = []
with open("words.txt", "r") as f:
    for word in f.read().split():
        if word != " ":
            content.append(word.lower())

with open("input.txt", "r") as f:
    for el in content:
        for word in f.read().split():

            if el == word:
                print(1)


os.remove("words.txt")
os.remove("input.txt")