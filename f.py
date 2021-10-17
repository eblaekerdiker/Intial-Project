import re
filename = input("Enter name of input file: ")#input alıyorum
file = open(filename, "r", encoding="utf8")#dosya okunabilir
wordcount={}
for word in file.read().split():
    if word in wordcount:
        wordcount[word] += 1
    else:
        wordcount[word] = 1
for k,v in wordcount.items():
    print(k, v)