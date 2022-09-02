import numpy as np
import random
import math
import hashlib
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats

m_bits=10

#funzione per la generazione di un ip con protocollo ipv4, l'ip generato è una stringa che dopo sarà passata
#alla funzione di hash
def generate_ip():
    a = str(math.floor(random.randint(0, 255)))
    b = str(math.floor(random.randint(0, 255)))
    c = str(math.floor(random.randint(0, 255)))
    d = str(math.floor(random.randint(0, 255)))
    return str(a + "." + b + "." + c + "." + d)

def search_in_list(arr, x):
    if arr and x in arr:
        return True
    else:
        return False

#funzione che genera casualmente degli interi, che saranno gli identificatori dei nodi all'interno dell'anello
#si parte generando un unico nodo, poi si ciclerà con while la procedura sino alla generazione di num_node identificatori
#di nodo; ho posto anche un controllo sulle collisioni (in generale improbabili se m_bits e num_size compatibili):
#se vi è un nodo con identificatore uguale, se ne genera uno nuovo
def hash_function_ip(num_node):
    hashed_ip=[]
    ip = generate_ip()
    myhash = hashlib.sha1(ip.encode('utf-8'))   #definizione di funzione di hashing
    x = int(myhash.hexdigest(), 16) % pow(2,m_bits)  #id generato dopo procedura di hashing
    hashed_ip.append(x)
    i=1
    while i!=num_node:
        ip=generate_ip()
        myhash=hashlib.sha1(ip.encode('utf-8'))
        x=int(myhash.hexdigest(),16)%pow(2,m_bits)
        if not search_in_list(hashed_ip, x):
            i=i+1
            hashed_ip.append(x)
    return hashed_ip

#implementazione di binary search
def binary_search(list, x):
    low=0
    high=len(list)-1
    while True and high>=low:
        mid=math.floor((low+high)/2)
        if list[mid]==x:
            return mid
        if list[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1


#condizione per appartenenza c€(b,a)
def conditionA(a, b, c):
    if a==b and c!=b:
        return True
    elif a==b and c==b:
        return False
    return ((a>b) and (c<a) and (b<c)) or ((a<b) and ((c > b and c > a) or (c < a and c < b)))
#primo caso estremo superiore maggiore di estremo inferiore, caso base elemento compreso da estremi
#secondo caso estremo inferiore maggiore di estremo superiore: elemento maggiore di entrambi gli estremi
#oppure elemento minore di entrambi gli estremi

#condizione per appartenenza c€(b,a]
def conditionB(a, b, c):
    if a==b:
        return True
    return ((a > b) and (c <= a) and (b < c)) or ((a < b) and ((c > b and c >= a) or (c <= a and c < b)))

#condizione per appartenenza c€[b,a)
def conditionC(a, b, c):
    if a==b:
        return True
    return ((a > b) and (c < a) and (b <= c)) or ((a < b) and ((c >= b and c > a) or (c < a and c <= b)))

#funzione che calocla le bande di confidenza per la media, essendo ipotizzata la normalità e utilizzando un intervallo
#alla Wald, le bande saranno simmetriche introno alla stima puntuale, quindi è sufficiente il calcolo di un solo valore
def mean_confidence_interval(data, confidence=0.95):
    a=np.array(data)
    n=len(a)
    se=scipy.stats.sem(a)  #calcolo sdt deviance
    h=se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return h