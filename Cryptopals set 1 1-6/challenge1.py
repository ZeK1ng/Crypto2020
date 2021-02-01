import base64
import binascii
import sys
# import codecs
s = ""
for line in sys.stdin:
    s = line
# bs1 = codecs.encode(codecs.decode(s, 'hex'), 'base64').decode()
# bs2 = base64.b64encode(binascii.unhexlify(s))
stob = bytearray.fromhex(s)
val = base64.b64encode(stob)
# print(val.decode("utf-8"))
sys.stdout.write(val.decode("utf-8"))
