#!/usr/bin/python
import re
import sys

for line in sys.stdin:
    first = re.sub('[0-4]','<', line)
    second = re.sub('[6-9]','>', first)
    sys.stdout.write(second)
