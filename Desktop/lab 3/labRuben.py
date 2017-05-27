class Nodo:
    def __init__(self, next = None, prev = None, valor = None):
        self.next = next
        self.prev = prev
        self.valor = valor

    def __str__(self):
        return self.valor
        
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
##        self.printL()




#insert
##    def insert(self,valor,pos):
        

        
#del
    def dl(self,valor):
        if isinstance(valor,int):
            nodo = self.head
            if self.head.__str__() == valor: #inicio es eliminado
                self.head = None
                self.head = nodo.next
                self.length -= 1
                return self.printL() #3
                
##            elif self.tail.__str__() == valor: #final es eliminado
##                self.tail = None
##                count = 0
##                temp = self.head
##                while count != self.length - 2:
##                    count += 1
##                    temp = temp.next
##                self.tail = temp
##                self.length -= 1
##                return self.printL()

            else:
                while nodo.next != None:
                    if nodo.next.__str__() == valor:            
                        nodo.prev = nodo
                        nodo.next = nodo.next.next #se salta al nodo.next que seria el que va a ser eliminado
                        break
                    else:
                        nodo.prev = nodo
                        nodo = nodo.next
                self.tail = nodo
                self.length -= 1
##                if 
            return self.printL()





#################################
    def delete(self,valor):
        nodo = self.head #head
        var = False
        if nodo == None:
            return "Lista vacia"
        elif self.head.__str__() == valor: #head.valor
            self.head = None
            self.head = nodo.next
            self.length -= 1
        else:
            while nodo.next != None:
                if valor == nodo.next.__str__(): 
                    nodo.prev = nodo
                    nodo.next = nodo.next.next #se salta al nodo.next que seria el que va a ser eliminado
                    var = True
                    break
                else:
                    nodo.prev = nodo
                    nodo = nodo.next
            self.tail = nodo
            if var == False:
                return "Elemento no en la lista"
        self.printL()
################################


#dela
##    def dela(self):
        
                
                
        




    
#lista predefinida
l = ListaDoble()

l.appe(1)
l.appe(3)
l.appe(6)
l.appe(9)
l.appe(12)
l.appe(15)
l.appe(18)

l.printL()

print("Head:", l.head.__str__())

print("Tail:", l.tail.__str__())
