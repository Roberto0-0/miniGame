#!/usr/bin/python3
import random
import os
import time
import datetime
import json

result = " "
score_list = []
players_list = []

#Arquivo json com as informações dos jogadores
with open("data/data.json","r") as file:
   players = json.load(file)

os.system("clear")
start = "\033[34mSTARTING\033[m"
print(start.center(30, "="))

#start o jogo
for matches in range(0, 10):
   time.sleep(5)
   os.system("clear")
   s = "\033[34m%s° PARTIDA\033[m"%(matches+1)

   #Adicionar o palpipe
   print(s.center(30, "="))
   for k, v in enumerate(players):
      value_input = input("%s falou -> "%(v["name"])).upper()
      #value_input = random.choice(["PAR", "IMPAR"])
      if value_input[0] == "P":
         v["guess"] = "PAR"
      elif value_input[0] == "I":
         v["guess"] = "IMPAR"
    
   #Verificar se o valor é IMPAR ou PAR
   random_number = random.randint(1, 100)
   if random_number % 2 == 0:
      result = "PAR"
      print("RESULTADO \033[32mPAR\033[m")
      #print(par.center(30, "-"))
   else:
      result = "IMPAR"
      print("RESULTADO \033[31mIMPAR\033[m")
      #print(impar.center(30, "-"))

   #Adicionar a pontuação a cada acerto
   for k, v in enumerate(players):
      if v["guess"] == result:
         v["score"]+=5
      else:
         v["score"]+=0

   #Lista todas as informações dos jogadores após uma palpipe
   for key, value in enumerate(players):
      if value["guess"] == result:
         if value["guess"] == "PAR":
            print("\033[33m-\033[m"*22)
            print("Jogador: \033[34m%s\033[m\nPalpite: \033[32m%s\033[m\nPontos:  \033[34m%s\033[m \033[32m+5\033[m"%(value["name"], value["guess"], value["score"]))
         elif value["guess"] == "IMPAR":
            print("\033[33m-\033[m"*22)
            print("Jogador: \033[34m%s\033[m\nPalpite: \033[31m%s\033[m\nPontos:  \033[34m%s\033[m \033[32m+5\033[m"%(value["name"], value["guess"], value["score"]))
      else:
         if value["guess"] == "PAR":
            print("\033[33m-\033[m"*22)
            print("Jogador: \033[34m%s\033[m\nPalpite: \033[32m%s\033[m\nPontos:  \033[34m%s\033[m"%(value["name"], value["guess"], value["score"]))
         elif value["guess"] == "IMPAR":
            print("\033[33m-\033[m"*22)
            print("Jogador: \033[34m%s\033[m\nPalpite: \033[31m%s\033[m\nPontos:  \033[34m%s\033[m"%(value["name"], value["guess"], value["score"]))

##      Após o final de uma partida     ##

#Sistema de ranking
print("\033[33m-\033[m"*22)
time.sleep(3)
ranking = "\033[34mRANKING PARTIDA\033[m"
print(ranking.center(30, "="))

#Adiciona os pontos e o id do jogador
for i in players:
   score = i["score"], i["id"]
   score_list.append(score)
   score_list.sort(reverse=True)
   all_score = score_list

#Verifica o id e retorna o ranking
cont_ranking = 0
for j in all_score:
   cont_ranking+=1
   for k, v in enumerate(players):
      if j[1] == v["id"]:
         if cont_ranking == 1:
            v["name"] = v["name"]+"👑"
            print(f"%s° {v['name']:<15} %s"%(cont_ranking,v["score"]))
         else:
            print(f"%s° {v['name']:<16} %s"%(cont_ranking,v["score"]))
#print("\033[32mData: %s/%s/%s\033[m"%(datetime.date.today().day, datetime.date.today().month,datetime.date.today().year))
the_end = "\033[34mTHE END\033[m"
print(the_end.center(30, "-"))
