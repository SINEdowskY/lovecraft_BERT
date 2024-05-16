import re
import os
import string
import nltk

TEXTS_DIR = r"lovecraft_novels"
DIR_LIST = os.listdir(TEXTS_DIR)
TXT_FILES = [file for file in DIR_LIST if file.endswith('.txt')]

one_line = ""
for text_file in TXT_FILES:
    with open(f"{TEXTS_DIR}/{text_file}") as file:
        lines = file.readlines()
        print(f"Read file: {text_file}")
        file.close()
    
    lines[0] = lines[0].removeprefix("\ufeff")
    lines = list(map(lambda x: " ".join(x.split()), lines))
    for line in lines:
        one_line += line + " "

old_new = {
    "--": " ",
    "-": " ",
    "×": "x",
    "ä": "a",
    "æ": "ae",
    "ç": "c",
    "é": "e",
    "ë": "e",
    "ï": "i",
    "ö":"o",
    "ü": "u",
    "ā": "a",
    "´": "'",
    "°":" degrees",
    "&":"and",
    "[":"",
    "]":"",
    "(":"",
    ")":"",
    ":":"",
    ";":"",
    "_":"",
    "\"":"''",
}

for old, new in old_new.items():
    one_line = one_line.replace(old, new)

nltk.download('punkt')

def split_into_sentences(text):
    sentences = nltk.sent_tokenize(text)
    return sentences

sentences = list(split_into_sentences(one_line))

print(' '.join(sorted(set(one_line))))

with open("sentences.txt", mode="w") as file:
    for sentence in sentences:
        file.write(sentence + "\n")