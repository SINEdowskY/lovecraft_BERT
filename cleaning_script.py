import re
import os
import string

TEXTS_DIR = r"lovecraft_novels"
DIR_LIST = os.listdir(TEXTS_DIR)
TXT_FILES = [file for file in DIR_LIST if file.endswith('.txt')]
full_text = ""

for text_file in TXT_FILES:
    print(f"File: {text_file}")
    with open(TEXTS_DIR+f"/{text_file}") as file:
        lines = file.readlines()
        file.close()
    
    lines[0] = lines[0].removeprefix("\ufeff")
    lines = list(map(str.lower, lines))
    lines = list(map(str.casefold, lines))
    lines = [line for line in lines if line != "\n"]
    lines = list(map(lambda x: " ".join(x.split()), lines))
    words = []
    for line in lines:
        splited = line.split(" ")
        for word in splited:
            matches = re.findall(r'\b\w+(?:[-]{1,2}\w+)+\b', word)
            if len(matches) > 0:
                for match in matches:
                    splited_dash = None
                    if "--" in match:
                        splited_dash = match.split("--")
                    else:
                        splited_dash = match.split("-")
                    for sd in splited_dash:
                        words.append(sd)
            else:
                words.append(word)
    
    words = list(map(lambda x: re.sub(f"[{re.escape(string.punctuation)}]", "", x), words))
    
    for word in words:
        full_text += word+" "

with open("train_text.txt", mode="w+") as file:
    file.write(full_text)
    file.close()
