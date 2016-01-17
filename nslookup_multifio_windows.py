# -*- coding: utf-8 -*-

import threading
import os
import sys
import re

# SOLO FUNCIONA EN WINDOWS

class Fio(threading.Thread):
	def __init__(self,host):
		super(Fio, self).__init__()
		self.host=host
		self.nome=""
	def run(self):
		try:
			saida_nslookup = os.popen("nslookup "+self.host).read().replace(" ","")
			self.nome = re.findall("Nombre:(.+)",saida_nslookup)[0]
		except:
			pass

print "===================="
print "NSLOOKUP AUTOMATICO"
print "====================\n"

if len(sys.argv) < 3:
	ip = raw_input("Introduce a IP inicial: ")
	ip_final = raw_input("Introduce a IP final: ")
else:
	ip = sys.argv[1]
	ip_final = sys.argv[2]

if not (re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip) or 
	re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip_final)):
	sys.exit("ERROR: IPs mal escritas")
	
ip = ip.split(".")
ip_final = ip_final.split(".")

for i in ip+ip_final:
	if int(i) > 255:
		sys.exit("ERROR: IPs mal escritas")

lista_fios = []

while not ip == ip_final:
	os.system("cls")
	print "Procesando..."
	print "nslookup a",".".join(ip)
	lista_fios.append(Fio(".".join(ip)))
	lista_fios[-1].start()
	if "255" in ip:
		for i in range(1,4):
			if ip[i] == "255":
				ip[i] = "0"
				ip[i-1] = str(int(ip[i-1])+1)
	else:
		ip[3] = str(int(ip[3])+1)
		
	
	
for i in lista_fios:
	i.join()
	
os.system("cls")
print "Resultados:"
	
for i in [i for i in lista_fios if not i.nome == ""]:
	print i.host, "-", i.nome
	
print "\n>> Deseas gardar os Resultados nun documento?"
print "1) Aceptar"

decision = raw_input()

if decision == "1":
	for i in range(100):
		if not os.path.exists("rexistro_host_"+str(i)+".txt"):
			nome_documento = "rexistro_host_"+str(i)+".txt"
			break
	documento=open(nome_documento,"w")
	documento.write("Rexistro NSLOOKUP:\n")
	for i in [i for i in lista_fios if not i.nome == ""]:
		documento.write(i.host+" - "+i.nome+"\n")
	documento.close()