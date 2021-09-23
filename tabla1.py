def tabla():
    print("Hola, qué tal estás?")
    n=input("¿Qué tabla deseas?: ")
    print("***************************")
    print("*       TABLA DEL "+str(n)+ "       *")
    print("***************************")
    for cont in range(0,11):
        print(" "+str(n)+" x "+str(cont)+" = "+str(cont*n))

tabla()
