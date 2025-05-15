###
# VARIABLES
# Las variables sirven para guardar datos en memoria
# Python es un lenguaje de tipado dinamico y de tipado fuerte
###

# Asignar una variable, solo hace falta poner esto:
my_name = "sergi"
# print(my_name)

# age = 26
# print(age)

age = 30
# print(age)

# Tipado dinamico: el tipo de dato se determina en tiempo de ejecución
# no tienes que declararlo explicicamente.

name = "sergi"
# print(type(name))

# name = 32
# print(type(name))

# Tipado fuerte: Python no realiza conversiones de tipo automaticas
# print(10 + "2")

#f string (literal de cadena de formato)
# desde la versión python 3.6
print(f"Hola {my_name}, tengo {age} años")

# NO RECOMENDADA FORMA DE ASIGNAR VARIABLES
name, age, city = "hola", 32, "Sabadell"

# convenciones de nombres de variables
mi_nombre_de_variable = "ok" #snake_case

MiNombreDeVariable = "ko" # PascalCase
minombredevariable = "ko" # todojunto

MI_CONSTANTE = 3.14 # UPPER_CASE -> constantes, no deberia cambiar

# palabras reservadas
# true = false ... etc