import sys
import time
import gmpy2
from gmpy2 import mpz
from gmpy2 import mul
from gmpy2 import addmul

hashTable = {}
p = mpz('13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171')
g = mpz('11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568')
h = mpz('3239475104050450443565264378728065788649097520952449527834792452971981976143292558073856937958553180532878928001494706097394108577585732452307673444020333')

def reverse(x,p): 
    #Lortu x**-1 Z_p multzoan
    return mpz(pow(x,p-2,p))    

def main():
    start = time.clock()
    B = 2**20
    x1 = 0
    x0 = 0
    g_reverse = mpz(reverse(g,p)) #g**-1
    g_B = mpz(pow(g,B,p))         #(g**B) mod p

    #Iterazio bakoitzean berreketa guztia kalkulatu beharrean,
    #aurreko iterazioko balioari berreketaren oinarria bidertu
    # x**3 = (x**2)*x; x**4 = (x**3)*x ...
    next_value = h                #x1=0 => h/g**x1=h/1=h
    try:
        for x1 in xrange(B):
	    #Lortu h/g**x1 eta gorde hiztegian
	    hashTable[next_value] = x1
	    #next_value = h/g**(x1 + 1) = h/(g**x1)*g:
            next_value = mpz(mul(next_value,g_reverse)%p)
        print 'Hiztegia amaitu da: ' + str(time.clock() - start)
	next_value = 1                #x0=0 => (g**B)**x0=1
        for x0 in xrange(B):
	    #Lortu (g**B)**x0 eta bilatu hiztegian
	    if hashTable.has_key(next_value):
		print 'Emaitza aurkitu da: ' + str(time.clock() - start)
		print '   x0 = ' + str(x0)
		print '   x1 = ' + str(hashTable[next_value])
		print '   x = ' + str(mpz(addmul(mpz(hashTable[next_value]),mpz(x0),mpz(B))%p)) 
		sys.exit()
	    next_value = mpz(mul(next_value,g_B)%p)
    except KeyboardInterrupt:
        print 'Keyboard interrupt: x1=' + str(x1) + ', x0=' + str(x0)
        print 'Denbora: ' + str(time.clock() - start)
        sys.exit() 
             
main()




