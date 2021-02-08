from oracle import *
import sys
import binascii

f = open(sys.argv[0])
cypherText = f.read()
f.close()
sys.stdout.write(cypherText)