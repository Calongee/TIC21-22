def devuelve3():
    mayor=input("Dame un n�mero: ")
    for cont in range(1,10):
        num=input("Dame un n�mero: ")
        if (num>mayor):
           mayor=num
    print("El n�mero m�s grande de los diez es: " +str(mayor))
devuelve3()
    
