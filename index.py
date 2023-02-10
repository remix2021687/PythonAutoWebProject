import os, shutil
import localisation as lc

print(lc.take_lang["sentence_1"])
lang = input(lc.take_lang["sentence_2"])

def Lang(localisation):
        print(localisation["sentence_1"])
        print(localisation["sentence_2"])
        Answer_1 = input("Вибір: ")

if lc.take_lang["sentence_2"] == "Українська":
    Lang()



input()