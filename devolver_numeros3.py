def devuelve3():
    mayor=input("Dame un número: ")
    for cont in range(1,10):
        num=input("Dame un número: ")
        if (num>mayor):
           mayor=num
    print("El número más grande de los diez es: " +str(mayor))
devuelve3()
    
