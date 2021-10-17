file=open("oguz.txt","r", encoding="utf8")
wordcount={}
for word in file.read().split():
    word = word.lower()
    if word.isalpha == True:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
copy = []
for k,v in wordcount.items():
    copy.append((v, k))


copy = sorted(copy, reverse=True)

for k in copy:
        print ('%s: %d' %(k[1], k[0]))