nombre = input("escribe tu nombre")
edad = input("escribe tu edad")
fecha = input("escribe tu fecha de nacimiento")

texto=[nombre+'\n', edad+'\n', fecha+'\n'] 
with open('alumnos.txt', 'a') as fichero:
    fichero.writelines(texto)

with open('alumnos.txt', 'r') as fichero:
     for linea in fichero.readlines():
 	    print(linea, end='')
