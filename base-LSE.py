# ===========================================
# By: Nury Farelo - Estructuras Datos
# Name: Lista Simplemente Enlazada 
# ===========================================

# Clase Nodo
class Nodo:
	def __init__(self, data):
		self.data = data
		self.siguiente = None

# CLase Listas enlazada simple
class ListaSE:
	def __init__(self):
		self.cabeza = None
  
  	# Lista Vacia
	def vacio(self):
		if self.cabeza == None:
			print("Está vacia")
		else:
			print("Lista no vacia")

	# Agregar al inicio
	def agregarInicio(self, data):
		nuevo_nodo = Nodo(data)
		if self.cabeza is None:
			self.cabeza = nuevo_nodo
			return
		else:
			nuevo_nodo.siguiente = self.cabeza
			self.cabeza = nuevo_nodo

	#Contar cuantos elementos tiene la lista
	def Contar_cuantos_elementos_tiene_la_lista(self):
		CantidadElementos = 0
		NodoActual = self.cabeza
		while NodoActual != None:
			CantidadElementos+=1
			NodoActual = NodoActual.siguiente
		
		print("hay ", CantidadElementos, " elementos en la lista")


	#Encontrar un elemento por su valor
	def Buscar_si_hay_un_elemento(self, valor):
		NodoActual = self.cabeza
		while NodoActual is not None:
			if NodoActual.data == valor:
				print("El valor si está en la lista --> Verdadero")
				return True
			
			else: 
				NodoActual = NodoActual.siguiente	

		
		print("Falso, el valor no está en la lista")
		return False
				
			
	#Eliminar el último elemento de la lista
	def Eliminar_ultimo_elemento(self):
		NodoActual = self.cabeza
  
		if NodoActual == None:
			print("La lista está vacía, no se puede eliminar nada")   #Comprobar lista vacía(Por si acaso xd)
			return


		elif NodoActual.siguiente == None:   #Si la lista tiene un solo elemento lo elimino y queda vacía
			self.cabeza = None
			print("Se eliminó el único elemento, la lista quedó vacía")
   
			return

		while NodoActual.siguiente.siguiente != None: #Busco el siguiente del siguiente pa llegar al penúltimo
			NodoActual = NodoActual.siguiente     #Avanzo uno

		NodoActual.siguiente = None   #Le cambio el apuntador del penúltimo a nada y el último desaparece mujejeje
		print("Se eliminó el último elemento de la lista")
	
	#Eliminar el primer elemento de la lista ---> Pero sin que se borre toda la lista, claro JAJAJA
	def Eliminar_primer_elemento(self):
		
		if self.cabeza is None:
			print("Lista vacía")
			return
        
		self.cabeza = self.cabeza.siguiente  #Reemplazo lo que hay actualmente en la cabeza por lo que hay en el apuntador de la misma, el primero, desaparece
		print("Se eliminó el primer elemento de la lista")

	#Insertar un elemento después de un elemento random
	def Insertar_despues_de_un_elemento_especifico(self, ValorAgregar, valorX):
		
		Nodo_a_insertar = Nodo(ValorAgregar)

		NodoActual = self.cabeza
		if NodoActual is not None:
			while True:
				if NodoActual is None:
					print("El valor no se encuentra en la lista")
					return			
    
				if NodoActual.data == valorX:
					Nodo_a_insertar.siguiente = NodoActual.siguiente
					NodoActual.siguiente = Nodo_a_insertar
					break
				else:	
					NodoActual = NodoActual.siguiente
			
			print("Se insertó: '", ValorAgregar, "' después del elemento: ", valorX)
		else:
			print("Lista vacía")
			return
			
   
	#Insertar antes de un elemento random
	def Insertar_antes_de_un_elemento_especifico(self, ValorAgregar, ValorX):

		if self.cabeza is None: #Comprobar si la lista está vacía
			print("Lista vacía")
			return


		if self.cabeza.data == ValorX:      #En caso de insertar antes del primero
			self.agregarInicio(ValorAgregar)
			print("Se insertó: '", ValorAgregar, "' antes del elemento: ", ValorX)
			return

		NodoActual = self.cabeza

		while NodoActual.siguiente is not None:

			if NodoActual.siguiente.data == ValorX:
				Nodo_a_insertar = Nodo(ValorAgregar)
				Nodo_a_insertar.siguiente = NodoActual.siguiente
				NodoActual.siguiente = Nodo_a_insertar

				print("Se insertó: '", ValorAgregar, "' antes del elemento:", ValorX)
				return
			else:
				NodoActual = NodoActual.siguiente
			
		print("El valor no se encuentra en la lista")


	def Insertar_al_final(self, ValorAgregar):
		Nodo_a_insertar = Nodo(ValorAgregar)
		if self.cabeza is None:
			self.cabeza = Nodo_a_insertar
			print("Se insertó:", ValorAgregar, "al final de la lista")
			return
		
		
		NodoActual = self.cabeza
		while NodoActual.siguiente is not None:
			NodoActual = NodoActual.siguiente

		NodoActual.siguiente = Nodo_a_insertar
		print("Se insertó:", ValorAgregar, "al final de la lista")
  

	def mostrar_lista(self):
		NodoActual = self.cabeza
		while NodoActual is not None:
			print("--", NodoActual.data)
			NodoActual = NodoActual.siguiente
		print("None")	
	
 






Lista1 = ListaSE()

#Se crea lista con la cabeza vacía
# Lista1: [None]

print("Lista creada")
print("La lista está vacia?")
Lista1.vacio()

#Entonces agregaré un valor
Lista1.agregarInicio("ShiningStar")

#Se crea un "nodo" un cubito con el valor proporcionado y que sabe que hay una caracteristica llamada "siguiente" con un valor "Nada"
#Se agrega a a lista directamente por que no hay nada al inicio
# [ShiningStar -> Nada]

Lista1.agregarInicio("Ama a")

#Se crea un "nodo" nuevo, un cubito con el valor proporcionado y que sabe que hay una caracteristica llamada "siguiente" con un valor "Nada"
#Pero como queremos agregarlo al inicio, no puede tener "nada" tendría que tener como característica "siguiente" el valor del que pusimos antes 
#Entonces el nodo que queremos agregar recibe el anterior como "siguiente", lo que reemplaza el "Nada" que tenía, así se dice que se "agregó" al principio
#Se agrega a la lista haciendole entender al código que lo que entiende como "cabeza" es este nuevo nodo
# [ShiningStar -> Nada] se convierte en: [Ama a --> ShiningStar --> Nada]

Lista1.agregarInicio("FlamaOscura")
#Misma lógica

#Verificamos que no esté vacía
print("Lista creada")
print("La lista está vacia?")
Lista1.vacio()
 
#Busquemos si está "Ama a"
Lista1.Buscar_si_hay_un_elemento("Ama a")

#Cuantos elementos tiene la lista?
Lista1.Contar_cuantos_elementos_tiene_la_lista()

#Agreguemos al final
Lista1.Insertar_al_final("Un Random")
# [FlamaOscura --> Ama --> ShiningStar --> Un Random --> Nada]

#Agreguemos antes de un elemento random
Lista1.Insertar_antes_de_un_elemento_especifico("Hay" , "Un Random")
# [FlamaOscura --> Ama --> ShiningStar --> Hay --> Un Random --> Nada

#Quitemos los ultimos elementos
Lista1.Eliminar_ultimo_elemento()
# [FlamaOscura --> Ama --> ShiningStar --> Hay --> Nada]

Lista1.Eliminar_ultimo_elemento()
# [FlamaOscura --> Ama --> ShiningStar --> Nada]

#mostremos la lista
Lista1.mostrar_lista()