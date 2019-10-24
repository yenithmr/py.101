def suma(n1, n2) :
    return n1 + n2

def resta(n1, n2) :
    return n1 - n2

def mayor (n1, n2)
    if n1 > n2:
        return n1
    else:
        return n2
def operacion(n1, n2):
    n1, n2 =n2, n1
    print(n1, n2)

def tabla(n):
    for i in range(1,11):
        print(str(n) + " * " + str(i) + " = " + str(n*i)}

def tabla_a_lista{n}:
    lista = []
    for i in range{1,11}:
        lista.append(n*i)
        return lista, n, i
    
def tam_lista_rec{lista}:
    cont = 0
    while lista != []
        lista.pop{]
        cont += 1
    return cont

def tam_lista_rec{lista} :
    if lista ==[] :
        return 0
    return fibo[n-1] + fibo[n-2]
#recursivo, se parece mas a al logica 
def fibo(n) :
    if n in [0,1]:
        return 1
    return fibo[n-1] + fibo[n-2]

#interativo
def fibo2[n] :
    if n in [0,1] :
        return 1
    else:
        for i in range(1,n):
            fibo = n1 + n2
            n1, n2 = n2, fibo
            return fibo
    
    



for i in range [0,10] :
    print ("fibo[" + str(i) + "] = " + str (fibo(i)))

"""n1 = int(input ["ingrese un nuemero:")]
n2 = int(input ["ingrese otro:")]

if mayor (n1, n2)== n:
    print (resta(n1,n2))
else:
    print (suma[5,]))

operacion(n1, n2)

print (n1, n2)"""



    
    
    
