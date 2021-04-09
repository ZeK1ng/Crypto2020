import math

# Find x such that g^x = h (mod p)
# 0 <= x <= max_x
def discrete_log(g, h, p, max_x):
	sqrt_x = math.sqrt(max_x)
	B= math.ceil(sqrt_x)
	B= int(B)
	dict = fillMap(g,h,p,B)
	findXo(dict,g,h,p,B)

def findXo(dict,g,h,p,B):
	glB= pow(g,B,p)
	glb_backup = glB
	for x in range(1,B):
		# print(x)
		if glB in dict:
			ans = x*B + dict[glB]
			print(ans)
			return
		glB= glB* glb_backup%p

def fillMap(g,h,p,B):
	dict= {}
	#had a little help here by a friend of mine
	gll = pow(g,p-2,p)
	backup_gll= gll
	for i in range(1, B):
		dict[h*gll%p] = i
		gll = gll*backup_gll%p
	return dict

def main():
	p = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
	g = 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
	h = 3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333
	max_x = 1 << 40 # 2^40
	discrete_log(g, h, p, max_x)

if __name__ == '__main__':
	main()

