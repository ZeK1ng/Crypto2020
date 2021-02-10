from oracle import *
import sys
import binascii
import random

def checkArgs():
 if len(sys.argv) < 2:
    print "Usage: python sample.py <filename>"
    sys.exit(-1)

def readData():
    f = open(sys.argv[1])
    cypherText = f.read()
    f.close()
    return cypherText


def main():
    checkArgs()
    # sys.stdout.write(cypherText)
    cypherText = readData()
    cypherText = converToIntBlocks(cypherText)
    num_blocks = len(cypherText)/ 16
    ctextBlocks = split_to_blocks(cypherText,num_blocks)
    # print(ctextBlocks)
    Oracle_Connect()
    sys.stdout.write(startAttack(ctextBlocks,num_blocks))
    sys.stdout.write('\n')
    Oracle_Disconnect()

def generateRandomBytes(size):
    randomBs = []
    for x in range(size):
        randomBs.append(random.randrange(256))
    return randomBs

def doSendMessage(randBytes,ind,intermediate_state,block):
    ch = ''
    for c in range(256):
        C1 = randBytes + [c]
        if 16-ind > 1:
            tmp = [a^b for (a,b) in zip([16 - ind]*(15 - ind),intermediate_state)]
            C1 += tmp
        if Oracle_Send(C1+block, 2) == 1:
            ch = c
            break
    return [ch ^ (16 - ind)] + intermediate_state
    
def startAttack(cypherBlocks,num_blocks):
    msg = []
    for i in range(num_blocks-1, 0, -1):
        curr_block= cypherBlocks[i]
        intermediate_state = []
        for j in range(15, -1, -1):
            randomBytes = generateRandomBytes(j)
            intermediate_state = doSendMessage(randomBytes,j,intermediate_state,curr_block)
        new_msg = [a^b for (a,b) in zip(intermediate_state, cypherBlocks[i-1])]
        new_msg += msg
        msg = new_msg
    res= []
    for ch in msg[:len(msg)-msg[len(msg)-1]]:
        res.append(chr(ch))
    return ''.join(res)


def split_to_blocks(text,num_blocks):
    res = []
    for i in range(num_blocks):
        res.append(text[i*16:i*16+16])
    return res

def converToIntBlocks(ctext):
    converted = []
    for i in range(0,len(ctext),2):
        converted.append(int(ctext[i:i+2],16))
    return converted



if __name__ == "__main__":
    main()
