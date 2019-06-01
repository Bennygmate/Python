#!/usr/bin/python
import re
import sys

if len(sys.argv) != 2:
    print >>sys.stderr, "Usage: %s <Whale Name>" % sys.argv[0]
    sys.exit(1)

client_name = sys.argv[1]

pods = 0
individuals =0

for line in sys.stdin:
    field = re.match(r'^(\d+)\s+(.*)\s*$', line)
    whale_number = int(field.group(1))
    whale_name = field.group(2)    
    if whale_name == client_name:
        pods = pods + 1;
        individuals = individuals + whale_number

print "%s observations: %d pods, %d individuals" %(client_name, pods, individuals)
