import sys
from datetime import date


#----------------------------------------------------------------------
def insertar():
    import cx_Oracle

    connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")

    cursor = connection.cursor()
    try:
        inscrip = int(input("Inserte el número del enfermo : "))
        iapelli = input("Inserte el apellido del enfermo")
        idir = input("Inserte la dirección del enfermo")
        ifecnac= input("Inserte la fecha de nacimiento del enfermo")
        isex= input("Inserte el sexo del enfermo")
        inss = input("Inserte el Número de la Seguridad Social del enfermo")

        cursor.callproc('tablaenfermo.insertar', (inscrip, iapelli, idir, ifecnac, isex, inss))
        print("DATO INSERTADO")
#        ConsultaAlta = ("INSERT INTO ENFERMO "
#                        "(INSCRIPCION, APELLIDO, DIRECCION, FECHA_NAC, SEXO, NSS) "
#                        "VALUES (:P1, :P2, :P3, to_date(:P4, 'dd-mm-yyyy'), :P5, :P6)")

#        datosEnfermo = (inscrip, iapelli, idir, ifecnac, isex, inss)
#        cursor.execute(ConsultaAlta, datosEnfermo)
        connection.commit()

    except connection.Error as error:
        print("Error: ", error)

    cursor.close()
    connection.close()


#--------------------------------------------------------------


def salir():
    sys.exit()


#--------------------------------------------------------------


def consultar():
    import cx_Oracle
    connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")
    cursor = connection.cursor()
    try:
        consulta = ("SELECT * FROM ENFERMO" )
        cursor.execute(consulta)

        resultado = False
        for ideptno, inombre, idir, ifecnac, isex, inss in cursor:
            print("Número Inscripción Enfermo: ", ideptno)
            print("Nombre del Enfermo: ", inombre)
            print("Dirección donde se ubica : ", idir)
            print("Fecha de Nacimiento del enferno : ", ifecnac)
            print("Sexo del enfermo : ", isex)
            print("Número de la Seguridad Social del Enfermo: ", inss)
            resultado = True
        if resultado == False:
            print("Sin resultados")
    except connection.Error as error:
        print("Error: ", error)

    connection.close()

#--------------------------------------------------------------

def borrar():
    import cx_Oracle

    connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")

    cursor = connection.cursor()
    try:

        numSS = input("NÚMERO DE Seguridad Social:")
        cursor.callproc('tablaenfermo.borrar', (numSS,))

        print("DATO ELIMINADO")

    except connection.Error as error:
        print("Error: ", error)
    cursor.close()
    connection.close()

"""

   import cx_Oracle

    connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")

    cursor = connection.cursor()
    try:

        ConsultaBaja = ("Delete from enfermo where nss=:param1")

        NumeroSS = input("Indiqueme el Número de la Seguridad Social para eliminar el enfermo:")

        cursor.execute(ConsultaBaja, (NumeroSS,))
        if cursor.rowcount > 0:
            print("Enfermo eliminado satisfactoriamente")
        else:
            print("Dato no encontrado")

        connection.commit()


    except connection.Error as error:
        print("Error: ", error)
    cursor.close()
    connection.close()

"""

def modificar():


    import cx_Oracle

    connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")

    cursor = connection.cursor()
    try:


        NuevoDireccion = input("Nueva localización :")
        NumeroSS = input(" Número de la Seguridad Social para poder modificar la dirección de este enfermo :")

        cursor.callproc('tablaenfermo.cambiardireccion', (NumeroSS,NuevoDireccion))

        if cursor.rowcount > 0:
            print("Dirección modificada satisfactoriamente")
        else:
            print("Dato no encontrado")

        connection.commit()


    except connection.Error as error:
        print("Error: ", error)
    cursor.close()
    connection.close()
#---------------------------------------------------------



quiereIntentarlo=True
letra="S"

while quiereIntentarlo :
    while letra== "S" or letra =="s" :
            print("Gracias por participar : ..... ")
            print( "1.- Alta Doctor ")
            print("2 .- Modificar salario Doctor ")
            print("3 .- Eliminar Doctor")
            print("4.- Mostrar Apellido y especialidad de un Doctor ")
            print("5.- Visualizar datos de grup de un Hospital")
            print("6.- Salir ")
            print(" ---------------------------------- ")
            opcion = input("Introduzca la opción requerida :  \n")
            if opcion=="1":
                insertar()
            if opcion=="2":
                borrar()
            if opcion == "3":
                modificar()
            if opcion == "4":
                consultar()
            if opcion == "5":
                salir()
            print(" ----------------------------------------------")
            intento = input("¿Quiere volver a intentarlo? (S/N)").upper()
            if intento=="S" or intento=="s" :
                quiereIntentarlo=True
            else:
                quiereIntentarlo=False



