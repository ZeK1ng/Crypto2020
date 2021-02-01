
import base64
import binascii
import collections
import string
import sys
arr = []
for line in sys.stdin:
    arr.append(line)
s1 = arr[0]
s2 = arr[1]
s1 = bytes.fromhex(s1)
s2 = bytes.fromhex(s2)
bts = []
for i in range(len(s1)):
    bts.append(s1[i]^s2[i])
res=bytes(bts)
# print(res.hex())
sys.stdout.write(res.hex())
