def tabla_multiplicar():
    cont=0
    num=input("¿De qué número quieres la tabla de multiplicar? ")
    print("TABLA DEL "+str(num))
    while(cont<11):
        print(str(cont)+" x "+str(num)+" = "+str(cont*num))
        cont=cont+1
    
tabla_multiplicar()
        
    
