import sys
import time
from gmpy2 import mpz
from gmpy2 import isqrt
from gmpy2 import mul

N = mpz('648455842808071669662824265346772278726343720706976263060439070378797308618081116462714015276061417569195587321840254520655424906719892428844841839353281972988531310511738648965962582821502504990264452100885281673303711142296421027840289307657458645233683357077834689715838646088239640236866252211790085787877')

def main():
    start = time.clock()
    try:
	A = isqrt(N)+1
	while True:
	    x = mpz(isqrt(pow(A,2) - N))
	    p = mpz(A - x)
	    q = mpz(A + x)
	    if mpz(mul(p,q)) == N:
		print 'p = ' + str(p)
	        print 'q = ' + str(q)
		print 'Time: ' + str(time.clock() - start)
		break
	    A += 1
    except KeyboardInterrupt:
            print 'Keyboard interrupt! (iteration #' + str(i) + ')'
	    print 'Time: ' + str(time.clock() - start)
            sys.exit()
    
main()




