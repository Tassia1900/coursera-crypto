import sys
import time
from gmpy2 import mpz
from gmpy2 import mpfr
from gmpy2 import isqrt
from gmpy2 import mul
from gmpy2 import div

N = mpz('720062263747350425279564435525583738338084451473999841826653057981916355690188337790423408664187663938485175264994017897083524079135686877441155132015188279331812309091996246361896836573643119174094961348524639707885238799396839230364676670221627018353299443241192173812729276147530748597302192751375739387929')

def main():
    start = time.clock()
    try:
	N_prime = mpz(mul(24,N))
	A_prime = isqrt(N_prime)+1
	x_prime = mpz(isqrt(pow(A_prime,2) - N_prime))
	p_prime = mpz(A_prime - x_prime)
	q_prime = mpz(A_prime + x_prime)
	assert mpz(mul(p_prime,q_prime)) == N_prime
	p = mpz(div(p_prime,6))
	q = mpz(div(q_prime,4))
	print 'p = ' + str(p)
	print 'q = ' + str(q)
	print 'Time: ' + str(time.clock() - start)
	assert mpz(mul(p,q)) == N
    except KeyboardInterrupt:
            print 'Keyboard interrupt!'
	    print 'Time: ' + str(time.clock() - start)
            sys.exit()
    
main()




