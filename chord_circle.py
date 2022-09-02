from Node_n import *

#in questo modulo si va ad implementare la calsse chord_circle, che è l'anello su cui si basa l'algoritmo.
#la classe riceve come parametro l'array di nodi da inseirire inizialmente. Ha come attributi un array di nodi di tipo
#Node_n, definiti nel modulo Node_n, il vettore di interi contenente gli identificatori per ogni nodo, la quantità di nodi
#nell'anello. i metodi gestiscono l'anello

class chord_circle:
    def __init__(self, array):
        self.node_array = []              #array di elementi Node_n
        self.a = array                    #array di interi, identificatori dei nodi
        self.m_size=len(array)            #intero, numero di nodi nell'anello

    #funzione per inizializzare l'anello
    def chord_circle_initialize(self):
        for i in range(self.m_size):
            self.node_array.append(Node_n(self.a[i]))   #inseriso un il tipo di dato Node_n
            self.node_array[i].init_node(self.a)        #inizializzo Node_n

    def print_chord_circle(self):
        for i in range(self.m_size):
            print("\nid:{}".format(self.node_array[i].id))
            self.node_array[i].print_n()

    #metodo che trova il nodo, presenta all'interno della FT del nodo interrogato, più vicino alla risorsa
    #riceve come parametri: j->indice del nodo a cui si fa la richiesta  item->risorsa da ricercare
    #la funzione ritorna il nodo trovato, il suo indice e il numero di passaggi fatti per trovare  il nodo
    def node_closest_preceding_finger(self, j, item, report=False):
        count=0
        for i in range(m_bits - 1, -1, -1):
            count=count+1
            if conditionA(item, self.node_array[j].id, self.node_array[j].ft_node[i]):
                b = self.node_array[j].ft_node[i]
                k = binary_search(self.a, b)  #per trovare l'indice dell'identificatore ritornato sopra
                if report: print("closest preceding finger:{}".format(self.node_array[k].id))
                return [self.node_array[k], k, count]
        if report: print("closest preceding finger:{}".format(self.node_array[j].id))
        return [self.a[j], j, count]

    #metodo che trova il nodo precedente una risorsa
    #riceve come parametri, l'indice j della risorsa a cui si fa l'interrogazione, la risorsa da cercare
    #ritrna il nodo, l'indice in cui si trova il nodo e il numero di passaggi
    def node_find_predecessor(self, j, item, report=False):
        n_tilde = self.node_array[j]
        count=0
        while not conditionB(n_tilde.successor(self.a), n_tilde.id, item):
            [n_tilde_id,j,pred_count]= self.node_closest_preceding_finger(j, item,report=False)
            count=pred_count+count
            n_tilde = self.node_array[j]
        if report:print("predecessor node of {} is {}".format(item, n_tilde.id))
        return [self.a[j], j, count]

    #metodo per la ricerca del nodo successivo una risorsa
    #riceve come parametri, l'indice j della risorsa a cui si fa l'interrogazione, la risorsa da cercare
    # ritrna il nodo, l'indice in cui si trova il nodo e il numero di passaggi
    def node_find_successor(self, j, item, report=False):
        [n_tilde, n_tilde_index, count]=self.node_find_predecessor(j ,item)

        if n_tilde_index==self.m_size-1:
            k=0
        else:
            k=n_tilde_index+1

        if report: print("successor node of {} is {} with {} complexity".format(item, self.a[k], count))
        return [self.a[k], k, count]

    #funzione per il calcolo di un nuovo nodo, si dichiara il nuovo nodo e si inizializza
    #ritorna il nodo creato, riceve come parametro l'identificatore del nodo da creare
    def computate_new_node(self, id):
        new_node=Node_n(id)
        new_node.init_node(self.a)
        return new_node

    #si modifica la finger table del nodo creato in modo che sia coerente con l'anello
    #riceve come parametri id, identificatore del nodo creato e j, indice di un nodo già presente
    #nell'anello
    def node_init_finger_table(self, id, j):
        new_node = self.computate_new_node(id)
        new_node.ft_node[0]=self.node_find_successor(j, new_node.ft_start[0])[0]
        for i in range(m_bits-1):
            if conditionC(new_node.ft_node[i], new_node.id,new_node.ft_start[i+1]):
                new_node.ft_node[i+1]=new_node.ft_node[i]
            else:
                new_node.ft_node[i+1]=self.node_find_successor(j, new_node.ft_start[i+1])[0]
        return new_node


    #funzione che aggiunge nell'anello il nuovo nodo, richiede come parametri l'indetificatore
    #del nodo da aggiungere e l'indice di un nodo già nell'anello
    #ritorna la posizione del nuovo nodo nell'array di nodi
    def add_in_chord_table(self, id, j):
        new_node = self.node_init_finger_table(id, j)
        i = self.m_size - 1
        while i >= 0 and self.node_array[i].id > new_node.id:
            i = i - 1
        self.node_array.insert(i + 1, new_node)
        self.a.insert(i + 1, id)
        self.m_size = self.m_size + 1
        return i + 1

    #con questa funzione verifichiamo che l'iesimo elemento della finger table del nodo j sia corretto o se è necessario
    #sostituirlo con s
    #riceve come parametri s, il valore dell'identificatore del nuovo nodo, i, la riga della finger table da modificare
    #j, j l'indice del nodo che si sta valutando se modificare, count il contatore di passaggi fatti, index_added l'indice
    #del nodo che è appena stato inserito
    def new_node_update_finger_tables(self, s, i, j, count, index_added):
        if j == index_added and j!=0:
            j=j-1
        elif j==index_added and j==0:
            j=self.m_size-1

        print("--> {} € [{} {}) <---".format(s, self.node_array[j].id, self.node_array[j].ft_node[i]))
        if conditionC(self.node_array[j].ft_node[i], self.node_array[j].id, s):
            print("cambio in node:{} ft_node:{} -> {}".format(self.node_array[j].id, self.node_array[j].ft_node[i], s))
            self.node_array[j].ft_node[i]=s
            k=self.node_array[j].predecessor(self.a, index=j) #<-tempo constante
            print("pred of {} is {}".format(self.node_array[j].id, self.node_array[k].id))
            count=count+1
            count=self.new_node_update_finger_tables(s, i, k, count, index_added)
        return count

    #aggiorna gli elementi della finger table con le nuove informazioni portate dal nuovo nodo in new_index.
    #si va a ritroso calcolando  prima un nodo precedente a quello appena inserito, poi
    #tramite la funzione sopra aggiornando i ft_node con il valore del nodo inserito
    #riceve come parametro l'indice del nuovo nodo
    def node_update_others(self, new_index):
        count=0
        for i in range(m_bits):
            print("i={} , {}-{}={} count:{}".format(i,self.node_array[new_index].id,pow(2, i) ,(self.node_array[new_index].id-pow(2, i))%pow(2,m_bits),count))
            p=self.node_find_predecessor(new_index, (self.node_array[new_index].id-pow(2, i))%pow(2,m_bits))[1]   #riotrna l'indice del nodo precedente a new_index
            print("predecessor of {} is {}".format((self.node_array[new_index].id-pow(2, i))%pow(2,m_bits), self.node_array[p].id))
            count=self.new_node_update_finger_tables(self.node_array[new_index].id,i,p,count,new_index)
        return count

    #funzione per aggiungere il nodo in un anello, riceve come parametri l'identificatore del nuovo
    #nodo e l'indice di un nodo già presente nell'anello, ritorna il numero di cambiamaneti fatti nelle finger_table già presenti nell'anello
    def node_join(self, id, j):
        if self.m_size > 0:
            new_index = self.add_in_chord_table(id, j)  #aggiunge nodo all'anello
            k = self.node_update_others(new_index)   #aggiorna le informazioni nelle finger_table di nodi già presenti nell'anello
            return k
        else:
            for i in range(m_size):
                self.node_array[0].ft_node[i] = id
                return 0

    #funzione che ripartisce un'array di risorse tra i vari nodi dell'anello
    def store_item_with_random_choice_of_j(self, array_of_items):
        for i in range(len(array_of_items)):
            j=random.randint(0,self.m_size-1)    #si sceglie un nodo casuale
            index=self.node_find_successor(j, array_of_items[i])[1]
            self.node_array[index].item=self.node_array[index].item+1
