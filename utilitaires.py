from random import randrange



def bezout(a, b) :
    #Renvoie (p,x,y) tq ax + by = p
    if a == 0 :
        return (b, 0, 1)
    else :
        g, x, y = bezout(b % a, a)
        return (g, y - (b // a) * x, x)
 
 

def inverse_modulaire(b, n) :
    g, x, _ = bezout(b, n)
    if g == 1:
        return x % n



def pgcd(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return pgcd(b, r)



def miller_rabin_temoin(a0, s, d, n):
	a = pow(a0, d, n)
	i=0
	if a == 1:
		return True
	
	while (i <= s-1):
		if a == n - 1:
			return True
		a = (a * a) % n
		i+=1
	
	return False



def miller_rabin(n):
    # On cherche s et d tel que n-1 = (2^s)d avec s la valuation 2-adique de n-1
    d = n-1
    s = 0
    while (d % 2 == 0):
        d = d // 2
        s += 1

    # Probalité que la fonction renvoie pour un nombre non premier : (1/4)^K
    K = 20
    i = 1
    while i <= K:
        a = randrange(2, n-1)
        if not miller_rabin_temoin(a, s, d, n):
            return False
        i += 1

    return True



def generate_large_primes():
    #Genere deux grands nombres premiers distincts sur 512 bits
    
    b = 256
    min_value = 2 ** (b - 1)
    max_value = 2**b - 1

    p = randrange(min_value, max_value)
    q = randrange(min_value, max_value)

    while (q == p) or (not miller_rabin(p)) or (not miller_rabin(q)):
        p = randrange(min_value, max_value)
        q = randrange(min_value, max_value)

    return p, q



def rac_nieme(a, n):
    # Renvoie la racine n-ième de a
    if a == 0:
        return 0

    p, g = 0, a
    while p < g:
        m = (p + g + 1) // 2
        if m ** n <= a:
            p = m
        else:
            g = m - 1
    return p