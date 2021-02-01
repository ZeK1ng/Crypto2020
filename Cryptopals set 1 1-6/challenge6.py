import base64
import binascii
import statistics 
import sys

#Gets two hex strings!! A and B and returns humming distance
#Write a function to compute the edit distance/Hamming distance between two strings. The Hamming distance is just the number of differing bits. The distance between:
def hammingDistance(a,b):
    bytesarr = uniryXor(a,b)
    return sum(bin(bt).count('1') for bt in bytesarr)



#Gets to byte arrays x a y and returns their xors as bytes
def uniryXor(x,y):
    bts = []
    # print(type(x),type(y))
    for i in range(len(x)):
        bts.append(x[i]^y[i])
    return bytes(bts)

# attacks repeting xor cypher .passed args are not hex strings. 
def repeatingXor(msg,key):
    key_byte =""
    for i in range(len(msg)):
        nx = key[i % len(key)]
        key_byte+=nx
    return uniryXor(bytes.fromhex(msg.encode().hex()),bytes.fromhex(key_byte.encode().hex()))

#attacks singlebitxor cypher . input is a hex , returns string
def singlebitxor(s1):
    ascii_text_chars = [32]+[33]+[46] + list(range(65,91)) + list(range(97, 123))  
    # s1 = bytes.fromhex(s1)
    # s1 = binascii.unhexlify(s1)
    res = None
    for i in range(0,256):
        ck = i.to_bytes(1, byteorder = 'big')
        unixor = uniryXor(s1,ck*len(s1))
        charls = []
        for x in unixor:
            if x in ascii_text_chars:
                charls.append(x)
        numLetters = sum(charls)/len(s1)
        if res == None or numLetters > res[1]:
            res = (uniryXor(s1,ck*len(s1)),numLetters,ck)
    return res
    # print("".join(map(chr,res["msg"]))) #https://stackoverflow.com/questions/606191/convert-bytes-to-a-string



#For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE
def getKeySize(shifrovka, ksize):
    chunks = []
    # for i in range(4) :
    #     chunks.append(shifrovka[i*ksize:(i+1)*ksize])
    #     # print(type(chunks[i]))
    # distances = []
    # distances.append(hammingDistance(chunks[0],chunks[1])/ksize)
    # distances.append(hammingDistance(chunks[1],chunks[2])/ksize)
    for i in range(0,len(shifrovka)-2*ksize, ksize):
        chunks.append(hammingDistance(shifrovka[i:i+ksize],shifrovka[i+ksize:i+2*ksize]))
    return statistics.mean(chunks)/ksize



def transpose_chunks(chunks,ksize):
    transposed_chunks = []
    for i in range(ksize):
        transposed_chunks.append(b'')
    for i, _ in enumerate(chunks):
        transposed_chunks[i%ksize] += chunks[i:i+1]
        
    return transposed_chunks
def attackRepeatingXor(text,key):
    res = bytes()
    index = 0
    for b in text:
        res+=bytes([b^key[index]])
        index = index+1
        index %=len(key)
    return res

def decypher(s):
    s= base64.b64decode(s)
    # print(type(s))
    # return
    str1 = "this is a test"
    str2 = "wokka wokka!!!"
    # assert(hammingDistance(str1,str2) == 37)
    #Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
    probable_key_sizes  = {}
    for i in range (2, 40) :
        probable_key_sizes[i] = getKeySize(s,i)
    # print(probable_key_sizes)
    probable_key_sizes_sorted = sorted(probable_key_sizes.items(), key=lambda kv: kv[1])
    # print(probable_key_sizes_sorted)
    key_size = probable_key_sizes_sorted[0][0]
    # print(key_size)
    # print(chunks)
    # print("---------------------------")
    transposed_chunks = transpose_chunks(s,key_size)
    # print(transposed_chunks)
    key_key = bytes()
    for trch in transposed_chunks:
        getKeyPart = singlebitxor(trch)
        key_key += getKeyPart[2]
    # print(key_key)
    msg = attackRepeatingXor(s,key_key)
    sys.stdout.write(msg.decode("ascii"))
    
def main():
    s = ""
    for line in sys.stdin:
        s = line

    # print(typeof(s)
    decypher(s)
    # print(s.encode().hex())
    
if __name__ == '__main__':
    main()
