from utilitaires import *
import time



def dechiffrement_Hastad(x,e) :
    m = int(rac_nieme(x,e)) % 256
    print (f"Message : {chr(m)}")
    return 0
  


def th_restes_chinois(C_i, N_i) :
    mu, nu, e_i = [],[],[]
    x_0, N = 0, 1
    

    for n_i in N_i:
        N*=n_i
    
    for n_i in N_i :
        mu.append(N//n_i)


    for j in range(len(N_i)) :
        nu.append(inverse_modulaire(mu[j],N_i[j]))

    # Calcul e_i = nu_i * mu_i
    for j in range(len(N_i)) :
        e_i.append( mu[j]*nu[j] )
        
    # Calcul et retour de x
    for j in range(len(N_i)) :
        x_0 += e_i[j] * C_i[j]
    x = int(x_0 % N)
    print (f"x : {x}")
    return x 
 


def Hastad(C_i, N_i, e):
    x = th_restes_chinois(C_i, N_i)
    return x
 
 

def test_hastad():
    # On choisit e "petit"
    e = 7
    message = "Bonjour, je m'appelle Yassine."  

    N_i = []

    i = 0
    while i < e:
        p, q = generate_large_primes()
        t = True
        for j in range(i):
            if pgcd(N_i[j], p*q) != 1:
                t = False
        if t:
            N_i.append(p*q)
            i+=1
        
    
    chiffrement_par_cle = []
    for n in N_i:
        chiffrement_i = [pow(ord(c), e, n) for c in message]
        chiffrement_par_cle.append(chiffrement_i)

    debut = time.perf_counter()

    message_dechiffre = ""
    for i in range(len(message)):
        C_i = [chiffrement_par_cle[j][i] for j in range(e)] 
        x = Hastad(C_i, N_i, e)
        m_i = int(rac_nieme(x,e)) % 256
        message_dechiffre += chr(m_i)
        
    fin = time.perf_counter()

    print(f"Message d'origine : {message}")
    print(f"Message retrouvé par Hastad : {message_dechiffre}")
    print(f"Temps d'exécution : {fin - debut:.6f} secondes")



'''
Test possible : 

C_i = [125,14,198]
N_i = [299,319,323]
e = 3
Hastad(C_i, N_i, e)

'''
    
