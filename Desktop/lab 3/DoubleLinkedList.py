class Nodo:
     #E: valor para el nodo de la lista, inicialmente es ninguno.
     def __init__(self, next = None, prev = None, valor = None):
          self.next = next
          self.prev = prev
          self.valor = valor
class ListaDoble:
     def __init__(self):
          self.head = None
          self.tail = None
          self.largo = 0
     #E: -
     #S: la lista mostrada
     #R: 
     def printL(self):
          nodo = self.head
          print('[', end = '')
          if nodo !=None:
               print(nodo.valor, end='')
               nodo = nodo.next
          while nodo != None:
               print(',' , nodo.valor, end = '')
               nodo = nodo.next
          print(']')
     #E: número
     #S: la lista con el dato indicado al final
     #R: Que el dato sea un número
     def appe(self, dato):
          if isinstance(dato, int):
               self.largo += 1
               tmp = self.head
               tail = self.head
               if self.head == None:
                    self.head = Nodo(valor = dato)
                    self.tail = Nodo(valor = dato)
               else:
                    while tmp.next != None:
                         tmp = tmp.next
                         tail = tmp.next
                    tmp.next = Nodo(valor = dato, prev = tmp)
                    self.tail = Nodo(valor = dato, prev = tmp)
          else:
               print('Error')
     #E: -
     #S: la lista mostrada al revés
     #R: 
     def rPrintL(self):
          nodo = self.tail
          print('[', end = '')
          if nodo != None:
               print(nodo.valor, end='')
               nodo = nodo.prev
          while nodo != None:
               print(',' ,str(nodo.valor), end = '')
               nodo = nodo.prev
          print(']')
     #E: valor
     #S: la lista con el valor indicado eliminado una vez
     #R: que la lista no esté vacía
     def dele(self, valor):
          head = self.head
          var = False
          if head == None:
               return 'La lista está vacía'
          elif valor == head.valor:
               self.head = (self.head).next
          else:
               while head.next != None:
                    if valor == head.next.valor:
                         head.prev =  head
                         head.next = (head.next).next
                         var = True
                         break
                    else:
                          head.prev = head
                          head = head.next
               self.tail = head
               if var == False:
                    return 'El elemento no se encuentra en la lista'
            
     # E: Dato y posición
     # S: Lista cambiada
     # R: Posicion debe ser menor al largo
     def insertar(self, dato, pos):
        if isinstance(dato, int) and pos <= self.largo:
            i = 0
            tmp = self.head
            if self.head == None:
                self.largo+=1
                self.head = Nodo(valor = dato)
                self.tail = Nodo(valor = dato)
            else:
                tmp = self.head
                if pos == 0:
                    self.largo+=1
                    self.head = Nodo(valor = dato, next = tmp)
                elif pos == self.largo:
                    self.appe(dato)
                else:
                    self.largo += 1
                    while i != pos:
                        i += 1
                        tmp = tmp.next
                    nuevo_nodo = Nodo(prev = tmp.prev, next = tmp, valor = dato)
                    (tmp.prev).next = nuevo_nodo
                    tmp.prev = nuevo_nodo          
        else:
            print("Error") 
          
