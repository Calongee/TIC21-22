def palabra4():
    nombre=raw_input("NOMBRE: ")
    apellido=raw_input("APELLIDO: ")
    print("Buenos días, "+nombre+ " "+apellido)
    print("Tu nombre empieza por la letra "+nombre[0])
    print("Voy a deletrear tu nombre")
    for cont in range(0,20):
        print(nombre[cont])
    
    

palabra4()
