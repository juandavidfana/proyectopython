 
nombre = input("Introduzca su nombre: " )  

edad = int(input("Introduzca su edad: "))
estatura = float(input("Introduzca su estatura: "))
peso = float(input("Introduzca su peso: "))
nacionalidad = (input("Cual es su nacionalida: "))

for i in  nacionalidad == 'haitiano' or 'Haitiano':
    es_Haitiano = True
    break
else:
    print(f'continuemos señor/a{nombre}')


print("Bienvenido ",nombre)
print("Su edad es ",edad)

if peso >180:
    frase1 = ("Usted esta obeso debe de rebajar")
    print(frase1)
else:
    frase2 = (f"Ustede esta en forma señor/a {nombre}")
    print(frase2)



lista_de_edades = []
print('ESTE ES EL SISTEMA QUE GUARDARA LAS EDADES')
cantidad = int(input('A cuantas pesonas quiere tomarle las edades: '))

for i in range(0, cantidad, 1):
    nombre = input('Ingrese el nombre de la persosna que quiere tomar la edad: ')
    
    edades = int(input(f'ingrese la edad de {nombre} por favor: '))
    lista_de_edades.append(edades)


# lista_de_pesos = []
# print('ESTE ES EL SISTEMA QUE GUARDA LOS PESOS')
# peso= int(input('A cuantas pesonas quiere tomarle el peso: '))

# for i in range(0, peso, 1):
#     nombre = input('Ingrese el nombre de la persosna que quiere tomar el peso: ')
    
#     peso = int(input(f'ingrese el peso de {nombre} por favor: '))
#     lista_de_pesos.append(peso)

# print(lista_de_pesos) 
print(lista_de_edades)
# print(lista_de_personas)






