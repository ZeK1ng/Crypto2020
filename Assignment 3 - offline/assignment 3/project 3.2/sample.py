from oracle import *
from helper import *

n = 18827690415350041396414434810597520017910815333161057356162945988138195085254940268485861291346289776388016321879849042436516237657288178187349615689385753023468758602595839311040974848241392481576556554592951771327433286806077428123386814516856161993467036266547833142962710363403155329390370050701660816367L

e = 65537

Oracle_Connect()

msg = "Crypto is hard --- even schemes that look complex can be broken"

m = ascii_to_int(msg)

# Should fail, because you're not allowed to query on the original message
sigma = Sign(m)
assert(sigma < 0)

# All other arbitrary messages <= 504 bits should be accepted by the oracle
msg = "Hello, World!"

m = ascii_to_int(msg)

sigma = Sign(m)
if sigma < 0:
    raise SystemExit

if Verify(m,sigma):
    print "Oracle is working properly!"

Oracle_Disconnect()
