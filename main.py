from random import randrange
from Hastad import *
from Pollard import *
from Wiener import *
from utilitaires import *



def creation_cle(p, q):
    N = p * q
    phi = (p - 1) * (q - 1)

    e = randrange(2, phi)
    while pgcd(e, phi) != 1:
        e = randrange(2, phi)

    d = inverse_modulaire(e, phi)
    # e possede un inverse modulo phi(N) car ils sont premiers entre eux

    return ((e, N), (d, N))



# Fonction de chiffrement
def chiffrement(message, cle_pub):
    e, n = cle_pub
    liste = [pow(ord(char), e, n) for char in message]
    return liste



# Fonction de dechiffrement
def dechiffrement(msg_chiffre, cle_priv):
    d, n = cle_priv
    message = ''.join([chr(pow(char, d, n)) for char in msg_chiffre])
    return message



if __name__ == "__main__":

    p,q = generate_large_primes()
    print(p)
    print(q)
    cle_pub, cle_priv = creation_cle(p,q)
    print(cle_priv)
    print(cle_pub)
    message = "Bonjour, je m'appelle Yassine."
    M = chiffrement(message, cle_pub)
    print(M)
    mes = dechiffrement(M, cle_priv)
    print(mes)
    
    print("\n \n \n")  
    print("************ Test d'Hastad ************")
    print("\n \n \n")
    
    test_hastad()
    
