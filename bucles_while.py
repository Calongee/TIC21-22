def bucles_while():
    suma=0
    continuar="S"
    while(continuar=="S"):
        num=input("Introduce un número: ")
        suma=suma+num
        continuar=raw_input("¿Quieres leer un número más?(S/N): ")
    print("SUMA= "+str(suma))    
    
bucles_while()
