from Crypto.Hash import SHA256
import sys
import time

hashDict = {}

def H(str):
  hash = SHA256.new()
  hash.update(str)
  s = bin(int(hash.hexdigest(),16))
  return s[-50:]

def main():
    i=21000000
    j=i+17000000
    start = time.clock()
    while i <= j:
        try:
	    hashValue = H(str(i))
	    hashDict[hashValue] = i
            i = i +1
        except KeyError:
            print 'Key error: ' + str(i) + ' and ' + str(hashDict[H(str(i))])
	    print 'Time: ' + str(time.clock() - start)
            sys.exit()
        except KeyboardInterrupt:
            print 'Keyboard interrupt: ' + str(i)
	    print 'Time: ' + str(time.clock() - start)
            sys.exit()
        except MemoryError:
            print 'Memory error: ' + str(i)
	    print 'Time: ' + str(time.clock() - start)
            sys.exit()
    print 'Dictionary finished in time ' + str(time.clock() - start)
    j = j+1
    while 1:
        try:
	    hashValue = H(str(j))
	    if hashDict.has_key(hashValue):
		print 'Collision found: ' + str(j) + ' and ' + str(hashDict[hashValue])
		print 'Hash value: ' + str(hashValue)
	    	print 'Hex values: ' + str(j).encode('hex') + ' and ' + str(hashDict[hashValue]).encode('hex')
		print 'Time: ' + str(time.clock() - start)
            	sys.exit()
            j = j +1
        except KeyError:
            print 'Key error: ' + str(i) + ' and ' + str(hashDict[H(str(i))])
	    print 'Time: ' + str(time.clock() - start)
            sys.exit()
        except KeyboardInterrupt:
            print 'Keyboard interrupt: ' + str(i)
	    print 'Time: ' + str(time.clock() - start)
            sys.exit()
        except MemoryError:
            print 'Memory error: ' + str(i)
	    print 'Time: ' + str(time.clock() - start)
            sys.exit()

    print str(i)
    
main()




