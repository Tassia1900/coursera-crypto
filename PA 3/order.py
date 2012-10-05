from Crypto.Hash import SHA256
import sys
import time

hashDict = {}

def main():
    if len(sys.argv) < 3:  
        sys.exit("Usage: python order.py p g")
    p = int(sys.argv[1])
    g = int(sys.argv[2])
    i = 1
    while i < p:
        try:
	    value = (g**i) % p
            if value == 1:
	       print 'Order of ' + str(g) + ' in Z_' + str(p) + ': ' + str(i)
	       sys.exit()
	    print str(i) + 'th power of ' + str(g) + ' mod ' + str(p) + ': ' + str(value)
	    time.sleep(0.25)
	    i = i +1
        except KeyboardInterrupt:
            print 'Keyboard interrupt: ' + str(i)
	    sys.exit() 
             
main()




