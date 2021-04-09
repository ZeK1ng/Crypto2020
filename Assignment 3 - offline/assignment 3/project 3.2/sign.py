from oracle import *
from helper import *
import math

def findAb(m):
    # sqrtM = math.floor(math.sqrt(m))
    # sqrtM = int(sqrtM)
    # print(sqrtM)
    for i in range(3,int(10e5)):
        if m%i == 0:
            return i,m/i
# A friend told me this part so i am letting you know . Plus its a standart wikipedia algorithm
def extendedEuclidean(a,b):
    x,x1,y,y1 = 0,1,1,0
    while a>0:
        (c,a),b = (b//a,b%a),a
        y,y1 = y1,y-c*y1
        x,x1 = x1,x-c*x1 
    return x
def generate_signature(m,n):
    a,b = findAb(m)
# A friend told me this part so i am letting you know . Plus its a standart wikipedia algorithm
    x = extendedEuclidean(Sign(1),n)
    return (Sign(a)*Sign(b)%n*x)%n   
def main():

    n = 18827690415350041396414434810597520017910815333161057356162945988138195085254940268485861291346289776388016321879849042436516237657288178187349615689385753023468758602595839311040974848241392481576556554592951771327433286806077428123386814516856161993467036266547833142962710363403155329390370050701660816367L

    e = 65537
    Oracle_Connect()

    msg = "Crypto is hard --- even schemes that look complex can be broken"

    m = ascii_to_int(msg)

    sigma = generate_signature(m,n)
    if sigma < 0:
        raise SystemExit
    print(sigma)
    if Verify(m,sigma):
        print "Oracle is working properly!"
    else :
        print("Not so much")
    Oracle_Disconnect()


if __name__ =="__main__":
    main()