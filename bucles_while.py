def bucles_while():
    suma=0
    continuar="S"
    while(continuar=="S"):
        num=input("Introduce un n�mero: ")
        suma=suma+num
        continuar=raw_input("�Quieres leer un n�mero m�s?(S/N): ")
    print("SUMA= "+str(suma))    
    
bucles_while()
