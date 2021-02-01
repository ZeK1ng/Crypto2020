import base64
import binascii
import sys
def uniryXor(x,y):
    x = bytes.fromhex(x)
    y = bytes.fromhex(y)
    bts = []
    for i in range(len(x)):
        bts.append(x[i]^y[i])
    return bytes(bts)

def repeatingXor():
    arr = []
    for line in sys.stdin:
        arr.append(line.strip())
    key = arr[0]
    msg = arr[1]
    key_byte = ""
    for i in range(len(msg)):
        nx = key[i % len(key)]
        key_byte+=nx
    sys.stdout.write(uniryXor(msg.encode().hex(),key_byte.encode().hex()).hex())
def main():
    repeatingXor()
    
if __name__ == '__main__':
    main()