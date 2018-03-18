import csv
import re
import datetime
import time

nome_array = []
ip_array = []


print("olaaaaaaaaaa")
with open('C:\\Users\\Deyvison\\Desktop\\script tarefa\\antenas_irc.csv', 'r', encoding="utf8") as f:
    print("Obtendo lista...")
    print(" ")
    reader = csv.reader(f)
    lista_hoteis = list(reader)
    for i in lista_hoteis:
        posicao_ip = i[0].find("10")
        ip = i[0][posicao_ip:posicao_ip+12].replace("[A-Z]","", 5).replace(" ","").replace("-","")
        ip_pure = re.findall( r'[0-9]+(?:\.[0-9]+){3}', ip )

        posicao_nome = i[0].find("MK")
        nome = i[0][:posicao_nome+3].replace("-","_").replace(" ","")
        nome2 = i[0][posicao_ip+13:].replace("-","_").replace(" ","_").replace("/","_").replace(".","_")

        nome_array.append(nome+nome2)
        ip_array.append(ip)



print("Antenas ficheiro...")
with open("C:\\Users\\Deyvison\\Desktop\\script tarefa\\resultadoirc.csv", 'w', encoding="utf8") as resultado:
    escrevendo = csv.writer(resultado)
    escrevendo.writerow(["Nome", "ip"])
    for i in range(len(nome_array)):
        print(ip_array[i], nome_array[i])
        escrevendo.writerow([nome_array[i],ip_array[i]])
    resultado.close()
print("done")
