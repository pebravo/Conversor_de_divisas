error = 0
salir=False
while not salir:
    print ('========================')
    print('|Banco Oeste\t\t|')
    print ('========================')
    print('|1.- Dólares\t\t|')
    print('|2.- Euro\t\t|')
    print('|3.- UF\t\t\t|')
    print('|4.- Salir\t\t|')
    print ('========================')
    dolar= 801.6
    euro=875.4
    uf=28993.7
    
    variable = int(input('Seleccione dirección de la converción :'))
    
    if variable == 1:
        print('1.- Peso chileno a Dólar') 
        print('2.- Dólar a peso Chileno')
        opcion = int(input('Ingrese opción :'))
        if opcion == 1:
            clp = int(input('Ingrese cantidad de pesos chilenos :'))
            print('Total dolares: US',round(clp/dolar,4))
            input('Presione Enter para continuar...!')
        if opcion == 2:
            dol = int(input('Ingrese cantidad de dólares :'))
            print('Total Pesos chilenos: $',round(dol*801.6,4))
            input('Presione Enter para continuar...!')
            
    elif variable == 2: 
        print('1.- Peso chileno a Euro') 
        print('2.- Euro a Peso chileno')
        opcion1 = int(input('Ingrese opción :'))
        if opcion1 == 1:
            clp2= int(input('Ingrese cantidad de pesos chilenos :'))
            print('Total euro: €',round(clp2/euro,4 ))
            input('Presione Enter para continuar...!')
        if opcion1 == 2:
            eur = int(input('Ingrese cantidad de euros :'))
            print('Total pesos chilenos: $',round(eur*875.4,4))
            input('Presione Enter para continuar...!')
            
    elif variable == 3:
        print('1.- Peso chileno a UF') 
        print('2.- UF a peso chileno')
        opcion2 = int(input('Ingrese opción :'))
        if opcion2 == 1:
            clp3 = int(input('Ingrese cantidad de pesos chilenos :'))
            print('Total UF: $',round(clp3/uf,4))
            input('Presione Enter para continuar...!')
        if opcion2 == 2:
            uf = int(input('Ingrese cantidad de UF :'))
            print('Total pesos chilenos: $',round(uf*28993.7,4))
            input('Presione Enter para continuar...!')
   
    elif variable == 4:
        salir=True
    else:
        print('opcion invalida intente denuevo')
        error = error+1
    if error == 3:
        print('“Ha llegado al límite de errores permitido”.')
        break




