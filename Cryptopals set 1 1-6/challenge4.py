import base64
import binascii
from binascii import unhexlify
import sys
def uniryXor(x,y):
    bts = []
    for i in range(len(x)):
        bts.append(x[i]^y[i])
    return bytes(bts)

def singlebitxor(s1):
    ascii_text_chars = [32] + list(range(65,90)) + list(range(97, 122))  
    # s1 = bytes.fromhex(s1)
    res = None
    for i in range(0,256):
        ck = i.to_bytes(1, byteorder = 'big')
        numLetters = sum([x in ascii_text_chars for x in uniryXor(s1,ck*len(s1))])
        if res == None or numLetters > res[1]:
            res = ( uniryXor(s1,ck*len(s1)),numLetters)
    return res[0], res[1]
    # print("".join(map(chr,res["msg"]))) #https://stackoverflow.com/questions/606191/convert-bytes-to-a-string
    
def main():
    # singlebitxor()
    inp = []
    for line in sys.stdin:
        inp.append(line.strip())
    inp.pop(0)
    best = None
    for s in inp:
        # s = input()
        s= binascii.unhexlify(s)
        msg,nm = singlebitxor(s)
        if best==None or nm >= best[1]:
            best = (msg, nm)
    sys.stdout.write("".join(map(chr,best[0])))
if __name__ == '__main__':
    main()
