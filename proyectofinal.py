
lista_nombres = []

lista_de_calificaciones=[]



while True:
    print(' \nAPARTADO DE OPCIONES')
    print(' 1--AGREGAR ESTUDIANTE y CALIFICACIONES')        
    print(' 2-- CALCULAR LAS CALIFICACIONES ')
    print(' 3--SALIR')
    

    opcion = int(input("\ningrese la opocion que desea: "))
    
    if opcion == 1:     
        
        print('\n<-----ESTE ES EL APARTADO DE AGREGAR ESTUDIANTES Y CALICIFACIONES-------->')
        
        
        cantidad = int(input('\nA cuantas pesonas quiere agregar: '))

        for i in range(0, cantidad, 1):
                nombre = input('Ingrese el nombre de la persosna que quieres guardar: ')
                lista_nombres.append(nombre)
                 
                 
                print('<-----AHORA AGREGAREMOS SU CALIFICASION----->')
                print('\ndesea salir de este apartado')
                calificacion = eval(input(f'ingrese la calificacion : '))
            
                
                if calificacion.lower() =='si':
                    break
                try:  
                    notas = float(calificacion)
                    if 0< calificacion <100:
                        lista_de_calificaciones.append(calificacion)  
                    else:
                      print('la calificacion debe de ser de cero a cien')
                except ValueError:
                    print("la calificacion que ingreso es invalida")
                if len(lista_de_calificaciones) == 0 :
                    print('no se ha ingresado una calificasion aun')
                    
                    
                promedio = sum(lista_de_calificaciones) / len(lista_de_calificaciones) 
                print(promedio) 
                print(lista_de_calificaciones)
                print(lista_nombres)      
    if  opcion == 3:
        print('gracias por usar nuestro sistema')
        break
               
     



