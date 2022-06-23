from xml.etree.ElementTree import XML


edad_roberta = 20

if edad_roberta >= 18 :
    print("Si puede entrar a la discoteca")
else :
    print("No puedes entrar, anda al cine")

edad_martin = 70
if edad_martin >= 65 :
    print("Esa persona esta jubilada")
elif edad_martin >= 18:
    print("Esa persona es mayor de edad")
elif edad_martin >=0 :
    print("Esa persona es menor de edad")
else:
    print("Edad imposible")

# la forma para ingresar valores al programa desde consola
#data = int(input("Hola, ingresa tu un numero: "))
data = input("Hola, ingresa tu talla de polo: ").lower()
print(type(data))

#Dependiendo de la talla del polo podriamos hacer lo siguiente: si es XL entonces
# indicar que llegara para fines de mes, si es L o M solicitar el color del polo,
#  si es S indicar que solamente hay en color Morado, si ingresa otra cosa, indicar
# que la talla es incorrecta

# Primer metodo
if data == xl :
    print("El polo llegara para fin de mes")
elif data == l or data == m :
    color = input("Indique que color de polo desea")
elif data == s:
    print("Solamente hay polo en color Morado")
else:
    print("La talla es incorrecta")
    

#Segundo metodo que igual funciona
if data == l or data == m :
    color = input("Indique que color de polo desea")
elif data == s:
    print("Solamente hay polo en color Morado")
if data == xl :
    print("El polo llegara para fin de mes")
else:
    print("La talla es incorrecta")