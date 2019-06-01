#!/usr/bin/python 
import sys
import re

count = 0
for line in sys.stdin:
    for alpha in re.split (r'[^A-Za-z]', line):
        for alpha in re.findall (r'[\S]+', alpha):
            count += 1
print "%d words" %(count)
