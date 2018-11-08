from recursive_cut import *
f = open("data.txt",encoding="utf-8",mode="r")
lines = f.readlines()

word_set = set()
for line in lines:
    for word in recursive_cut(line):
        word_set.add(word.lower())

print(len(word_set))
