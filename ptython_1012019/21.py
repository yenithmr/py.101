import random

"""
Funcion que convierte las letras
de la baraja en valores numericos
retorna el valor numerico de la carta
"""
def valor_carta (c):
    if c == "j" :
        return 10
    elif c == 'q' :
        return 10
    elif c == 'k' :
        return 10
    elif c == 'A' :
        return 11
    else :
        return c

"""
es una funcion que recorre las cartas seleccinadas
y suma sus valores
retorna el valor total de la sumatoria de las cartas
"""
def suma (lista):
    total=0
    for i in range(0,len(lista)):
        # llamamos la funcion valor_carta con el valor de
        #de la carta para que nos retorne el valor numerico
        #y poder sumar el total
        total += int (valor_carta(lista[i][0]))
    return total


"""
esta funcion selecciona aleatoriamente una carta
"""
def aleatorio (tlist) :
    return random.randint(0,tlist-1)


"""
opcion de 1 o 11 en la carta A o As
"""
def buscar_y_reemplaza_As (lista):
    for i in range (0,len(lista)):
        if 'A' == lista [i][0] :
            lista [i] = (1,lista [i][1])
            break
    return lista
"""
recorre una listra hasta encontrar el primer As
si lo encuentra returna verdadero si no falso
"""
def buscar_As (lista):
    for i in range (0,len(lista)):
        if 'A' == lista [i][0] :
            return True
        else :
            return False 
     
            
lista = [(v, p) for v in ['A','2','3','4','5','6','7','8','9','j','q','k'] for p in ['c','d','p','t']]

def jugar_jugador():
    lista_carta = []

    aleatorio1 = aleatorio(len(lista))
    aleatorio2 = aleatorio(len(lista))


    #pop nos permite remover el ultimo elemento de la lista
    lista_carta.append(lista.pop(aleatorio1))
    lista_carta.append(lista.pop(aleatorio2))

    while True :
        print(lista_carta)
        print (str(suma(lista_carta)))
        res = suma(lista_carta)
        while res>21 and buscar_As (lista_carta) :
            lista_carta = buscar_y_reemplaza_As(lista_carta)
            print (str(suma(lista_carta)))
            res = suma(lista_carta)
            
        if res>21 :
            print ("perdiste")
            break
        
            
        u= input('quiere otra carta s/n :')
        if u == 's' :
            lista_carta.append(lista.pop(aleatorio(len(lista))))
        else :
            break
    return res

        
def jugar_maquina():
    lista_carta = []

    aleatorio1 = aleatorio(len(lista))
    aleatorio2 = aleatorio(len(lista))


    #pop nos permite remover el ultimo elemento de la lista
    lista_carta.append(lista.pop(aleatorio1))
    lista_carta.append(lista.pop(aleatorio2))

    while True :
        print(lista_carta)
        print (str(suma(lista_carta)))
        res = suma(lista_carta)
        while res>21 and buscar_As (lista_carta) :
            lista_carta = buscar_y_reemplaza_As(lista_carta)
            print (str(suma(lista_carta)))
            res = suma(lista_carta)

        if res <= 18 :
            lista_carta.append(lista.pop(aleatorio(len(lista))))
        else :
            break
            
        if res>21 :
            print ("perdiste")
            break
        
    return res

print ("jugador")
resultado_jugador = jugar_jugador()
print ("maquina")
resultado_maquina = jugar_maquina()

if resultado_jugador <=21 and (resultado_jugador > resultado_maquina or resultado_maquina > 21) :
    print ("ganaste")
elif resultado_maquina <=21 and (resultado_maquina > resultado_jugador or resultado_jugador >21) :
    print ("gana la casa")
elif resultado_jugador >21 and resultado_maquina >21 :
    print ("nadie gana")
        









