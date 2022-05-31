calificacion = input("introduce tu calificacion de la AZ-900: ")

calificacion =int(calificacion)

if calificacion < 700 :
    print("Lo siento reprobaste") # si es menor a 700 muestras esto
elif calificacion > 1000:
    print("No puedes sacar mas de mil")
else :
    print("Felicidades, pasa por tu certificado")  # se ejecuta por si alguno de los if se cumple



edad = input("Introduce tu edad: ")
edad = int(edad)


if edad >= 18 and edad <= 100:
    print("bienvenido al mamitas")
elif edad > 100:
    print("Si vienes acompañado de tus abuelitos, si te fiamos")
elif edad < 0:
    print("ni que fueras viajero del timapo")
else:
    print("no puedes ver chicas malas")