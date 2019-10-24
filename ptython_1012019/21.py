from funciones_21 import *
import random


     
            
lista = [(v, p) for v in ['A','2','3','4','5','6','7','8','9','j','q','k'] for p in ['c','d','p','t']]


Turno = random.randint(0,1)
if Turno == 0 :
    print ("jugador")
    resultado_jugador = jugar_jugador(lista)
    print ("maquina")
    resultado_maquina = jugar_maquina(lista)
    
else :
    print ("maquina")
    resultado_maquina = jugar_maquina(lista)
    print ("jugador")
    resultado_jugador = jugar_jugador(lista)
   
    
    



if resultado_jugador <=21 and (resultado_jugador > resultado_maquina or resultado_maquina > 21) :
    print ("ganaste")
    print ("resultado casa : " + str(resultado_maquina)) 
elif resultado_maquina <=21 and (resultado_maquina > resultado_jugador or resultado_jugador >21) :
    print ("gana la casa")
    print ("resultado casa : " + str(resultado_maquina)) 
elif resultado_jugador >21 and resultado_maquina >21 :
    print ("nadie gana")
    print ("resultado casa : " + str(resultado_maquina))    









