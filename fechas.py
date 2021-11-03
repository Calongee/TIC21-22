def fecha_mes():
    fecha=raw_input("Introduce una fecha (dd/mm/aa): ")
    meses="EneFebMarAbrMayJunJulAgoSepOctNovDic"
    miMes=int(fecha[3])*10+int(fecha[4])
    print("Tu mes es el número "+str(miMes))
    mes_elegido=meses[(miMes-1)*3:(miMes-1)*3+3]
    print("Nombre del mes: "+str(mes_elegido))
    
fecha_mes()

