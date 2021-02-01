import base64
import binascii
import sys
def uniryXor(x,y):
    bts = []
    for i in range(len(x)):
        bts.append(x[i]^y[i])
    return bytes(bts)

def singlebitxor(s1):
    ascii_text_chars = [32]+[33] + [46]+ list(range(65,91)) + list(range(97, 123))  
    # s1=input()
    s1 = bytes.fromhex(s1)
    res = None
    for i in range(0,256):
        ck = i.to_bytes(1, byteorder = 'big')
        numLetters = sum([x in ascii_text_chars for x in uniryXor(s1,ck*len(s1))])
        if res == None or numLetters > res[1]:
            res = (uniryXor(s1,ck*len(s1)),numLetters,ck)
    sys.stdout.write("".join(map(chr,res[0])))
    # sys.stdout.write("".join(map(chr,res["key"])))

    # print(res["key"])
def main():
    s1 = ""
    for line in sys.stdin:
        s1 = line
    singlebitxor(s1)
    
if __name__ == '__main__':
    main()
