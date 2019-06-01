#!/usr/bin/python 
import sys
import re

if len(sys.argv) != 2:
    print >>sys.stderr, "Usage: %s <Counted Word>" % sys.argv[0]
    sys.exit(1)

count_word = sys.argv[1].lower()
word_count = 0

for line in sys.stdin:
    for alpha in re.split (r'[^A-Za-z]', line):
        for alpha in re.findall (r'[\S]+', alpha):
            if count_word.lower() == alpha.lower():
                word_count += 1
print "%s occurred %d times" %(count_word, word_count)
