def diagrama():
    num=input("Dame un n�mero: ")
    sumita=1
    for cont in range(num,-1,-1):
        print(cont,sumita)
        sumita=sumita*cont
diagrama()
