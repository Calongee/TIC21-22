def sustituye_vocales2():
    palabra=raw_input("Dime una palabra ")
    letra=raw_input("Dime la letra por la que quieras cambiar las vocales: ")
    nueva_palabra=" "
    cont=0
    while(cont<len(palabra)):
        if(palabra[cont]=="a"):
            nueva_palabra=nueva_palabra+letra
        else:
            if(palabra[cont]=="e"):
                nueva_palabra=nueva_palabra+letra
            else:
                if(palabra[cont]=="i"):
                    nueva_palabra=nueva_palabra+letra
                else:
                    if(palabra[cont]=="o"):
                        nueva_palabra=nueva_palabra+letra
                    else:
                        if(palabra[cont]=="u"):
                            nueva_palabra=nueva_palabra+letra
                        else:
                            nueva_palabra=nueva_palabra+(palabra[cont])
        cont=cont+1
    print("Palabra transformada: "+nueva_palabra)

sustituye_vocales2()
