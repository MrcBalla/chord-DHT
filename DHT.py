#FILE PER ANNOTAZIONI

from chord_circle import *


#sistema binary search e sorted_list, non ha senso ohni volta rioridinare la lista, a questo punto prova o ad abbandonare
#binary search su ista ordinata e fare linear search o ordino la lista una volta la metto in memoria e via di binary
#search. ANCORA MEGLIO RICHIEDERE INPUT IN CLASSI GIà ORDINATO [RISOLTO]

#cerca di sisitemare questione relativa a memorizzazione di array di nodi, ogni nodo mermorizza l'intero array, vi è
#spreco di memoria, si dovrebbe tentare di memorizzare l'array una volta sola per ogni nodo [RISOLTO]

#per sistemare questione sopra, l'ideale è eliminare l'istanza self.id_other, questa memorizza per ogni nodo un vettore di tutti i nodi. questa viene usata in tre funzioni:
#predecessor e successor, e compute_ft_node_ith, in tutte queste potrebbe essere più sensato avere l'array di tutti i nodi come argomento delle funzioni, dato che nella
#classe chord_circle memorizzo un array di interi dei id dei nodi. [RISOLTO]

#problema di collisioni in generazione di nodi, nonostante abbia usato sha1 e sha256 per la generazione di una chiave hash sorgono varie volte delle collisioni, come si potrebbe
#evitare questa cosa?

#c'è un problema di implementazione, in init_ft_table sorgono probelmi dato che non si può torvare predecessor

#ora c'è pensare alle analisi da fare sui dati: primo su tutti grafico con numero di nodi e numero di items medio per nodo
#si può anche fare il grafico sui tempi, come aumenta il tempo all'aumnetare dei nodi.

#DA ADATTARE SU SUCCESSOR O PREDECESSOR, per risparmiare tempo posso riscrivere la funzione predecesor
#e successor in modo da tenere conto che l'array dei nodi è ordinato

#implementa eccezzione su join, non posso inserire nodo già presente

#in teoria vi è uno sbagli nel caloclo della complessità di node_join, ogni nodo mantiene
#lo stesso numero di informazioni, all'aumentare dei nodi non cambia il numero di info da
#modificare all'interno di ogni nodo, poichè rimane costante, cambia invece il numero
#di nodi da verificare; potrei contare il numero di nodi che subiscono modifiche nella
#finger table, questo dovrebbe aumentare in O(logn)

#--------------risultati da dimostrare---------------------
#numero di nodi da contattare medio per trovare il successore in un N-node network è logn
#numero messaggi medio da inviare medio per ristabilire un anello chord log^2(n)
#ogni nodo sarà responsabile di item/n elementi
#----------------------------------------------------------

#--------------report scritto----------------------------
#per report scritto direi di differenziare in varie parti:
#1)introdizione alla DHT chord
#2)aspetti di programmazione e approccio affrontato, arichitettura del software
#3)discussione dei risultati statistichi ottentati con grafici
#-------------------------------------------------------------


'''''
funzioni da riciclare all'interno della classe chord_circle

#da fixare gli intervalli dato che siamo in artimetica modulo 2^m-1
    #return closest fingere preceding item
    def closest_preceding_finger(self, item):
        i=m_size-1
        #print("e che ne so\n")
        while i>=1:
            #print("i:{}".format(i))
            if self.ft_node[i]>self.id and self.ft_node[i]<item and item>=self.id:
                return self.ft_node[i]
            if self.ft_node[i]<self.id and self.ft_node[i]<item and item<=self.id:
                return self.ft_node[i]
            i=i-1

        return self.id

    def find_predecessor(self, item):
        n_tilde=self
        while True:
            if n_tilde<item and successor_without_self(self.id_other, n_tilde)>=item and successor_without_self(self.id_other, n_tilde)>n_tilde:
                break
            if False:
                break

        return n_tilde.id

    def find_successor(self, item):
        pass
        #n_tilde=
        #return n_tilde.successor()
'''




'''
    def node_init_finger_table(self, b, j):
        print("successor di {} tamite {} n.id {}".format(self.node_array[b].ft_start[0], j, self.node_array[j].id))
        self.node_array[b].ft_node[0]=self.node_find_successor(j, self.node_array[b].ft_start[0])[0]
        #manca un pezzo ma va, bo
        print("compute ft_node[0]")
        for i in range(m_bits-1):
            print("node_ init i:{}".format(i))
            if conditionC(self.node_array[b].ft_node[i], self.node_array[b].id, self.node_array[b].ft_start[i+1]):
                print("if")
                self.node_array[b].ft_node[i+1]=self.node_array[b].ft_node[i]
            else:
                print("else")

                print("self.node_array[b].ft_node[i+1]:{}\n".format(self.node_array[b].ft_node[i+1]))
                self.node_array[b].ft_node[i+1]=self.node_find_successor(j, self.node_array[b].ft_start[i+1])[0]
                print("dopo else")

        #self.print_chord_circle()
'''

'''

    def add_node_in_chord_table(self, id):
        new_node=Node_n(id)   #<-inserisco nuovo Node_n
        i=self.m_size-1
        while i>=0 and self.node_array[i].id>id:
            self.node_array.insert(i+1, self.node_array[i])
            self.a.insert(i+1, self.a[i])
            print("inserito id:{} in posizione {}".format(self.node_array[i].id, i+1))
            i=i-1
        self.a.insert(i+1, id)
        new_node.init_node(self.a)
        self.node_array.insert(i+1, new_node)
        self.m_size=self.m_size+1
        print("---id alternativo---")
        for i in range(self.m_size):print(self.node_array[i].id)
        print("------\n")
        self.print_chord_circle()
        return i+1
        
    "Esperimento 6","Esperimento 7","Esperimento 8","Esperimento 9","Esperimento 10",
                             "Esperimento 11","Esperimento 12", "Esperimento 13", "Esperimento 14", "Esperimento 15", "Esperimento 16"
                        , "Esperimento 17
    
    ,
                  np.mean(DT["Esperimento 6"]),np.mean(DT["Esperimento 7"]),np.mean(DT["Esperimento 8"]),
                  np.mean(DT["Esperimento 9"]),np.mean(DT["Esperimento 10"]),np.mean(DT["Esperimento 11"]),
                  np.mean(DT["Esperimento 12"]),np.mean(DT["Esperimento 13"]),np.mean(DT["Esperimento 14"]),
                  np.mean(DT["Esperimento 15"]),np.mean(DT["Esperimento 16"]),np.mean(DT["Esperimento 17"])

    def new_compute(self, j, array_of_nodes):
        x=self.ft_start[j]
        low=0
        high=len(array_of_nodes)-1
        minimum=[None,0]
        while True:
            mid=math.floor((high+low)/2)
            if high is low:
                mid=high
                if high is low is len(array_of_nodes)-1:
                    return 0
                if array_of_nodes[mid]>x:
                    return mid
                else: return min

            if (array_of_nodes[mid]-x) is 0:
                return mid

            if array_of_nodes[mid]-x<0:
                low=mid+1

            if array_of_nodes[mid]-x>0:
                if minimum[0] is None:
                    minimum[1]=mid
                    minimum[0]=array_of_nodes[mid]-x
                elif minimum[0]>array_of_nodes[mid]-x:
                    minimum[0]=array_of_nodes[mid]-x
                    minimum[1]=mid
                high=mid-1

'''

'''
    def new_compute(self, j, array_of_nodes):
        x=self.ft_start[j]
        low=0
        high=len(array_of_nodes)-1
        minimum=[None,0]
        while True:
            mid=math.floor((high+low)/2)
            if high is low:
                mid=high
                if high is low is len(array_of_nodes)-1:
                    return 0
                if array_of_nodes[mid]>x:
                    return mid
                else: return min

            if (array_of_nodes[mid]-x) is 0:
                return mid

            if array_of_nodes[mid]-x<0:
                low=mid+1

            if array_of_nodes[mid]-x>0:
                if minimum[0] is None:
                    minimum[1]=mid
                    minimum[0]=array_of_nodes[mid]-x
                elif minimum[0]>array_of_nodes[mid]-x:
                    minimum[0]=array_of_nodes[mid]-x
                    minimum[1]=mid
                high=mid-1
                
                
        def add_in_chord_table(self, id, j):
        new_node=self.node_init_finger_table(id, j)
        i=self.m_size-1
        while i>=0 and self.node_array[i].id>new_node.id:
            i=i-1
        self.node_array.insert(i+1,new_node)
        self.a.insert(i+1, id)
        self.m_size=self.m_size+1
        return i+1
        
        
        def node_join(self, id, j):
        if self.m_size>0:
            new_index=self.add_in_chord_table(id, j)
            #print("\nper esempio nodo: 0 successor:{} predecessor:{}".format(self.node_array[0].successor(self.a), self.node_array[0].predecessor(self.a)))
            #print("successor:{} predecessor:{}".format(self.node_array[new_index].successor(self.a), self.node_array[new_index].predecessor(self.a)))
            k=self.node_update_others(new_index)
            return k
        else:
            for i in range(m_size):
                #k=binary_search(self.a, id)
                self.node_array[0].ft_node[i]=id
                return 0
                
        def new_node_update_finger_tables(self, s, i, j, count):
        #print("--> {} € [{} {}) <---".format(s, self.node_array[j].id, self.node_array[j].ft_node[i]))
        #print("----a durante update_ft_table----")
        if between_sx(self.node_array[j].id,self.node_array[j].ft_node[i],s):
            #print("cambio in node:{} ft_node:{} -> {}".format(self.node_array[j].id, self.node_array[j].ft_node[i], s))
            self.node_array[j].ft_node[i]=s
            k=0
            if j != 0:
                k=j-1
            elif j == 0:
                k=self.m_size-1
            count=count+1
            count=self.new_node_update_finger_tables(s, i, k, count)
        return count
        
        
        #se s è l'i-esimo finger del nodo j, aggiorno la finger table del nodo j con s
    #la necessità di inserire index_added ovvero l'indice dove risiede il nuovo nodo aggiunto è
    #data dal dover evitare che si cambino i termini della sua finger table
    def node_update_finger_tables(self, s, i, j, count, index_added):
        #print("--> {} € [{} {}) <---".format(s, self.node_array[j].id, self.node_array[j].ft_node[i]))
        #print("----a durante update_ft_table----")
        if between_sx(self.node_array[j].id, self.node_array[j].ft_node[i], s) and j!=index_added:
            #print("cambio in node:{} ft_node:{} -> {}".format(self.node_array[j].id, self.node_array[j].ft_node[i], s))
            self.node_array[j].ft_node[i]=s
            p=self.node_array[j].predecessor(self.a)
            k=binary_search(self.a, p)
            count=count+1
            count=self.node_update_finger_tables(s, i, k, count, index_added)
        return count
        
        
        #il controllo è per vedere che non entri in mezzo index_added
    def new_node_update_finger_tables(self, s, i, j, count, index_added):
        print("--> {} € [{} {}) <---".format(s, self.node_array[j].id, self.node_array[j].ft_node[i]))
        #print("----a durante update_ft_table----")
        if between_sx(self.node_array[j].id, self.node_array[j].ft_node[i], s) and j!=index_added:
            print("cambio in node:{} ft_node:{} -> {}".format(self.node_array[j].id, self.node_array[j].ft_node[i], s))
            self.node_array[j].ft_node[i]=s
            k=self.node_array[j].predcessor_with_index(j, self.a) #<-tempo constante
            print("pred of {} is {}".format(self.node_array[j].id, self.node_array[k].id))
            count=count+1
            count=self.new_node_update_finger_tables(s, i, k, count, index_added)
        return count

    #j è l'indice dove è inserito l'elemento appena aggiunto, è importante specificarlo anche in node_update_finger dal momento
    #che dobbiamo evitare che il nodo appena aggiunto venga aggiornato nel momento in cui si vanno ad aggiornare le finger tables
    def node_update_others(self, j):
        count=0
        for i in range(m_bits):
            print("i={} , {}-{}={} count:{}".format(i,self.node_array[j].id,pow(2, i) ,(self.node_array[j].id-pow(2, i))%pow(2,m_bits),count))
            p=self.node_find_predecessor(j, (self.node_array[j].id-pow(2, i))%pow(2,m_bits))[1]
            print("predecessor of {} is {}".format((self.node_array[j].id-pow(2, i))%pow(2,m_bits), self.node_array[p].id))
            count=self.new_node_update_finger_tables(self.node_array[j].id,i,p,count,j)
        return count

    def node_join(self, id, j):
        if self.m_size > 0:
            new_index = self.add_in_chord_table(id, j)
            k = self.node_update_others(new_index)
            return k
        else:
            for i in range(m_size):
                self.node_array[0].ft_node[i] = id
                return 0

def conditionA(a, b, c):
    if a==b:
        return True
    return ((a>b) and (c<a) and (b<c)) or ((a<b) and ((c > b and c > a) or (c < a and c < b)))

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




from Node_n import *

class chord_circle:
    def __init__(self, array):
        self.node_array = []
        self.a = array
        self.m_size=len(array)

    # inizializza anello chord, è necessario che a sia ordinato altrimenti il vettore di nodi risulta
    #sballato
    def chord_circle_initialize(self):
        for i in range(self.m_size):
            self.node_array.append(Node_n(self.a[i]))
            self.node_array[i].init_node(self.a)

    # for debug
    def print_chord_circle(self):
        for i in range(self.m_size):
            print("\nid:{}".format(self.node_array[i].id))
            self.node_array[i].print_n()

    # return closest finger preceding item
    def node_closest_preceding_finger(self, j, item, counter=False, report=False):
        count=0
        for i in range(m_bits - 1, -1, -1):
            count=count+1
            if between_exclusive(self.node_array[j].id, item, self.node_array[j].ft_node[i]):
                b = self.node_array[j].ft_node[i]
                k = binary_search(self.a, b)
                if report: print("closest preceding finger:{}".format(self.node_array[k].id))
                return [self.node_array[k], k, count]
        if report: print("closest preceding finger:{}".format(self.node_array[j].id))
        return [self.node_array[j], j, count]

    def node_find_predecessor(self, j, item, counter_pred=False, report=False):
        n_tilde = self.node_array[j]
        count=0
        while not between_dx(n_tilde.id, n_tilde.successor(self.a), item):
            [n_tilde,j,pred_count]= self.node_closest_preceding_finger(j, item,report=False, counter=counter_pred)
            count=pred_count+1+count
            n_tilde = self.node_array[j]
        if report:print("predecessor node of {} is {}".format(item, n_tilde.id))
        return [n_tilde, j, count]

    def node_find_successor(self, j, item, counter_succ=False, report=False):
        [n_tilde, n_tilde_index, count]=self.node_find_predecessor(j ,item, counter_pred=counter_succ)

        if n_tilde_index==self.m_size-1:
            k=0
        else:
            k=n_tilde_index+1

        if report: print("successor node of {} is {} with {} complexity".format(item, self.a[k], count))
        return [self.a[k], k, count]

    def computate_new_node(self, id):
        new_node=Node_n(id)
        new_node.init_node(self.a)
        return new_node

    def node_init_finger_table(self, id, j):
        new_node = self.computate_new_node(id)
        new_node.ft_node[0]=self.node_find_successor(j, new_node.ft_start[0])[0]
        for i in range(m_bits-1):
            if between_sx(new_node.id,new_node.ft_node[i],new_node.ft_start[i+1]):
                new_node.ft_node[i+1]=new_node.ft_node[i]
            else:
                new_node.ft_node[i+1]=self.node_find_successor(j, new_node.ft_start[i+1])[0]
        return new_node

    #sposto insert in fine di join
    def add_in_chord_table(self, id, j):
        new_node = self.node_init_finger_table(id, j)
        i = self.m_size - 1
        while i >= 0 and self.node_array[i].id > new_node.id:
            i = i - 1
        self.node_array.insert(i + 1, new_node)
        self.a.insert(i + 1, id)
        self.m_size = self.m_size + 1
        return i + 1

       #il controllo è per vedere che non entri in mezzo index_added
    def new_node_update_finger_tables(self, s, i, j, count, index_added):
        print("--> {} € [{} {}) <---".format(s, self.node_array[j].id, self.node_array[j].ft_node[i]))
        if between_sx(self.node_array[j].id, self.node_array[j].ft_node[i], s) and j!=index_added:
            print("cambio in node:{} ft_node:{} -> {}".format(self.node_array[j].id, self.node_array[j].ft_node[i], s))
            self.node_array[j].ft_node[i]=s
            k=self.node_array[j].predcessor_with_index(j, self.a) #<-tempo constante
            if k==index_added and k!=0:
                k=k-1
            elif k==index_added and k==0:
                k=self.m_size-1
            print("pred of {} is {}".format(self.node_array[j].id, self.node_array[k].id))
            count=count+1
            count=self.new_node_update_finger_tables(s, i, k, count, index_added)
        return count

    #j è l'indice dove è inserito l'elemento appena aggiunto, è importante specificarlo anche in node_update_finger dal momento
    #che dobbiamo evitare che il nodo appena aggiunto venga aggiornato nel momento in cui si vanno ad aggiornare le finger tables
    def node_update_others(self, j):
        count=0
        for i in range(m_bits):
            print("i={} , {}-{}={} count:{}".format(i,self.node_array[j].id,pow(2, i) ,(self.node_array[j].id-pow(2, i))%pow(2,m_bits),count))
            p=self.node_find_predecessor(j, (self.node_array[j].id-pow(2, i))%pow(2,m_bits))[1]
            if p==j and p!=0:
                p=p-1
            elif p==j and p==0:
                p=self.m_size-1
            print("predecessor of {} is {}".format((self.node_array[j].id-pow(2, i))%pow(2,m_bits), self.node_array[p].id))
            count=self.new_node_update_finger_tables(self.node_array[j].id,i,p,count,j)
        return count

    def node_join(self, id, j):
        if self.m_size > 0:
            new_index = self.add_in_chord_table(id, j)
            k = self.node_update_others(new_index)
            return k
        else:
            for i in range(m_size):
                self.node_array[0].ft_node[i] = id
                return 0

    def store_item_with_random_choice_of_j(self, array_of_items):
        for i in range(len(array_of_items)):
            j=random.randint(0,self.m_size-1)
            index=self.node_find_successor(j, array_of_items[i])[1]
            self.node_array[index].item=self.node_array[index].item+1



# key€[ID1, ID2)
def between_dx(ID1, ID2, key):
    if ID1 == ID2 and key!=ID1:
        return True
    if ID1 == ID2 and key!=ID2:
        return False
    if not ID1 > ID2:
        return True if key > ID1 and key <= ID2 else False
    else:
        return True if key > ID1 or  key <= ID2 else False

#c
def between_sx(ID1, ID2, key):
    if ID1 == ID2 and key!=ID2:
        return True
    if ID1 == ID2 and key==ID2:
        return false
    if not ID1 > ID2:
        return True if key >= ID1 and key < ID2 else False
    else:
        return True if key >= ID1 or  key < ID2 else False

def between_exclusive(ID1, ID2, key):
    if ID1 == ID2 and key!=ID1:
        return True
    if ID1 == ID2 and key!=ID1:
        return False
    if not ID1 > ID2:
        return True if key > ID1 and key < ID2 else False
    else:
        return True if key > ID1 or  key < ID2 else False

  def predecessor(self, array_of_nodes):
        try:
            i = binary_search(array_of_nodes, self.id)
            return array_of_nodes[i - 1]
        except IndexError:
            return array_of_nodes[len(sorted_node_array)-1]

    def predcessor_with_index(self, index, array_of_nodes):
        if index!=0:
            return index-1
        else:
            return len(array_of_nodes)-1

   def successor_index(self, array_of_nodes ,index=None):
        if index is None:
            k=binary_search(array_of_nodes,self.ft_node[0])
            return k
        else:
            if index==len(array_of_nodes):
                return 0
            else:
                return index+1

'''
