import os 
import pickle
import os.path
import datetime
from re import A
clear = lambda x: os.system(x)

class Operaciones():
    def __init__(self) -> None:
        self.patente=""
        self.codpro=0
        self.fechacupo=[0]*3
        self.estado=""
        self.bruto=0
        self.tara=0
class Productos():
    def __init__(self) -> None:
        self.cod=0
        self.nombre=""
        self.estado="A"
class Rubros():
    def __init__(self) -> None:
        self.cod=0
        self.nombre=""
        self.estado="A"
class RubrosxProducto():
    def __init__(self) -> None:
        self.codrubro=0
        self.codpro=0
        self.valmin=0.0
        self.valmax=0.0
class Silos():
    def __init__(self) -> None:
        self.codsilo=0
        self.nombre=""
        self.codpro=0
        self.stock=0

""" ---------------------------DEF---------------------- """
        
def validar_patente(opc):
    if len(opc) >=6 and len(opc) <=7:
        return False
    else:
        return True

def validar_tipo(tipo,opc,desde,hasta):
    try:
        opc=tipo(opc)
        while opc < desde or opc > hasta:
            print("Error. El numero ingresado debe estar entre",desde,"y",hasta)
            opc = tipo(input("Intente nuevamente: "))
    except:
        print("Error. Debe ingresar un numero.")
        opc = tipo(input("Intente nuevamente: "))
        validar_tipo(tipo,opc,desde,hasta)
    return opc
""" ---------------------------------------LJUST---------------------------------- """
#0-{Rubros,Productos};1-{Silos-RubrosxProductos}
def formatear(obj,b):
    if b==0:
        obj.cod=str(obj.cod)
        obj.cod=obj.cod.ljust(10," ")
        obj.nombre=obj.nombre.ljust(20," ")
    elif b==1:
        obj.valmin=str(obj.valmin)
        obj.valin=obj.valmin.ljust(2," ")
        obj.valmax=str(obj.valmax)
        obj.valmax=obj.valmax.ljust(2," ")
    elif b==3:
        obj.codsilo=obj.codsilo.ljust(10," ")
        obj.nombre=obj.nombre.ljust(10," ")
        obj.codpro=obj.codpro.ljust(10," ")
        obj.stock=obj.stock.ljust(5," ")
""" --------------------------------------------------------- """
def validar_longitud(mensaje,hasta):
    opc = input(mensaje)
    while len(opc) > hasta:
        print("Error. La longitud del codigo debe ser menor a",hasta)
        opc = input("Intente nuevamente: ")
    return opc

def busqueda_secuencial(al,af,instancia,cod):
    bus=instancia()
    encontrado = False
    al.seek(0)
    t=os.path.getsize(af)
    while al.tell() <t and encontrado == False:
        pos = al.tell()
        bus = pickle.load(al)
        if int(bus.cod) == int(cod):
            encontrado = True
    if encontrado:
        return pos
    else:
        return -1

def mostrar(vr,archf,archl):
    t=os.path.getsize(archf)
    archl.seek(0)
    if t== 0:
        print("No hay nda")
    else:
        while archl.tell() < t:
            vr=pickle.load(archl)
            print(vr.cod,vr.nombre)

def crear_archivos(archivo):
    if not os.path.exists(archivo):
        logico=open(archivo,"w+b")
    else:
        logico=open(archivo,"r+b")
    return logico
#-----------------------Archivos
afo="./operaciones.dat"
afp="./productos.dat"
afr="./rubros.dat"
afrxp="./rubrosxproductos.dat"
afs="./silos.dat"

alo=crear_archivos(afo)
alp=crear_archivos(afp)
alr=crear_archivos(afr)
alrxp=crear_archivos(afrxp)
als=crear_archivos(afs)
#----------------------Procedures1

def construccion():
    print("Esta funcionalidad esta construccion")
    clear("pause")

def adminstracion_visible():
    print("A-Titulares\nB-Productos\nC-Rubros\nD-RubrosXProductos\nE-Silos\nF-Sucursales\nG-Productos\nV-Volver al menu")

def submenu_administacion_visible():
    print("A-Alta\nB-Baja\nC-Consulta\nM-Modificaciones\nV-Volver al menu")

def menu_visible():
    print("[1] ADMINISTRACIONES \n[2] ENTREGA DE CUPOS \n[3] RECEPCION \n[4] REGISTRAR CALIDAD \n[5] REGISTRAR PESO BRUTO\n[6] REGISTRAR DESCARGA\n[7] REGISTRAR TARA\n[8] REPORTES\n[0] Fin del programa")

#---------------------Functions
""" ---------------------Alta Rubros Productos------------------ """
def alta_producto_rubro(car,nombre,al,af):
    clear("cls")
    print("---------Alta---------")
    t=os.path.getsize(af)
    al.seek(t)
    print("Seleccione codigo de",nombre,". Presione 0 para salir")
    codigo = validar_tipo(int,input("Codigo: "),0,1000)
    while codigo != 0:
        car.cod=codigo 
        print("Nombre de",nombre,": ")
        car.nombre=input("")
        while len(car.nombre)<0 or len(car.nombre)>20:
            print("El ",nombre,"debe tener como maximo 20 caracteres")
            print("Nombre de",nombre,":")
            car.nombre=input("")
        formatear(car,0)
        pickle.dump(car,al)
        al.flush()
        print("Seleccione codigo de",nombre,". Presione 0 para salir")
        codigo = validar_tipo(int,input("Codigo: "),0,1000)
        
    mostrar(car,af,al)
    clear("pause")
""" --------------------Alta RubroXProducot----------------------------------- """
def alta_silos_rubroxproducto(af,al,car):
    t = os.path.getsize(af)


    # ____________________________ ESTO HAY QUE HACERLO FUNCION___ LA BUSQUEDA DE CODIGOS YA SEA
    # DE RUBBROS O PRODUCTOS SE HACE EN RUBROXPRODUCTO, SILOS (Y CAPAPZ OPERACIONES)
    
    idx1=idx2=-1
    while idx1 == -1:
        codrubro = input("Ingrese codigo de rubro: ")
        idx1 = busqueda_secuencial(alr,afr,Rubros,codrubro)
        if  idx1 == -1:
            print("Error. El codigo de rubro ingresado no existe.")
    while idx2==-1:
        codproducto = input("Ingrese codigo de producto: ")
        idx2 = busqueda_secuencial(alp,afp,Productos,codproducto)
        if idx2== -1:
            print("Error. El codigo de producto ingresado no existe.")

    valmin,valmax=rubroxproducto_valminmax()
    al.seek(t)
    car.codrubro=codrubro
    car.codpro=codproducto
    car.valmin=valmin
    car.valmax=valmax
    formatear(car,1)
    pickle.dump(car,al)
    al.flush()


def rubroxproducto_valminmax():
    valmin = validar_tipo(int,input("Ingrese el valor minimo: "),0,100)
    valmax = validar_tipo(int,input("Ingrese el valor maximo: "),valmin,100)
    return valmin,valmax
    
""" -------------------------Alta Silos--------------------------- """
def silos(af,al,car):
    global alp,afp
    t = os.path.getsize(af)
    codigo = validar_longitud("Ingrese el codigo de silo: ",10)
    nombre = validar_longitud("Ingrese un nombre: ",10)
    regp = Productos()
    idx=-1
    while idx ==-1:
        codpro = validar_longitud("Ingrese un codigo de producto: ",10)
        idx = busqueda_secuencial(alp,afp,Productos,codpro)
    alp.seek(idx)
    regp = pickle.load(alp)   
    stock = validar_longitud("Ingrese un codigo de stock: ",10)
    al.seek(t)
    car.codsilo=codigo
    car.nombre=nombre
    car.codpro=regp.cod
    print(car.codpro)
    car.stock=stock
    formatear(car,3)
    pickle.dump(car,al)
    al.flush()

def submenu_administacion(opc1):
    opc=""
    while opc != "V":
        clear("cls")
        submenu_administacion_visible()
        opc=input("Seleccione una opcion: ").upper()
        match opc:
            case "A":
                altas(opc1)
            case "B":
                print("Hola")
            case "C":
                print("Hola")
            case "M":
                print("Hola")
            case "V":
                pass 
            case _:
                print("Opcion invalida")
                                
def altas(opc1):
    if opc1 == "B":
        car=Productos() #Define donde estas yendo######################
        alta_producto_rubro(car,"producto",alp,afp)
    elif opc1== "C":
        rub=Rubros() 
        alta_producto_rubro(rub,"rubro",alr,afr)
    elif opc1=="D":
        car=RubrosxProducto() 
        alta_silos_rubroxproducto(afrxp,alrxp,car)
    elif opc1 =="E":
        sil=Silos()
        silos(afs,als,sil)


def administraciones():
    opc=""
    while opc != "V":
        clear("cls")
        adminstracion_visible()
        opc=input("Seleccione una opcion: ").upper()
        if opc == "B"  or opc == "C" or opc== "D" or opc == "E":
            submenu_administacion(opc)
        elif opc == "A" or opc =="F" or opc=="G":
            construccion()            
        elif opc != "V":
            print("Opcion invalida")
            clear("pause")




def ingreso_fecha():
    ban = True
    while ban:
        try:
            fecha = input("Ingrese fecha en formato DD-MM-AAAA: ")
            datetime.datetime.strptime(fecha, '%d-%m-%Y')
            ban = False
            print("Fecha Valida")
        except ValueError:
            print("Fecha Invalida")
    return fecha
            

def entrega_cupos():
    pat = input("Ingrese patente: ")
    while(validar_patente(pat)):
        print("Error.La patente ingresada es invalida. Intente nuevamente")
        pat = input("Ingrese patente: ")
    #print("La fecha debe escribirse en el formato dia-mes-ano. Ejemplo '01-12-05'.")
    fecha = ingreso_fecha()
    print("Aca se imprime la fecha en hd",fecha)
    input("Ingrese contraseña de git: ")



def menu():
    opc=""
    while opc != "0":
        clear("cls")
        menu_visible()
        opc=input("Seleccione una opcion: ")
        match opc:
            case "1":
                administraciones()
            case "2":
                entrega_cupos()
            case "3":
                print("hola")
            case "4":
                print("hola")
            case "5":
                print("hola")
            case "6":
                print("hola")
            case "7":
                print("hola")
            case "8":
                print("hola")
            case "9":
                print("hola")
            case "0":
                print("Has salido")
            case _:
                pass


menu()

t=os.path.getsize(afrxp)
alrxp.seek(0)
if t  == 0:
    print("No hay archivos")
else:
    while alrxp.tell() <t:
        car=pickle.load(alrxp)
        print(car.codrubro,car.codpro)


