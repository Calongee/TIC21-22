def analizador ():
    suma=0
    num=input("D�me un n�mero ")
    mayor=num
    menor=num
    for cont in range(1,5):
        num=input("D�me un n�mero ")
        if(num>mayor):
            mayor=num
        if(num<menor):
            menor=num
        suma=suma+num
    media=suma/5.0
    print("MAYOR= "+str(mayor))
    print("MENOR= "+str(menor))
    print("MEDIA= "+str(media))
     
    
analizador()
