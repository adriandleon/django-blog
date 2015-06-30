# Algoritmos para el cajero de Pedro Riquel

caja = [[100, 7], [50, 0], [20, 34], [10, 11], [5, 0], [2, 1]]

# Pocos Billetes: Le da prioridad a los billetes de alta denominacion
def pocos(cantidad):
	
	if cantidad <= total:
		resultado = []

		for valor in caja:
			if cantidad >= valor[0]:
				temp = cantidad % valor[0]
				billetes = int((cantidad - temp) / valor[0])
				if billetes <= valor[1]:
					cantidad -= billetes * valor[0]
					resultado.append([valor[0], billetes])
				else:
					cantidad -= valor[1] * valor[0]
					resultado.append([valor[0], valor[1]])
			else:
				resultado.append([valor[0], 0])

		if cantidad > 0:
			print('Sobran ' + str(cantidad) + ' Bs.')
		return resultado
	else:
		return 'No hay suficiente dinero en la caja. ' + str(total) + ' Bs.'

# Muchos Billetes: Le da prioridad a los billetes de baja denominacion

# Aleatorio: Realiza una selección de billetes aleatoriamente

# Total: Calcular el total que hay en la caja
def total(caja):
	cant = 0
	for billete in caja:
		cant += billete[0] * billete[1]
	return cant


######################################

total = total(caja)

print(pocos(160000))

