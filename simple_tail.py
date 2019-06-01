#!/usr/bin/python
import sys
import fileinput

for filename in sys.argv[1:]:
    infile = open(filename).readlines()
    i = len(infile)
    if (i - 10 < 0):
        for line in infile:
            sys.stdout.write(line)
    else:
       for x in range(i-10, i):
           sys.stdout.write(infile[x])
