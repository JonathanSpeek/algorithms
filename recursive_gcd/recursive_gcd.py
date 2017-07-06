def recursive_gcd(a,b):
	'''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
	if a % b == 0:
		return b
	else:
	    return gcd(b, a % b)

def iter_gcd(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    i, large, small = min(a,b), max(a,b), min(a,b)
    
    while True:
        if large % i == 0 and small % i == 0:
            return i
        else:
            i -= 1