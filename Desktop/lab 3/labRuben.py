#lab2 lista doble i2017 Código
#26/05/17




#Nodo
class Nodo:
    def __init__(self, next = None, prev = None, valor = None):
        self.next = next
        self.prev = prev
        self.valor = valor

    def __str__(self):
        return self.valor


#ListaDoble       
class ListaDoble:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

#printL
    def printL(self):
        nodo = self.head
        lista_final = []
        for i in range(self.length):
            while nodo != None:
                lista_final += [nodo.__str__()]
                nodo = nodo.next
        print(lista_final)

#rPrintL
    def rPrintL(self):
        nodo = self.tail
        lista_final = []
        for i in range(self.length):
            while nodo != None:
                lista_final += [nodo.__str__()]
                nodo = nodo.prev
        print(lista_final)
        
#appe
    def appe(self, value):
        self.length += 1
        if self.head == None: #lista vacia
            self.head = Nodo(valor=value)
            self.tail = self.head
        else:
            temp = self.tail
            nodo = Nodo(valor=value)
            temp.next = nodo
            nodo.prev = temp
            self.tail = nodo

#insert
    def insert(self,value,pos):
        if isinstance(value,int) and isinstance(pos,int):
            if pos > self.length + 1:
                return "Index out of range"
            elif self.head == None: #lista vacia
                self.head = Nodo(valor=value)
                self.tail = self.head
            elif pos == 0:
                new = Nodo(valor=value)
                temp = self.head
                self.head = new
                temp.prev = new
                new.next = temp
            else:
                temp = self.head
                for i in range(pos-1):
                    temp = temp.next
                new = Nodo(valor=value)
                new.prev = temp
                new.next = temp.next
                temp.next = new
                if new.next == None:
                    self.tail = new
                else:
                    new.next.prev = new
                self.length += 1
            self.printL()
        else:
            return "Error"
                            
#del
    def dl(self,valor):
        if isinstance(valor,int):
            nodo = self.head
            check = False
            if self.head.__str__() == valor: #inicio es eliminado
                self.head = None
                self.head = nodo.next
                self.length -= 1
                return self.printL()
            else:
                while nodo.next != None: #elimina los demas
                    if nodo.next.__str__() == valor:            
                        nodo.prev = nodo
                        nodo.next = nodo.next.next #se salta nodo.next (eliminado)
                        check = True
                        break
                    else:
                        nodo.prev = nodo
                        nodo = nodo.next
                self.tail = nodo
                self.length -= 1
                if check == False:
                    return "Elemento no en la lista"
            return self.printL()
        else:
            return "Error"


#dela
##    def dela(self):
        
                
                
        
