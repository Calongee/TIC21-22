def devuelve(num1,num2,num3):
    if(num1>num2 and num1>num3):
        mayor=num1
    if(num2>num1 and num2>num3):
        mayor=num2
    else:
       mayor=num3
    return(mayor)
def introducir():
    num1=input("Introduce un n�mero: ")
    num2=input("Introduce otro n�mero: ")
    num3=input("Introduce otro n�mero: ")
    print("El n�mero m�s grande de los tres es: "+str(devuelve(num1,num2,num3)))
introducir()


