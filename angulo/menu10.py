import libreria

def agregarPostal():
    # 1. Pedir el codigo postal
    localidad=libreria.pedir_nombre("Ingrese el nombre de la localidad:")
    postal=libreria.pedir_postal("Ingrese el codigo postal:")
    # 2. Guardar el codigo postak en el archivo postal.txt
    contenido= localidad+ "-" + postal + "\n"
    libreria.guardar_datos("postal.txt", contenido, "a")
    print("Datos guardados")

def mostrarPostal():
    # 1. Abrir el archivo postal.txt y mostrar sus datos
    data=libreria.obtener_datos_lista("postal.txt")
    # 2. COmprobar si hay datos
    if ( data != ""):
        for item in data:
            localidad,postal = item.split("-")
            msg="la localidad {} tiene el sgte codigo postak: {}"
            localidad=localidad.replace("\n","")
            postal=postal.replace("\n","")
            print(msg.format(localidad, postal))
        #fin_for
    else:
        print("No hay datos")

opc=""
max=3
while(opc != max):
    print("######### MENU ########")
    print("# 1. Agregar Postal    #")
    print("# 2. Mostrar Postal    #")
    print("# 3. Salir            #")
    print("#######################")
    opc=libreria.pedir_numero("Ingrese Opcion:", 1, 3)

    if ( opc ==1 ):
        agregarPostal()
    if ( opc ==2 ):
        mostrarPostal()
#fin_while
