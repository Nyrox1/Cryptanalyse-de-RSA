from math import log, sqrt
 


def dvpt_frac_continue(n, d):
    liste = []
    a, b = n, d
    while b != 0:
        r = a%b
        q = (a - r) // b
        liste.append(q)
        a, b = b, r
    return liste
 


def reduites_frac_continue(liste):
    # Calcul des réduites
    reduites=[]
    h0, h1 = 1, 0
    k0, k1 = 0, 1
    for i in range(len(liste)):
        h = liste[i] * h1 + h0
        h0, h1 = h1, h
        k = liste[i] * k1 + k0
        k0, k1 = k1, k
        reduites.append((k,h))
    return reduites   
 


def calcul_cle(N, e, f) :
    # p et q son racine de ce polynome : x^2 - (N - phi(N) + 1)x + N
    phi = (e*f[1]-1)//f[0]
    a = 1
    b = -(N-phi+1)
    c = N
    delta =b*b - 4*a*c
    if delta > 0 :
        x1 = (-b + int( sqrt(b*b - 4*a*c)) )//(2*a)
        x2 = (-b - int( sqrt(b*b - 4*a*c)) )//(2*a)
        if x1*x2 == N :
            print(f"p = {x1}")
            print(f"q = {x2}")



def Wiener(e, N, test, C) :
    for f in reduites_frac_continue(dvpt_frac_continue(e, N)) :
        if pow(C, f[1], N) == test :
            calcul_cle(N, e, f)
            return f[1]
    return -1
 



def dechiffrement_Wiener(C, N, d) :
    p = pow(C, d, N) % 256
    print(f"Message d'origine = {p}")
 


'''
Test possible : 

e = 17993
N = 90581
print(f"e : {str(e)}")
print(f"N : {str(N)}")
    
test_msg = 97
msg_chiffre = pow(test_msg, e, N)
d = Wiener(e, N, test_msg, msg_chiffre)
    
if d != -1 :
print(f"d = {str(d)}")
dechiffrement_Wiener(msg_chiffre, N, d)

'''