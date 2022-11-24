import tkinter

#Para un usuario, crea un formulario que pida 
#nombre, apellido, edad, sexo, correo, contraseña, username, hobbies.
#Al presionar el botón, almacena los datos en un diccionario, y posteriormente, genera la consulta 
#para insertar los datos en una tabla de una base de datos.

ventana = tkinter.Tk()
#ventana.geometry("1024x768")
ventana.title("Formulario")
#Nombre
nombre = tkinter.Label(text="Ingrese su Nombre: ")
cajanombre = tkinter.Entry()
cajanombre.grid(row=1, column=1)
nombre.grid(row=1, column=0)

#Apellido
apellido = tkinter.Label(text="Ingrese su Apellido: ")
cajaapellido = tkinter.Entry()
cajaapellido.grid(row=2, column=1)
apellido.grid(row=2, column=0)

#Edad
edad = tkinter.Label(text="Ingrese su Edad: ")
cajaedad = tkinter.Entry()
cajaedad.grid(row=3, column=1)
edad.grid(row=3, column=0)

#Sexo
sexo = tkinter.Label(text="Ingrese su Sexo: ")
cajasexo = tkinter.Entry()
cajasexo.grid(row=4, column=1)
sexo.grid(row=4, column=0)

#Correo
correo = tkinter.Label(text="Ingrese su Correo: ")
cajacorreo = tkinter.Entry()
cajacorreo.grid(row=5, column=1)
correo.grid(row=5, column=0)

#Contraseña
contraseña = tkinter.Label(text="Ingrese su Contraseña: ")
cajacontraseña = tkinter.Entry()
cajacontraseña.grid(row=6, column=1)
contraseña.grid(row=6, column=0)

#Username
username = tkinter.Label(text="Ingrese su Username: ")
cajausername = tkinter.Entry()
cajausername.grid(row=7, column=1)
username.grid(row=7, column=0)

#Hobbies
hobbies = tkinter.Label(text="Ingrese sus Hobbies: ")
cajahobbies = tkinter.Entry()
cajahobbies.grid(row=8, column=1)
hobbies.grid(row=8, column=0)


def guardar():
    f = open("datos.txt", "w")
    f.write("Nombre: " + cajanombre.get() +"\n")
    f.write("Apellido: " + cajaapellido.get() + "\n")
    f.write("Edad: " + cajaedad.get() + "\n")
    f.write("Sexo: " + cajasexo.get() + "\n")
    f.write("Correo: " + cajacorreo.get() + "\n")
    f.write("Contraseña: " + cajacontraseña.get() + "\n")
    f.write("Username: " + cajausername.get() + "\n")
    f.write("Hobbies: " + cajahobbies.get() + "\n")
    f.close()
boton= tkinter.Button(ventana, text="Boton", command=guardar)
boton.grid (row=9, column=0)
ventana.mainloop()