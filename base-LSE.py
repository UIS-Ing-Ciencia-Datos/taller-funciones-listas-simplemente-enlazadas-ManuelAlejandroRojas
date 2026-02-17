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



	#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
	#Manuel Rojas Changes
	#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

	#Contar cuantos elementos tiene la lista
	def Contar_cuantos_elementos_tiene_la_lista(self):
		CantidadElementos = 0
		NodoActual = self.cabeza
		while NodoActual != None:
			CantidadElementos+=1
			NodoActual = NodoActual.siguiente
		
		print(CantidadElementos)


	#Encontrar un elemento por su valor
	def Buscar_si_hay_un_elemento(self, valor):
		NodoActual = self.cabeza
		while NodoActual != None:
			if NodoActual == valor:
				print("El valor si está en la lista --> Verdadero")
				return True
			
			else:
				NodoActual = NodoActual.siguiente

			if NodoActual == None:
				print("Falso, el valor no está en la lista")
				return False
			

