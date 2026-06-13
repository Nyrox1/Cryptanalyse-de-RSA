from utilitaires import pgcd
        


def fact(n):
    a = 1
    for i in range(2, n + 1):
        a *= i
    return a



def Pollard(N) :
    B = 2
    a = 2
    t = True
    while t:
        B = fact(B)
        a = pow(a, B, N)
        p = pgcd(a-1, N)
        if p != 1 :
            print (f"p = {str(p)}")
            q = int(N/p)
            print (f"q = {str(q)}")
            t = False
        B += 1
    print(B-1)
    return (p,q)
 


'''
Test possible : 

N = 172189
Pollard(N)

'''
