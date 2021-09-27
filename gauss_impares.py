def gauss_pares():
    n=input("Hola,¿hasta qué número quieres contar? ")
    acumulador=0
    resto=0
    for cont in range (1,n+1):
        resto= cont % 2
        if(resto==0):
            acumulador=acumulador+cont
        print (str(cont) +" acumulador= "+str(acumulador))
        
gauss_pares()
    
    
