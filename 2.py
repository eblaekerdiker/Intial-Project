import errno

while True:
  try:
    filename = input("Enter name of input file: ")#input alıyorum
    file = open(filename, "r", encoding="utf8")#dosya okunabilir
    wordCounter = {}
    with open(filename,'r',encoding="utf8") as fh:
      for line in fh:
        # Replacing punctuation characters. Making the string to lower.
        # The split will spit the line into a list.
        word_list = line.replace(',','').replace('\'','').replace('.','').replace("'",'').replace('"','').replace('"','').replace('#','').replace('!','').replace('^','').replace('$','').replace('+','').replace('%','').replace('&','').replace('/','').replace('{','').replace('}','').replace('[','').replace(']','').replace('(','').replace(')','').replace('=','').replace('*','').replace('?','').lower().split()
        for word in word_list:
          # Adding  the word into the wordCounter dictionary.
          if word not in wordCounter:
            wordCounter[word] = 1
          else:
            # if the word is already in the dictionary update its count.
            wordCounter[word] = wordCounter[word] + 1

    print('{:15}{:3}'.format('Word','Count'))
    print('-' * 18)
    # printing the words and its occurrence.
    for  word,occurance  in sorted(wordCounter.items(), key=lambda x: x[1], reverse=True):
      print(word,occurance)

  except IOError as e:
    if e.errno == errno.EACCES:  # dosya ulaşılabilir mi kontrolü yapıyor
      print("Dosya var ama okunabilir değil")
    elif e.errno == errno.ENOENT:  # dosya var mı yok mu onu kontrol eder
      print("Bu dosya yok. Dosya adını doğru ve uzantısıyla birlikte(.txt) yazdığınıza emin olun")