def tabla():
    numero=raw_input("�Qu� tabla quieres?")
    print("*   TABLA DEL "+numero+"   *")
    for cont in range(0,11):
        print(+numero+ " x "str(cont)+" = "+str(+numero*cont))
    print("Ya est�")
        
tabla()
