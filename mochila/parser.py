import sys
import csv
import os
from bag import *
import timeit

def read_data(data):
	"""leer_datos se encarga de leer una linea de un archivo csv, mientras lea devuelve el proximo, 
	una vez que alcanza la ultima linea, devuelve None"""
	try:
		return data.next()
	except StopIteration:
		return None 

def open_file(name ,mode='r'):
	"""Funcion que abre un archivo y valida especificamente los errores de que no exista o no tenga permiso"""
	try:
		return open(name,mode)
	except IOError, e:
		print "Error while opening the file"
	return None

def open_csv(fil):
	"""Funcion que devuelve un reader de csv, que en caso de que devuleva error lo muestra y devuelve None"""
	try:
		return csv.reader(file)
	except csv.Error:
		print "File doesn't have the correct format"
		return None

def parse_bag_file(csv_file):
	line = 1
	while line != None:	

		items = []
		values = []
		weights = []
		
		line = read_data(csv_file)
		l = read_data(csv_file)
		try:
			a = int(l[0].split()[1])
		except Exception, e:
			break
		n = int(l[0].split()[1])
		c = int(read_data(csv_file)[0].split()[1])
		z = int(read_data(csv_file)[0].split()[1])
		time = float(read_data(csv_file)[0].split()[1])
		line = read_data(csv_file)
		while line and not line[0] == '-----':
			num_item,valor,peso,x = line
			num_item,valor,peso,x = [int(num_item),int(valor),int(peso),int(x)]
			items.append(num_item)
			values.append(valor)
			weights.append(peso)
			line = read_data(csv_file)

		line = read_data(csv_file)
		#print(n, c)

		def problem():
			return problema_mochila(n, c, weights, values, items)

		print(timeit.timeit(problem, number=1))
		#print(optimum, z)

def parse(fileName):
	with open(fileName, 'rb') as f:
	    reader = csv.reader(f)
	    parse_bag_file(reader)

if __name__ == '__main__':
	parse('../../smallcoeff_pisinger/knapPI_9_50_1000.csv')