def piramide():
    fila_completa=" "
    num=input("Dime un n�mero: ")
    for fil in range(num,0,-1):
        for cont in range(1,fil+1):
            fila_completa=fila_completa+str(fil)
        print fila_completa
        fila_completa=" "
piramide()
