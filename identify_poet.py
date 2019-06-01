#!/usr/bin/python
import sys
import re
import math
import glob
from sys import maxint

word_count = 0
total_word = 0
log_words = {}
poet = {}
big_log = -maxint

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

for poem_txt in sys.argv[1:]:
    for poem_txt in glob.glob(poem_txt):
        for poem_lines in open(poem_txt):
            for poem_words in re.split ('[^A-Za-z]', poem_lines):
                for poem_words in re.findall ('[\S]+', poem_words):
                    for file in sorted(poet.keys()):
                        for poem_word in sorted(poet[file].keys()):
                            total_word += poet[file][poem_word]
                            if poem_word.lower() == poem_words.lower():
                                word_count += poet[file][poem_word]
                        log_word = float(word_count + 1) / total_word
                        if file in log_words:
                            log_words[file] += float(math.log(log_word))
                        else:
                            log_words[file] = float(math.log(log_word))
                        total_word = 0
                        word_count = 0
    for file in sorted(log_words.keys()):
        if big_log < (log_words[file]):
            big_log = log_words[file]
            copy_poet = file
        log_words[file] = 0
    print "%s most resembles the work of %s (log-probability=%.1f)" %(poem_txt, copy_poet, big_log)
    big_log = -maxint



