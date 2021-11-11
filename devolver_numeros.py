def devuelve(num1,num2,num3):
    if(num1>num2 and num1>num3):
        mayor=num1
    if(num2>num1 and num2>num3):
        mayor=num2
    else:
       mayor=num3
    return(mayor)
def introducir():
    num1=input("Introduce un número: ")
    num2=input("Introduce otro número: ")
    num3=input("Introduce otro número: ")
    print("El número más grande de los tres es: "+str(devuelve(num1,num2,num3)))
introducir()


