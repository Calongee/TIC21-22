def menu():
    #Pedimos dos numeros
    error=1
    while(error==1):
        num1=float(input("Introduce un numero: "))
        num2=float(input("Introduce otro n�mero: "))
        print("****************************")
        print("*           MENU           *")
        print("****************************")
        print("1. SUMAR")
        print("2. RESTAR")
        print("3. MULTIPLICACION")
        print("4. DIVISION")
        opcion=0
        while(opcion<=0 or opcion>4):
            opcion=input(" ELIGE: ")
            if(num2==0 and opcion==4):
                error=1
                print("ELECCION ERR�NEA. NO ME HAN ENSE�ADO A DIVIVIR POR 0")
            else:
                error=0
    print("Has elegido la opcion "+str(opcion))
    #OPCION SUMA
    if(opcion==1):
        print(num1+num2)
        #OPCION RESTA
    else:
        if(opcion==2):
            print(num1-num2)
            #OPCION PRODUCTO
        else:
            if(opcion==3):
               print(num1*num2)
                #OPCION COCIENTE   
            else:
                print(num1/num2)
menu()
