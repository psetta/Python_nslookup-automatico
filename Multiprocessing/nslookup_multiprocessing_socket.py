# -*- coding: utf-8 -*-

import multiprocessing
import threading
import aux_multiprocessing as aux
import sys
import os
import re

# NON FUNCIONA EN WINDOWS


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

lista_ips = []

print "Procesando..."

while not ip == ip_final:
    lista_ips.append(ip[:])
    if "255" in ip:
        for i in range(1,4):
            if ip[i] == "255":
                ip[i] = "0"
                ip[i-1] = str(int(ip[i-1])+1)
    else:
        ip[3] = str(int(ip[3])+1)


if __name__ == "__main__":
    pool = multiprocessing.Pool(len(lista_ips))
    nomes = pool.map(aux.ip2nome, lista_ips)

print "\nResultados:"

for ip, nome in zip(lista_ips, nomes):
    if nome:
        print ".".join(ip), "-", nome

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
    for ip, name in zip(lista_ips, nomes):
        if name:
            documento.write(ip+" - "+name+"\n")
    documento.close()