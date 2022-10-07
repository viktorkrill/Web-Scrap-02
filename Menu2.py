from os import execv


def pais(opciones):
    while True:
        for i, opcion in enumerate(opciones):
            print(i, opcion)
        try:
            opcion = int(input("¿En que pais quieres buscar? "))
            if opcion < 0 or opcion >= len(opciones):
                raise ValueError
            return opcion
        except ValueError:
            print("Opcion incorrecta")

opciones = ["Colombia", "Mexico", "Argentina"]
pais = pais(opciones)
print("-Has elegido", opciones[pais])


def menu(opciones):
    while True:
        for i, opcion in enumerate(opciones):
            print(i, opcion)
        try:
            opcion = int(input("¿En que tienes experiencia? "))
            if opcion < 0 or opcion >= len(opciones):
                raise ValueError
            return opcion
        except ValueError:
            print("Opcion incorrecta")


opciones = ["Python Developer", "Javascript Developer", "React Developer"]
opcion = menu(opciones)
print("-Has elegido", opciones[opcion])


def empresas(opciones):
    while True:
        for i, opcion in enumerate(opciones):
            print(i, opcion)
        try:
            opcion = int(input("¿Donde quieres buscar? "))
            if opcion < 0 or opcion >= len(opciones):
                raise ValueError
            return opcion
        except ValueError:
            print("Opcion incorrecta")


opciones = ["Computrabajo", "LinkedIn", "El Empleo"]
opcion = empresas(opciones)
print("-Buscando chambita en ", opciones[opcion])

if opcion == 0:
    exec(open("co-computrabajo/compuAWS.py").read())
elif opcion == 1:
    exec(open("linkedin.py").read())
elif opcion == 2:
    exec(open("empleo.py").read())
else:
    print("No entendi, repite por favor")
