#!/usr/bin/python
import sys
import re
import glob
import math

if len(sys.argv) != 2:
    print >>sys.stderr, "Usage: %s <Word-Match>" %sys.argv[0]
    sys.exit(1)

count_word = sys.argv[1]
total_word = 0
word_count = 0

for file in glob.glob("poems/*.txt"):
    for poem_line in open(file):
        for poem_word in re.split ('[^A-Za-z]', poem_line):
            for poem_word in re.findall ('[\S]+', poem_word):
                total_word += 1             
                if poem_word.lower() == count_word.lower():
                    word_count+= 1
    log_word = float(word_count) / (total_word)
    file = re.sub ('.*/', '', file)
    file = re.sub ('_',' ', file)
    file = re.sub ('\..*', '', file)
    print "%4d/%6d = %.9f %s" %(word_count,total_word, log_word, file)
    total_word = 0
    word_count = 0
                    
            
