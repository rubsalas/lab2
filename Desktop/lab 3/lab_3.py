
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
        self.largo = 0

    def printL(self):
        nodo = self.head
        lista_final = []
        for i in range(self.largo):
            lista_final += [nodo.__str__()]
            nodo = nodo.next
        print(lista_final)

    def rPrintL(self):
        nodo = self.tail
        lista_final = []
        for i in range(self.largo):
            lista_final += [nodo.__str__()]
            nodo = nodo.prev
        print(lista_final)

    def appe(self, value):
        self.largo += 1
        if self.head == None:
            self.head = Nodo(valor = value)
            self.tail = self.head

        else:
            temp = self.tail
            nodo = Nodo(valor = value)
            temp.next = nodo
            nodo.prev = temp
            self.tail = nodo

    def dl(self,valor):
        if isinstance(valor, int):
            nodo = self.head
            if self.head.__str__() == valor: #inicio es eliminado
                self.head = None
                self.head = nodo.next
                self.largo -= 1
                
            elif self.tail.__str__() == valor: #final es eliminado
                self.tail = None
                count = 0
                temp = self.head
                while count != self.largo - 2:
                    count += 1
                    temp = temp.next
                self.tail = temp
                self.largo -= 1

            else:
                temp = nodo.next
                count = 0
                while temp.__str__() != valor and count < self.largo:
                    temp = temp.next
                    count +=1
                if temp.__str__() == valor and count < self.largo:
                    nodo.next = temp.next
                    nodo = temp.next
                    nodo.prev = temp
                    self.largo -= 1
                else:
                    return "Valor no registrado"
                


    def dela(self,valor):
        nodo=self.head
        
