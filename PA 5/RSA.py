import sys
import time
from gmpy2 import mpz
from gmpy2 import mpfr
from gmpy2 import ceil
from gmpy2 import isqrt
from gmpy2 import mul
from gmpy2 import root

N = mpz('179769313486231590772930519078902473361797697894230657273430081157732675805505620686985379449212982959585501387537164015710139858647833778606925583497541085196591615128057575940752635007475935288710823649949940771895617054361149474865046711015101563940680527540071584560878577663743040086340742855278549092581')

def main():
    start = time.clock()
    try:
	A = isqrt(N)+1
	print 'A = ' + str(A)
	x = mpz(isqrt(pow(A,2) - N))
	p = mpz(A - x)
	q = mpz(A + x)
	print 'p = ' + str(p)
	print 'q = ' + str(q)
	print 'Time: ' + str(time.clock() - start)
	assert mpz(mul(p,q)) == N
    except KeyboardInterrupt:
            print 'Keyboard interrupt!'
	    print 'Time: ' + str(time.clock() - start)
            sys.exit()
    
main()




