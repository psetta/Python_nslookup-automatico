# -*- coding: utf-8 -*-

import socket
import sys
import os
import re

ip = sys.argv[1]
ip_final = sys.argv[2]
	
ip = ip.split(".")
ip_final = ip_final.split(".")

lista_ips = []
lista_nomes = []

print "Procesando..."

while not ip == ip_final:
	lista_ips.append(".".join(ip))
	if "255" in ip:
		for i in range(1,4):
			if ip[i] == "255":
				ip[i] = "0"
				ip[i-1] = str(int(ip[i-1])+1)
	else:
		ip[3] = str(int(ip[3])+1)
		
lista_nomes = []
		
for ip in lista_ips:
	try:
		lista_nomes.append(socket.gethostbyaddr(ip)[0])
	except:
		lista_nomes.append(None)
	
print "\nResultados:"


	
for ip,nome in zip(lista_ips,lista_nomes):
	if nome:
		print ip, "-", nome