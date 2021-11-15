import sys

miNombreHospital = "general"
nuevoSalario=-1




#----------ALTA DOCTOR ---------------------------------------------------------
def altaDoctor():
    hospitalcod=0
    codigoHospital=0
    # print("entrando en altaDoctor()")
    nombreHospital = input("Introduzca el nombre del Hospital : \n")
    #hospitalcod = hospitalnombre2code(nombreHospital)
    #print(f'El código del Hospital es : {hospitalcod}')

    import cx_Oracle
    connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")
    cursor = connection.cursor()
    try:

        consulta = ("SELECT HOSPITAL_COD from HOSPITAL WHERE NOMBRE = :p1")

        cursor.execute(consulta, (nombreHospital,))
        # Si en un único parámetro tenemos que poner ',' a continuación del valor de la variable

        cursor.execute(consulta)
        codigoHospital = -1
        resultado = False
        for hospitalcode in cursor:
            #print(f"Código Hospital , hospital_cod: , {hospitalcode}")
            codigoHospital = hospitalcode[0]
            resultado = True
        if resultado == False:
            print("Sin resultados")
            codigoHospital = None
    except connection.Error as error:
        print("Error: ", error)
   # print(f"Código Hospital , hospital_cod: , {codigoHospital}\n")
    connection.close()

    connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")
    cursor = connection.cursor()
    try:
        doctorno = input("Inserte el número del Doctor (doctorno)  : ")
        apellido = input("Inserte el apellido del Doctor : ")
        especialidad= input("Inserte la especialidad del Doctor : ")
        salario= input("Inserte el salario del Doctor : ")



        cursor.callproc('tabladoctor.altaDoctor', (codigoHospital, doctorno, apellido, especialidad, salario))
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

# -------------MODIFICAR SALARIO DOCTOR -------------
def modificarSalarioDoctor():
    import cx_Oracle

    connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")

    cursor = connection.cursor()
    try:

        numDoctor = input("Inserte por favor el número del Doctor (Doctorno) :\n")
        nuevoSalario=int(input("Inserte el nuevo salario algo razonable :\n"))
        cursor.callproc('tabladoctor.modificarsalario', (numDoctor,nuevoSalario))

        print("DATO MODIFICADO ")

    except connection.Error as error:
        print("Error: ", error)
    cursor.close()
    connection.close()

# ----------------ELIMINAR DOCTOR -------------------------------------------

def eliminarDoctor():

    import cx_Oracle

    connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")

    cursor = connection.cursor()
    try:

        numDoctor = input("Inserte por favor el número del Doctor (Doctorno):")
        cursor.callproc('tabladoctor.borrardoctor', (numDoctor,))

        print("DATO ELIMINADO")

    except connection.Error as error:
        print("Error: ", error)
    cursor.close()
    connection.close()

# ----------------------------------------------------------------------------

def mostrarApellidoEspecialidad():
    import cx_Oracle
    connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")
    cursor = connection.cursor()
    try:
        miNumeroDoctor = input("Introduce Número de Doctor:")
        consulta = ("SELECT DOCTOR_NO, APELLIDO, ESPECIALIDAD FROM DOCTOR WHERE DOCTOR_NO= :p1")
        cursor.execute(consulta, (miNumeroDoctor,))

        resultado = False
        for doctno,ape, espe in cursor:
            print("Número DOCTOR : ", doctno)
            print("Apellido del Doctor: ", ape)
            print("Especialidad del Doctor : ", espe)
            resultado = True
        if resultado == False:
            print("Sin resultados")
    except connection.Error as error:
        print("Error: ", error)

    connection.close()


"""------------------------------------------------------
Vamos a crear una tabla nueva que se llama Grupo que tiene los datos de las tablas donde hay doctores y empleados, 

CREATE TABLE GRUPO
	(NOMBRE VARCHAR2(10),
	TIPO VARCHAR2(10),
	APELLIDO VARCHAR2(20),
	SALARIO NUMBER(10,0));



INSERT INTO GRUPO(NOMBRE, TIPO, APELLIDO, SALARIO)
select h.nombre, 'plantilla' Tipo, p.apellido, p.salario
from plantilla p
join hospital h on p.hospital_cod = h.hospital_cod
union
select h.nombre, 'doctor' Tipo, d.apellido, d.salario
from doctor d
join hospital h on d.hospital_cod = h.hospital_cod
order by 1,2,3


# select  nombre, sum(salario), avg(salario), count(*) from grupo where NOMBRE = 'general' group by nombre
"""

def visualizarDatosGrupo():
    import cx_Oracle
    connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")
    cursor = connection.cursor()
    try:
        miNombreHospital = input("Introduce el nombre del Hospital: \n")
        consulta = ("SELECT NOMBRE, SUM(salario), AVG(salario), COUNT(*) FROM GRUPO WHERE NOMBRE= :P1 GROUP BY NOMBRE")
        cursor.execute(consulta, (miNombreHospital,))



        resultado = False
        for nom, sumasal, avgsal, countemp in cursor:
            print("Datos del Grupo")
            print("Nombre Hospital : ", nom)
            print("Total Suma Salarial de Doctores y Empleados en Plantilla : ", sumasal)
            print("Media Salarial del Hospital : ", avgsal)
            print("Número de Empleados, Doctores y Plantilla : ", countemp)
            resultado = True
        if resultado == False:
            print("Sin resultados")
    except connection.Error as error:
        print("Error: ", error)

    connection.close()


#----------SALIR  ------------------------------------------------------------

def salir():
    sys.exit()

# ------------------------------MENU PRINCIPAL --------------------------------
quiereIntentarlo=True
letra="S"

while quiereIntentarlo :
    while letra== "S" or letra =="s" :
            print("Gracias por participar : ..... ")
            print( "1.- Alta Doctor ")
            print("2 .- Modificar salario Doctor ")
            print("3 .- Eliminar Doctor")
            print("4.- Mostrar apellido y especialidad de un Doctor ")
            print("5.- Visualizar datos de grupo de un Hospital")
            print("6.- Salir ")
            print(" ---------------------------------- ")
            opcion = input("Introduzca la opción requerida :  \n")
            if opcion=="1":
                altaDoctor()
            if opcion=="2":
                modificarSalarioDoctor()
            if opcion == "3":
                eliminarDoctor()
            if opcion == "4":
                mostrarApellidoEspecialidad()
            if opcion == "5":
                visualizarDatosGrupo()
            if opcion == "6":
                salir()
            print(" ----------------------------------------------")
            intento = input("¿Quiere volver a intentarlo? (S/N)").upper()
            if intento=="S" or intento=="s" :
                quiereIntentarlo=True
                letra="S"
            else:
                quiereIntentarlo=False
                letra="N"