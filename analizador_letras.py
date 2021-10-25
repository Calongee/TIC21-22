def analizador_letras():
    letras=0
    vocal=0
    consonante=0
    cont=0
    palabra=raw_input("Dime una palabra: ")
    while(cont<len(palabra)):
        if(palabra[cont]in "aeiou"):
            vocal=vocal+1
        else:
            consonante=consonante+1
        cont=cont+1
        letras=letras+1
    print("NÚMERO DE VOCALES: "+str(vocal))
    print("NÚMERO DE CONSONANTES: "+str(consonante))
    print("NÚMERO DE LETRAS: "+str(letras))
analizador_letras()
                
                
                
                
            
            
