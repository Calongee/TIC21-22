def tabla():
    print("Hola, qu� tal est�s?")
    n=input("�Qu� tabla deseas?: ")
    print("***************************")
    print("*       TABLA DEL "+str(n)+ "       *")
    print("***************************")
    for cont in range(0,11):
        print(" "+str(n)+" x "+str(cont)+" = "+str(cont*n))

tabla()
