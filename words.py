import argparse
import collections
import os
from collections import Counter
import errno
import re
import string
def remove_punctuation(value):
    result = ""
    for c in value:
        # If char is not punctuation, add it to the result.
        if c not in string.punctuation:
            result += c
    return result

while True:
    try:
        filename = input("Enter name of input file: ")#input alıyorum
        file = open(filename, "r", encoding="utf8")#dosya okunabilir
        wordcount = Counter(file.read().split())#counter nesne sayar, split liste oluşturur
        for k, v in wordcount.most_common():
            print(remove_punctuation(k), v)
    except IOError as e:
        if e.errno == errno.EACCES: #dosya ulaşılabilir mi kontrolü yapıyor
            print("Dosya var ama okunabilir değil")
        elif e.errno == errno.ENOENT: #dosya var mı yok mu onu kontrol eder
            print("Bu dosya yok. Dosya adını doğru ve uzantısıyla birlikte(.txt) yazdığınıza emin olun")