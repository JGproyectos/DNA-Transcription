"""
Nombres: Gaspar Hermán Sandoval, Jesus Marcano Carnets: 13-10637, 12-10359

Descripcion: Proyecto I Algoritmos y Estructuras II
"""
# Importando modulos necesarios
import sys
import time

# Definiendo esta mitosis para su uso más adelante
def mitosis1(arreglo):
	# Lo primero que hay que hacer es separar en dos cadenas la cadena actual usando unzip
	simple1 = []  # Se almacenará aquí una mitad de la cadena doble
	simple2 = []  # Se almacenará aquí la otra mitad de la cadena doble de entrada

	try:
		# Precondicion
		assert(all(isinstance(arreglo[i],tuple)) for i in range(len(arreglo)))

	except AssertionError:
			print("hubo un error leyendo datos. Por favor revise")
			sys.exit()	

	for i in range(len(arreglo)):
		for j in range(2):  # Esto es debido a que es un arreglos de tuplas de dos elementos
			if j % 2 == 0:
				simple1.append(arreglo[i][j])

			else:
				simple2.append(arreglo[i][j])

	# Postcondicion
	assert(len(simple1) == len(simple2) and (len(arreglo) == len(simple2)))

	# Ahora hay que buscar el complemento de cada una usando el método de complementar
	complemento_para1 = []  # Se guarda el complemento para simple1
	complemento_para2 = []  # Se guarda el complemento para simple2

	# Hay que recorrer todo el arreglo para conocer cual es el complemento
	# Para simple1
	for base in range(len(simple1)):
		if simple1[base] == "A":
			complemento_para1.append("T")

		elif simple1[base] == "T":
			complemento_para1.append("A")

		elif simple1[base] == "G":
			complemento_para1.append("C")

		else:
			complemento_para1.append("G")	

	# Postcondicion
	assert(len(complemento_para1) == len(simple1))

	# Para simple2
	for base in range(len(simple1)):
		if simple2[base] == "A":
			complemento_para2.append("T")

		elif simple2[base] == "T":
			complemento_para2.append	("A")

		elif simple2[base] == "G":
			complemento_para2.append("C")

		else:
			complemento_para2.append("G")	

	# Postcondicion
	assert(len(complemento_para2) == len(simple2))

	"""
	Ahora que tenemos simple1 y su complemento al igual que simple2 y su complemento
	buscaremos convertir ambas en una sola cadena usando zip.
	"""

	# Para 1
	cadena_final1 = []  # Almacenamos los complementos de la cadena dada junto a su original

	# Crearemos la doble
	for i in range(len(complemento_para1)):
		temporal = (simple1[i],complemento_para1[i])  # Almacenamos la cadena original y el complemento
		cadena_final1.append(temporal)

	# Postcondicion
	assert(len(cadena_final1) == len(complemento_para1))

	# Para 2
	cadena_final2 = []  # Almacenamos los complementos de la cadena dada junto a su original

	# Crearemos la doble
	for i in range(len(complemento_para2)):
		temporal = (simple2[i],complemento_para2[i])  # Almacenamos la cadena original y el complemento
		cadena_final2.append(temporal)

	# Postcondicion
	assert(len(cadena_final2) == len(complemento_para2))

	return (cadena_final1,cadena_final2)

def borrar_espacios(x:str)->list:  # Funcion que carga una lista en un arreglo y quita el "\n"
	y = []  # lista vacia donde se almacenará todo

	# Se carga un archivo de texto que contenga la información necesaria de los productos
	with open(x,'r') as f:
		datos = f.readlines()  # Almacenamos todos los datos del archivo aquí

	for line in datos:  # Colocamos cada línea del archivo dentro del arreglo
		y.append(line)

	# Eliminamos el "\n" de cada elemento del arreglo
	for i in range(len(y)):
		y[i] = y[i].replace("\n","")

		if y[i].isnumeric():  # En caso de tener un número tratado como texto se convierte en un número
			y[i] = int(y[i])

		# Invariante
		assert(all(y[i] == y[i].replace("\n","")) for i in range(len(y)))	  

	return y

"""
Esta funcion tiene una particularidad curiosa: La idea consiste en sacar una cadena de ADN simple de un texto y 
convertira en doble. La idea consiste en usar el metodo zip que fue programado antes de esta función, aquí el detalle,
la cadena simple que se quiera convertir en doble, antes de eso debe convertirse en un objecto ADNdoble, luego
se llama al método ADNdoble.zip([]). ¿Por qué []?. Por detalles en la especificación se colocó que el método recibe una cadena.
Es más fácil de arreglar convirtiendo dicha cadena en un objeto y llamar al método que cambiar todos los métodos.
"""

def lectura_archivo(archivo):
	primera_lista = borrar_espacios(archivo)  # Aquí se guardará cada linea en un arreglo sin el "\n"

	lista_salida1 = []

	"""
	Aquí se almacenan listas, cada lista es una cadena de ADN, cuyos elementos están separados por comas.
	Además se iterará a lo largo de la primera_lista y luego a lo largo de cada elemento en dicha lista para
	que se agregue a la lista de salida.
	"""

	for i in range(len(primera_lista)):
		lista_temporal = []  # En esta lista se guardarán los elementos a agregar a lista_salida

		for j in range(len(primera_lista[i])):
			lista_temporal.append(primera_lista[i][j])

		lista_salida1.append(lista_temporal)  # Agregamos la cadena separa por comas en esta lista al salir de la iteración

	for i in range(len(lista_salida1)):
		lista_salida1[i] = ADNdoble(lista_salida1[i])
		lista_salida1[i] = lista_salida1[i].zip([])

	return lista_salida1	

# Definiendo la variable donde se almacenarán los ADN basura
global ADNbasura
ADNbasura = []

# Creando las clases
class ADNsimple():
	def __init__(self,cadena):
		self.size = len(cadena)
		self.cadena = cadena
		self.complemento = []  # Se almacenarán aquí los complementos

	# Metodos	
	def complementar(self):  # Genera la cadena complemento
		# Precondicion
		try:

			assert(all(isinstance(self.cadena[i],str) for i in range(self.size)))

		except AssertionError:
			print("hubo un error leyendo los datos")
			sys.exit()	

		# Hay que recorrer todo el arreglo para conocer cual es el complemento
		for base in range(self.size):
			if self.cadena[base] == "A":
				self.complemento.append("T")

			elif self.cadena[base] == "T":
				self.complemento.append	("A")

			elif self.cadena[base] == "G":
				self.complemento.append("C")

			else:
				self.complemento.append("G")	

		# Postcondicion
		assert(len(self.complemento) == self.size)
		return self.complemento

	def transcribir(self):
		# Hacemos el llamado del método para complementar
		ARN = self.complementar()

		# Realizamos el cambio de la Timina por Uralcio, para esto hay que recorrer todo el arreglo
		for i in range(len(ARN)):
			if ARN[i] == "T":
				ARN[i] = "U"

		ARN = ARNt(ARN)  # Convertimos nuestro ARN en un objeto de la clase ARNt para que tenda todos sus métodos y lo retornamos
		return ARN

class ADNdoble(ADNsimple):
	def __init__(self,cadena):
		self.nueva_cadena = []  # Aquí se almacenará la cadena doble completa
		self.size = len(cadena)
		self.cadena = cadena  # Cadena simple
		self.complemento = []  # Se almacenarán aquí los complementos
		self.simple1 = []  # Se almacena una simple para el proceso unzip
		self.simple2 = []  # Se almacena la otra simple para el proceso de unzip
		self.simple_doble1 = []  # Para almacenar datos una vez hecha la mitosis
		self.simple_doble2 = []  # Para almacenar datos una vez hecha la mitosis

	def zip(self,cadena):  # Crea una cadena doble a partir de una simple
		el_complemento = self.complementar()  # Almacenamos los complementos de la cadena dada
		cadena_final = []  # Se almacena aquí la cadena ya creada

		# Crearemos la doble
		for i in range(len(self.complemento)):
			temporal = (self.cadena[i],el_complemento[i])  # Almacenamos la cadena original y el complemento
			self.nueva_cadena.append(temporal)

		# Postcondicion
		assert(len(self.nueva_cadena) == len(self.complemento))
		cadena_final = self.nueva_cadena
		return cadena_final

	def unzip(self):  # Funcion para separar las cadenas de ADN
		try:
			# Precondicion
			assert(all(isinstance(self.nueva_cadena[i],tuple)) for i in range(len(self.nueva_cadena)))

		except AssertionError:
			print("hubo un error leyendo datos. Por favor revise")
			sys.exit()	

		for i in range(self.size):
			for j in range(2):  # Esto es debido a que es un arreglos de tuplas de dos elementos
				if j % 2 == 0:
					self.simple1.append(self.nueva_cadena[i][j])

				else:
					self.simple2.append(self.nueva_cadena[i][j])

		# Postcondicion
		assert(len(self.simple1) == len(self.simple2) and (self.size == len(self.simple2)))

		"""
		Como simple1 y simple 2 son atributos del objeto ADNdoble no hay necesidad de hacerles un return.
		En caso de querer acceder a estas listas, sólo hay que hacer un llamado simple al atributo, además
		de esta manera es posible usar los mismos atributos para el proceso de mitosis.
		"""	

	def mitosis(self):

		"""
		Se debe hacer un llamado a una función externa que haga todo el proceso de mitosis.
		La idea original era usar todos los metodos disponibles hasta el momento y fusionarlos 
		de forma tal que fuera posible hacer una mitosis. El problema recae en la forma de llamar 
		los métodos, la cual hace que se sobreescriba información, cosa que no se quiere.
		"""

		if len(self.nueva_cadena) != 0:
			cadena_a_separar = self.nueva_cadena			

			# Llamamos a la funcion
			salida = mitosis1(cadena_a_separar)

			# Guardamos esto como atributos del objeto
			self.simple_doble1 = salida[0]
			self.simple_doble2 = salida[1]

		else:
			print("no hay cadenas disponibles, por favor intentelo de nuevo")
			sys.exit()

	def busqueda(self,cadena):
		# Precondicion
		try:
			assert(len(cadena) <= len(self.nueva_cadena) and (len(self.nueva_cadena) > 0))

		except AssertionError:	
			print("Hubo uno de dos posibles errores:")
			print("1) la cadena a buscar es más grande que la que se tiene")
			print("2) aún no se usa el método de crear una cadena doble de ADNdoble, por favor hagalo")
			print("abortando en:")
			print(3)
			time.sleep(1)
			print(2)
			time.sleep(1)
			print(1)
			time.sleep(1)
			print(0)
			sys.exit()

		# Declaración de variables iniciales del proceso
		cadena_original = self.nueva_cadena
		cadena_simple1 = []  # Aquí almacenamos una parte de la cadena original
		cadena_simple2 = []  # Aquí almacenamos la otra parte de la cadena original

		for i in range(len(cadena_original)):
			for j in range(2):  # Esto es debido a que es un arreglos de tuplas de dos elementos
				if j % 2 == 0:
					cadena_simple1.append(cadena_original[i][j])

				else:
					cadena_simple2.append(cadena_original[i][j])

		# Postcondicion
		assert(len(cadena_simple1) == len(cadena_simple2) and (len(cadena_original) == len(cadena_simple1)))

		complemento_buscar = []  # Almacenamos el complemento de la sub cadena simple aquí

		# Hay que recorrer todo el arreglo para conocer cual es el complemento
		# Un método de ADNsimple más generalizado
		for base in range(len(cadena)):
			if cadena[base] == "A":
				complemento_buscar.append("T")

			elif cadena[base] == "T":
				complemento_buscar.append	("A")

			elif cadena[base] == "G":
				complemento_buscar.append("C")

			else:
				complemento_buscar.append("G")	

		# Postcondicion
		assert(len(complemento_buscar) == len(cadena))

		# Para hacer la busqueda más simple	
		variable = ""  # Aquí se colocará todo el string

		cadena_simple1 = variable.join(cadena_simple1)

		variable = ""  # Reiniciamos

		cadena_original = variable.join(cadena_simple2)

		variable = ""  # Reiniciamos

		complemento_buscar = variable.join(complemento_buscar)

		variable = ""  # Reiniciamos

		cadena_a_buscar = variable.join(cadena)

		Existencia = False  # Almacenamos si está o no la cadena dentro de la otra, por defecto estará en False

		if (cadena_a_buscar in cadena_simple1) or (cadena_a_buscar in cadena_simple2) or (complemento_buscar in cadena_simple1)\
		or (complemento_buscar in cadena_simple2):
			Existencia = True

		if Existencia:
			print("la subcadena pasada, si existe dentro de la cadena doble")

		else:
			print("la subcadena pasada no existe dentro de la cadena doble")		



	def imprimir(self):
		print(self.nueva_cadena)

class Proteina():
	def __init__(self,cadena):
		self.cadena = cadena
		self.codones_existentes = ["AUG","UUU","UUC","UUA","UUG","CUU","CUC","CUA","CUG","AUU","AUC","AUA","GUU","GUC","GUA","GUG",\
		"UCU","UCC","UCA","UCG","CCU","CCC","CCA","CCG","ACU","ACC","ACA","ACG","GCU","GCC","GCA","GCG","UAU","UAC","CAU","CAC",\
		"CAA","CAG","AAU","AAA","AAG","GAU","GAC","GAA","GAG","UGU","UGC","UGG","CGU","CGC","CGA","CGG","AGU","AGC","AGA","AGG",\
		"GGU","GGC","GGA","GGG","UAG","UAA","UGA"]
		self.proteina = []  # Se almacenará aquí la proteína sintetizada

	def sintetizar(self):
		abreviacion_proteinas = ["Met","Phe","Leu","Ile","Val","Ser","Pro","Thr","Ala","Tyr","His","Gln","Asn",\
		"Lys","Asp","Glu","Cys","Trp","Arg","Gly"]

		"""
		Iniciamos una iteración a lo largo de la cadena que se pasó de argumento, comparando uno a uno sus elementos,
		en base a los resultados le asignaremos un valor de la lista abreviaciom_proteinas a self.proteina
		"""
		for i in range(len(self.cadena)):

			if self.cadena[i] == self.codones_existentes[0]:
				self.proteina.append(abreviacion_proteinas[0])

			elif self.cadena[i] == self.codones_existentes[1] or self.cadena[i] == 	self.codones_existentes[2]:
				self.proteina.append(abreviacion_proteinas[1])

			elif self.cadena[i] == self.codones_existentes[3] or self.cadena[i] == self.codones_existentes[4] or \
			self.cadena[i] == self.codones_existentes[5] or self.cadena[i] == self.codones_existentes[6] or \
			self.cadena[i] == self.codones_existentes[7] or self.cadena[i] == self.codones_existentes[8]:
				self.proteina.append(abreviacion_proteinas[2])

			elif self.cadena[i] == self.codones_existentes[9] or self.cadena[i] == self.codones_existentes[10] or\
			self.cadena[i] == self.codones_existentes[11]:
				self.proteina.append(abreviacion_proteinas[3])

			elif self.cadena[i] == self.codones_existentes[12] or self.cadena[i] == self.codones_existentes[13] or\
			self.cadena[i] == self.codones_existentes[14] or self.cadena[i] == self.codones_existentes[15]:
				self.proteina.append(abreviacion_proteinas[4])

			elif self.cadena[i] == self.codones_existentes[16] or self.cadena[i] == self.codones_existentes[17] or\
			self.cadena[i] == self.codones_existentes[18] or self.cadena[i] == self.codones_existentes[19] or\
			self.cadena[i] == self.codones_existentes[53] or self.cadena[i] == self.codones_existentes[54]:
				self.proteina.append(abreviacion_proteinas[5])

			elif self.cadena[i] == self.codones_existentes[20] or self.cadena[i] == self.codones_existentes[21] or\
			self.cadena[i] == self.codones_existentes[22] or self.cadena[i] == self.codones_existentes[23]:
				self.proteina.append(abreviacion_proteinas[6])

			elif self.cadena[i] == self.codones_existentes[24] or self.cadena[i] == self.codones_existentes[25] or\
			self.cadena[i] == self.codones_existentes[26] or self.cadena[i] == self.codones_existentes[27]:
				self.proteina.append(abreviacion_proteinas[7])	

			elif self.cadena[i] == self.codones_existentes[28] or self.cadena[i] == self.codones_existentes[29] or\
			self.cadena[i] == self.codones_existentes[30] or self.cadena[i] == self.codones_existentes[31]:
				self.proteina.append(abreviacion_proteinas[8])

			elif self.cadena[i] == self.codones_existentes[32] or self.cadena[i] == self.codones_existentes[33]:
				self.proteina.append(abreviacion_proteinas[9])

			elif self.cadena[i] == self.codones_existentes[34] or self.cadena[i] == self.codones_existentes[35]:
				self.proteina.append(abreviacion_proteinas[10])

			elif self.cadena[i] == self.codones_existentes[36] or self.cadena[i] == self.codones_existentes[37]:
				self.proteina.append(abreviacion_proteinas[11])

			elif self.cadena[i] == self.codones_existentes[38] or self.cadena[i] == self.codones_existentes[39]:
				self.proteina.append(abreviacion_proteinas[12])

			elif self.cadena[i] == self.codones_existentes[40] or self.cadena[i] == self.codones_existentes[41]:
				self.proteina.append(abreviacion_proteinas[13])

			elif self.cadena[i] == self.codones_existentes[42] or self.cadena[i] == self.codones_existentes[43]:
				self.proteina.append(abreviacion_proteinas[14])

			elif self.cadena[i] == self.codones_existentes[44] or self.cadena[i] == self.codones_existentes[45]:
				self.proteina.append(abreviacion_proteinas[15])

			elif self.cadena[i] == self.codones_existentes[46] or self.cadena[i] == self.codones_existentes[47]:
				self.proteina.append(abreviacion_proteinas[16])

			elif self.cadena[i] == self.codones_existentes[48]:
				self.proteina.append(abreviacion_proteinas[17])

			elif self.cadena[i] == self.codones_existentes[49] or self.cadena[i] == self.codones_existentes[50] or\
			self.cadena[i] == self.codones_existentes[51] or self.cadena[i] == self.codones_existentes[52] or\
			self.cadena[i] == self.codones_existentes[55] or self.cadena[i] == self.codones_existentes[56]:
				self.proteina.append(abreviacion_proteinas[18])

			elif self.cadena[i] == self.codones_existentes[57] or self.cadena[i] == self.codones_existentes[58] or\
			self.cadena[i] == self.codones_existentes[59] or self.cadena[i] == self.codones_existentes[60]:
				self.proteina.append(abreviacion_proteinas[19])	
			else:
				print("el elemento no es un triplete hay algún error")  # Esto para poder verificar si no se está cumpliendo algo y revisarlo
				

class ARNt():
	def __init__(self,cadena):
		self.cadena = cadena
		self.final = []  # Este objeto tendrá una cadena vacía para almacenar los aminoacidos que encuentre
		#self.basura = []  # Variable donde almacenaremos ADNbasura
		self.ARNbasura = []  # Variable donde almacenamos ARNbasura


	def traducir(self):
		codon = ""  # Inicializamos aquí la variable que almacenará cada codon luego de una futura iteracion

		# Almacenamos todos los aminoacidos que existen
		codones_existentes = ["AUG","UUU","UUC","UUA","UUG","CUU","CUC","CUA","CUG","AUU","AUC","AUA","GUU","GUC","GUA","GUG",\
		"UCU","UCC","UCA","UCG","CCU","CCC","CCA","CCG","ACU","ACC","ACA","ACG","GCU","GCC","GCA","GCG","UAU","UAC","CAU","CAC",\
		"CAA","CAG","AAU","AAA","AAG","GAU","GAC","GAA","GAG","UGU","UGC","UGG","CGU","CGC","CGA","CGG","AGU","AGC","AGA","AGG",\
		"GGU","GGC","GGA","GGG","UAG","UAA","UGA"]

		frecuencia = []  # Frecuencia en la que aparecen los aminoacidos

		for i in range(len(codones_existentes)):  # Todos están inicialmente en cero
			frecuencia.append(0)

		# Primero formaremos el aminoacido de inicio
		for i in range(3):
			codon = codon + self.cadena[i]

		if codon != codones_existentes[0]:  # En caso de que no tenga codon de iniciacion
			for i in range(len(self.cadena)): # Como nos pide devolver ADN basura entonces hay que devolver el cambio "U", "T"

				if self.cadena[i] == "U":
					self.cadena[i] = "T"	

			#self.basura.append(self.cadena)
			global ADNbasura
			ADNbasura.append(self.cadena)
				
		else:  # Buscamos si es o no es ARN basura
			basura = True # Esta variable servirá para que si al final de esta iteracion sea clasificada o no como basura
			# Inicialmente se asume que es basura

			i = 3  # Variable para trabajar con un ciclo while

			"""
			originalmente se pensaba en un bucle for, pero como no se sabe exactamnte si la cadena de los casos de prueba
			son divisible entre 3, se decidió hacer un bucle while.
			"""

			while i < len(self.cadena):  # Subimos la iteracion de 3 en 3. Esto por la forma en que se hace el aminoacido

				codon = "" # Reiniciamos la variable de codon

				for j in range(i,i+3):  # Para crear el triplete a comparar
					codon = codon + self.cadena[j]

				if (codon == codones_existentes[62]) or (codon == codones_existentes[61]) or (codon == codones_existentes[60]):
					basura = False
					break # Salimos del bucle

				else:  # Agregamos el aminoacido y la frecuencia
					for z in range(len(codones_existentes)):
						if codones_existentes[z] == codon:
							frecuencia[z] = frecuencia[z] + 1  # Agregamos la frecuencia 

					self.final.append(codon)  # Agregamos el elemento a la cadena de codones

				i = i + 3  # Ajustamos la variable de iteracion

			if basura:  # En caso de que haya terminado de iterar y no haya encontrado un aminoácido de culminación
				for i in range(len(self.cadena)): # Como nos pide devolver ADN basura entonces hay que devolver el cambio "U", "T"

					if self.cadena[i] == "U":
						self.cadena[i] = "T"	

				#self.basura.append(self.cadena)
				ADNbasura.append(self.cadena)
				self.ARNbasura.append(self.final)


#Casos de prueba simples con existo
prueba = lectura_archivo("prueba1.txt")
print(prueba[0])
print("\n")
print(prueba[1])
print(prueba[2])
a = ADNdoble(["T","A","G","A"])
a.zip([])
print(a.nueva_cadena)
a.busqueda(["A","T","C"])
print(b)
z = ARNt(["A","U","G","U","U","U","G","A","A","A","A","A","U","G","A"])
z.traducir()
hola = z.final
print(hola)
hola = Proteina(hola)
hola.sintetizar()
hola = hola.proteina
print(hola)
print(z.ARNbasura)
print(z2)
patria = [("T","A"),("A","T"),("G","C")]
vector = mitosis1(patria)	
a.imprimir()
a.unzip()
print(a.simple1)
print(a.simple_doble1)
print(a.simple_doble2)
print(b)
print(z.complementar())	
print(a.simple2)
print(vector[1])
print(vector[0])