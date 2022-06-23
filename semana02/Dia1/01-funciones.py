#una funcion es bloque de codigo que no se ejecutara automaticamente hasta que sea llamado

import re


def saludar():
    print("Buenas tardes!")

saludar()

def saludarConNombre(nombre):
    print("Hola {}, como te va?".format(nombre))

def saludoCordial(nombre):
    """Funcion que recibe un nombre y te saluda cordialmente preguntandote como te va"""
    print("Hola {}, como te va?".format(nombre))

saludarConNombre("Eduardo")
saludarConNombre(False)

saludoCordial("Eduardo")

# funcion que puede devolver un valor (esto se debera al resultado de cierta logica)

def calcularIGV(valor):
    valorIncluidoIGV = valor * 1.18
    return valorIncluidoIGV

precio=100
precioConIGV=calcularIGV(precio)
print(precioConIGV)

precio=110
precioConIGV=calcularIGV(precio)
print(precioConIGV)

precio=150
precioConIGV=calcularIGV(precio)
print(precioConIGV)

precio=800
precioConIGV=calcularIGV(precio)
print(precioConIGV)

precio=600
precioConIGV=calcularIGV(precio)
print(precioConIGV)

def calcularSalarioMinimo(profesion, experiencia):
    salarioMinimo=1050
    if profesion == "Desarrollador":
        if experiencia == "Basica":
            salarioMinimo = 3000
        elif experiencia == "Media":
            salarioMinimo = 4000
        elif experiencia == "Avanzada":
            salarioMinimo = 7000
    elif profesion == "Marketing":
        if experiencia == "Basica":
            salarioMinimo = 2500
        elif experiencia == "Media":
            salarioMinimo = 4150
        elif experiencia == "Avanzada":
            salarioMinimo = 6820
    
    return salarioMinimo

profesion,experiencia = "Desarrollador","Basica"
salario = calcularSalarioMinimo(profesion,experiencia)
print(salario)

profesion,experiencia = "Desarrolador","Media"
salario = calcularSalarioMinimo(profesion,experiencia)
print(salario)

profesion,experiencia = "Desarrolador","Avanzada"
salario = calcularSalarioMinimo(profesion,experiencia)
print(salario)

#de esta manera se puede indicar a un parametro va a ir determino valor si no queremos respetar el orden
#de los parametros al momento de definir la funcion

salario = calcularSalarioMinimo(experiencia="basica", profesion="Marketing")
print(salario)

electrodomesticos = []

def registrarElectrodomesticos(nombre,precio,almacen="Las Malvinas"):
    electrodomesticos.append({"nombre":nombre,  "precio":precio, "almacen":almacen})
    return True

registrarElectrodomesticos("Licuadora 12v", 115.00)
registrarElectrodomesticos("Freidora de aire", 100,"Cercado")
registrarElectrodomesticos("Secador de cabello", 140)
registrarElectrodomesticos("Vaso de vidrio",9.90,"Panamerica Norte")

print(electrodomesticos)

def contarElectromesticosPorAlmacen():
    """Cuenta cuantos electrodomesticos hay en cada Almacen"""
    print(electrodomesticos[0])

    malvinas=0
    cercado=0
    for electromestico in electrodomesticos :
        if electromestico["almacen"] == "Las Malvinas" :
            malvinas +=1
        elif electromestico["almacen"] == "Cercado" :
            cercado +=1
        else:
            otro +=1
        #luego de iterar los electrodomesticos indicar
        #en las malvinas hay 2 electrodomesticos y en el cercado hay 1 electrodomestico

        return [malvinas,cercado,otro]

resultado=contarElectromesticosPorAlmacen()
print("""En Las Malvinas hay {}, en Cercado hay {} y en Otros
hay {} electrodomesticos""".foramat(resultado[0],resultado[1],resultado[2]))

#si en una funcion queremos recibir un numero indeterminado en valores
# args > arguments
def recibirAlumnos(clase,*alumnos):
    #cuando un parametro tiene el * al comienzo significa que ese
    #parametro recibira n valores y  lo convertira en una tupla
    print(type(alumnos)) #mostrar el tipo de dato que contiene esta  variable
                         #typeof en Javascript
    print(alumnos)
    alumnos_lista = list(alumnos) # se convierte de un tipo de dato a otro SIEMPRE Y CUANDO SEA COMPATIBLE
    #alumnos_numero = int(alumnos) # esto al no ser compatible emitira un error y matara el programa
    print(clase)
    