from chord_circle import *

#funzione per la simulazione della distribuzione di risorse all'interno dei vari nodi dell'anello
#si fissa il numero di nodi per ogni esperimento 100. varia il numero di risorse
def calcolo_numero_item_medio(x=100):
    lungehzza_risorse=[50, 150, 250, 350, 450, 550, 650]
    y=len(lungehzza_risorse)
    risultato = np.empty((x, y))   #matrice dove verranno inseriti i risultati
    for i in range(y):
        print("completato {}/{}".format(i+1,y))
        temp=[] #<-lista per quantià di item inserite per ogni nodo
        for j in range(x):
            arr=hash_function_ip(100)   #gli esperimetni si svolgono tutti su un anello di 100 nodi
            arr=np.sort(arr)
            n=chord_circle(arr)
            n.chord_circle_initialize()
            item_array=[]
            for h in range(lungehzza_risorse[i]): item_array.append(random.randint(0,pow(2,m_bits)-1)) #generazione di un array di risorse
            n.store_item_with_random_choice_of_j(item_array) #l'array generato incrementa i contatori dell'anello
            for k in range(n.m_size): temp.append(n.node_array[k].item) #si inserisce la lunghezza del contatore di ogni nodo in un array
            risultato[j][i]=np.mean(temp) #si calcola la media di risorse per nodo
            print("[{} {}]->{}".format(i, j, risultato[j][i]))
            temp.clear()

    DT = pd.DataFrame(data=risultato[0:, 0:], index=range(1, x+1),
                      columns=range(1,y+1))
    print(DT)
    mean_array=np.zeros(y)
    for i in range(y):mean_array[i]=np.mean(DT[i+1])  #calcolo di stime puntuali
    print("\nmedia:\n")
    print(mean_array)
    fig=plt.figure()
    plt.errorbar(lungehzza_risorse, mean_array, marker='o')
    plt.ylabel("item/node")
    plt.xlabel("numero di risorse")
    plt.title("numero di risorse per nodo (tot=100 nodi)")
    plt.show()

#caloclo di risultati per le simulazioni sulla complessità di find_successor
def calcolo_complessita_find_successor(x=100):
    lunghezza_nodi = [50, 150, 250, 350, 450, 550, 650]
    y=len(lunghezza_nodi)
    complex = np.empty((x, y))
    for i in range(y):
        print("completato {}/{}".format(i + 1, y))
        for j in range(x):
            arr = hash_function_ip(lunghezza_nodi[i])
            arr = np.sort(arr)
            n = chord_circle(arr)
            n.chord_circle_initialize()
            node_index = random.randint(0, n.m_size - 1)   #genero un intero casuale, è l'indice del nodo che fa la ricerca
            item_to_search = random.randint(0, pow(2, m_bits) - 1)   #risorsa da ricercare
            complex[j][i] = n.node_find_successor(node_index, item_to_search)[2]  #applico find_successor e faccio ritornare solo il numero di passaggi
            print("[{},{}]->{}".format(i,j,complex[j][i]))

    DT = pd.DataFrame(data=complex[0:, 0:], index=range(1, x+1),
                      columns=range(1,y+1))
    print(DT)
    ic=np.zeros(y)
    for i in range(y):
        ic[i]=mean_confidence_interval(DT[i+1])   #calcolo intervallo di confidenza sulla media
    mean_array=np.zeros(y)
    for i in range(y):mean_array[i]=np.mean(DT[i+1])   #calcolo stima puntuale della media
    print("\nintervalli di confidenza:\n")
    print(ic)
    print("\nmedia:\n")
    print(mean_array)
    fig=plt.figure()
    plt.ylabel("numero di iterazioni")
    plt.xlabel("numero di nodi")
    plt.title("complessità find_successor")
    plt.errorbar(lunghezza_nodi, mean_array,yerr=ic,ecolor='red', elinewidth=0.7)

    plt.show()

#funzione per il calcolo della complessità realtiva alla sistemazione dell'anello dopo un inserimetno/eliminazione
#in particolare all'aumentare dei nodi nell'anello aumentano anche i nodi inseriti
#al primo passo inserisco 1 nodo, 2 al secondo, 3 al terzo, ...
#questo perchè la grandezza della finger table rimane fissa.
def node_changing_after_join(x=100):
    lunghezza_nodi = [50, 150, 250, 350, 450, 550, 650]
    y=len(lunghezza_nodi)
    risultato = np.empty((x, y))
    for i in range(y):
        print("completato {}/{}".format(i + 1, y))
        for j in range(x):
            arr = hash_function_ip(lunghezza_nodi[i])
            arr.sort()
            n = chord_circle(arr)
            n.chord_circle_initialize()
            k=0 #contatore passaggi
            f=0 #numero di nodi da inserire per ogni simulazione
            while True:
                if f==i+1:   #inserisco i+1 nodi da aggiungere
                    break
                index_node_for_search=random.randint(0,n.m_size-1) #<-nodo che andrà ad inserire il nodo da aggiungere
                node_to_be_insert=random.randint(0, pow(2,m_bits)-1)
                if binary_search(n.a, node_to_be_insert)==-1:
                    a=n.node_join(node_to_be_insert, index_node_for_search) #ritorna i passaggi fatti per aggiioranre il nodo
                    k=k+a
                    f=f+1
            risultato[j][i] = k
            print("[{},{}]->{}".format(i, j, risultato[j][i]))

    DT = pd.DataFrame(data=risultato[0:, 0:], index=range(1, x+1),
                      columns=range(1,y+1))
    print(DT)
    ic=np.zeros(y)
    for i in range(y):
        ic[i]=mean_confidence_interval(DT[i+1])   #calcolo intervalli di confindeza
    mean_array=np.zeros(y)
    for i in range(y):mean_array[i]=np.mean(DT[i+1]) #calcolo della media puntuale
    print("\nintervalli di confidenza:\n")
    print(ic)
    print("\nmedia:\n")
    print(mean_array)
    fig=plt.figure()
    plt.errorbar(lunghezza_nodi, mean_array, yerr=ic, ecolor='red', elinewidth=0.7)
    plt.ylabel("passaggi")
    plt.xlabel("numero di nodi")
    plt.title("passaggi per ristabilire finger table dopo join")

    plt.show()



