from oracle import *
import random
import binascii
import sys

def checkargs():
    if len(sys.argv) <2 :
        print("Usage: python forge.py <filename>")
        sys.exit(-1)

def getInput():
    f=open(sys.argv[1])
    data = f.read()
    f.close()
    return data  
    
def getBlocks(data,block_size):
    return [data[i:i+block_size] for i in range(0,len(data),block_size)]

def sliceInHalf(block,block_size):
    return block[0:block_size/2],block[block_size/2:block_size]


def xore_firstHWithTag(data,tag):
    res = []
    for i in range(len(tag)):
        xr = tag[i] ^ ord(data[i])
        res.append(chr(xr))
    return "".join(res)

def getTag(data,block_size,blocks):
    res = []
    for _ in range(block_size/2):
        res.append(0)
    for block in blocks:
        first_half,second_half = sliceInHalf(block,block_size)
        # print first_half,second_half
        xor_first_half_with_res = xore_firstHWithTag(first_half,res)
        # print(xor_first_half_with_res)
        res = Mac(xor_first_half_with_res+second_half,len(xor_first_half_with_res+second_half))
    return res

def verifyTag(data,tag):
    if Vrfy(data,len(data),tag) == 1:
        print ("Message verified successfully!")
    else:
        print ("Message verification failed.")

def main():
    checkargs()  
    data = getInput()
    # sys.stdout.write(data+"\n")
    block_size = 32
    blocks = getBlocks(data,block_size)
    Oracle_Connect()
    tag = getTag(data,block_size,blocks)
    verifyTag(data,tag)
    Oracle_Disconnect()



if __name__ == "__main__":
    main()

