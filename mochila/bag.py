def problema_mochila(nro_de_elementos,capacidad,lista_pesos,lista_valores,lista_idrs):
	"""Funcion que dado una cantidad de elementos con sus pesos,valores e identificadores y una capacidad
	de mochila maxima, calcula la solucion optima que llena la mochila con el mayor valor total. Ademas devuelve
	una lista con todos las ids de los elementos que componen la solucion."""
	# Inicializo una matriz de "capacidad" filas y "nro_de_elementos" columnas con una lista
	# que contiene un cero y una lista vacia cada posicion de la matriz.
	matriz = [[ [0,[]] for x in xrange(nro_de_elementos+1)] for x in xrange(capacidad+1)]
	for j in xrange(1,capacidad+1): # Cada ciclo aumenta la capacidad de la mochila
		for i in xrange(1,nro_de_elementos+1): # Cada ciclo aumenta la cantidad de elementos considerados
			peso = lista_pesos[i-1]
			valor = lista_valores[i-1]
			idr = lista_idrs[i-1]
			if peso > j:
				matriz[j][i][0] = matriz[j][i-1][0]
				matriz[j][i][1] = matriz[j][i-1][1]
			if peso <= j:
				if matriz[j][i-1][0] >= (matriz[j-peso][i-1][0] + valor):
					matriz[j][i][0] = matriz[j][i-1][0]
					matriz[j][i][1] = matriz[j][i-1][1]
				else:
					matriz[j][i][0] = (matriz[j-peso][i-1][0] + valor)
					matriz[j][i][1] = list(matriz[j-peso][i-1][1]) # Esto crea una nueva lista igual a la anterior
					matriz[j][i][1].append(idr) # Agrego el idr del elemento que ahora es parte de la mejor solucion parcial
	return matriz[capacidad][nro_de_elementos][0],matriz[capacidad][nro_de_elementos][1]