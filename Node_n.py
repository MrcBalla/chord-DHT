from hashFunction import *

#in questo modulo si andrà a definire la classe Node_n, che descrive gli attributi
#propri del nodo e i suoi metodi

class Node_n:
    def __init__(self, id):
        self.id=id                              #identificatore nodo
        self.ft_start=np.empty(m_bits)          #elemento start di ft
        self.ft_interval=np.empty((m_bits, 2))  #interval mantiene
        self.ft_node=np.empty(m_bits)           #il nodo successivo a start
        self.item=0                             #contatore di risorse di competenza di un determinato nodo


    #metodo per il calcolo del successore di un nodo, richiede com e imput la lista
    #degli altri nodi nell'anello e, se si volesse trovare tramite indice, l'indice
    #si svolge controllo per aritmetica modulare
    def successor(self, array_of_nodes ,index=None):
        if index is None:
            return self.ft_node[0]
        else:
            try:
                return array_of_nodes[index+1]
            except IndexError:
                return array_of_nodes[0]

    #medesime cose di successor controllo per aritmetica modulare non necessario
    #vista a[-1]=a[len(.)-1]
    def predecessor(self, array_of_nodes, index=None):
        if index is None:
            i = binary_search(array_of_nodes, self.id)
            return array_of_nodes[i - 1]
        else:
            if index!=0:
                return index-1
            else:
                return len(array_of_nodes)-1

    #calcolo di elemento ft_start in finger_table
    def compute_ft_start(self):
        for i in range(m_bits):
            self.ft_start[i]=((self.id+pow(2,i))%pow(2, m_bits))

    #calocolo elemento interval di finger_table, ritorna una matrice
    def compute_ft_interval(self):
        for i in range(m_bits):
            a=[self.ft_start[i], ((self.id+pow(2,i+1))%pow(2, m_bits))]
            self.ft_interval[i]=a

    #calcolo fist.node >= finger_start per ogni entrata della tabella
    #questa è una versione lenta del calcolo di ft_node, si scandaglia tutto l'array
    #fino a quando l'elemento finger_start non diventa maggiore dell'elemento di array_of_nodes
    def compute_ft_node_ith_naive(self, j, array_of_nodes):
        succ=0
        for i in range(len(array_of_nodes)):
            if array_of_nodes[i]-self.ft_start[j]>=0:
                succ=array_of_nodes[i]
                return succ

        #dato aritmetica modulo 2^m-1, qui siamo in caso in cui il nodo maggiore di ft_start[i] è il primo del
        #vettore ordinato dei nodi
        if succ==0 :
            succ=array_of_nodes[0]
            return succ

    #versione più veloce, complessità logaritmica; si basa sul binary_search e richiede
    #come parametro una lista ordinata
    #si vuole trovare il primo nodo tale per cui, il suddetto nodo sia maggiore uguale di ft_start.
    #per fare ciò ci si mette al centro dell'array, se il valore è maggiore di ft_start, si farà la ricerca nella parte
    #inferiore, se è minore di ft_start si andrà a fare la ricerca enlla parte superiore. l'elemetno di innovazione
    #rispetto a binary_search è la presenza di minumum, che se si è trovato un nodo candidato ad essere il primo maggiore
    #di ft_start, lo memorizza. si conclude quando non si può più dividere l'array, in quel caso la condizione di
    #termine è minimum o il primo valore dell'array di nodi ordinato.
    def compute_ft_node_ith_fast(self, j, array_of_nodes):
        x=self.ft_start[j]
        if array_of_nodes[len(array_of_nodes)-1]<x:
            return array_of_nodes[0]
        low=0
        high=len(array_of_nodes)-1
        minimum=None
        while high>=low:
            mid=math.floor((high+low)/2)
            if array_of_nodes[mid]-x<0:
                low=mid+1
            if array_of_nodes[mid]-x>0:
                if minimum is None:
                    minimum = array_of_nodes[mid]
                if minimum - x > array_of_nodes[mid] - x:
                    minimum = array_of_nodes[mid]
                high=mid-1
            if array_of_nodes[mid]-x==0:
                return x
        if minimum is None:
            return array_of_nodes[0]
        return minimum

    #caloclo del primo nodo maggiore uguale a ft_start per ogni riga della finger_table
    def compute_ft_node(self, array_of_nodes):
        for i in range(m_bits):
            self.ft_node[i]=self.compute_ft_node_ith_fast(i, array_of_nodes)

    #funzione che inizializza il nodo
    def init_node(self, array_of_nodes):
        self.compute_ft_start()
        self.compute_ft_interval()
        self.compute_ft_node(array_of_nodes)

    def print_n(self):
        print("start:{}\ninterval:{}\nnode:{}".format(self.ft_start, self.ft_interval, self.ft_node))




