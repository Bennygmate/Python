#!/usr/bin/python
import sys
import re
import math
import glob

poet = {}

if len(sys.argv) != 2:
    print >>sys.stderr, "Usage %s <Word_Match>" %sys.argv[0]
    sys.exit(1)

for file in glob.glob("poems/*.txt"):
    for poem_line in open(file):
        file = re.sub ('.*/', '', file)
        file = re.sub ('_',' ', file)
        file = re.sub ('\..*', '', file)
        for poem_word in re.split ('[^A-Za-z]', poem_line):
            for poem_word in re.findall ('[\S]+', poem_word):
                if file in poet:
                    if poem_word in poet[file]:
                        poet[file][poem_word] += 1
                    else:
                        poet[file][poem_word] = 1        
                else:
                    poet[file] = {}
                    poet[file][poem_word] = 1 

count_word = sys.argv[1].lower()
word_count = 0
total_word = 0

for file in sorted(poet.keys()):
    for poem_word in sorted(poet[file].keys()):
        total_word += poet[file][poem_word]
        if poem_word.lower() == count_word:
            word_count += poet[file][poem_word]
    log_word = float(word_count + 1) / total_word
    log_words = math.log(log_word)
    print "log((%d+1)/%6d) = %8.4f %s" %(word_count, total_word, log_words, file)
    total_word = 0
    word_count = 0
