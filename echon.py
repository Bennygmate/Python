#!/usr/bin/python
import sys
if len(sys.argv) != 3:
    print >>sys.stderr, "Usage: %s <Number> <Word>" % sys.argv[0]
    sys.exit(1)

number = int(sys.argv[1])
word = sys.argv[2]

i = 0
while i < number:
    sys.stdout.write(word)
    print
    i = i + 1
