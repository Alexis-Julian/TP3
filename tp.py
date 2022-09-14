from math import prod
import os 
import pickle
import os.path
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
class Rubros():
    def __init__(self) -> None:
        self.cod=0
        self.nombre=""
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

class comp():
    def __init__(self) -> None:
        self.var1=0
        self.var2=""

""" ---------------------------DEF---------------------- """
        
def validarpatente(opc):
    if len(opc) >=6 and len(opc) <=7:
        return False
    else:
        return True

def validar_tipo(tipo,opc,desde,hasta):
    try:
        opc=tipo(opc)
        if opc >= desde and opc <= hasta:
             return False
        else:
            return True
    except:
        return True

def crear_archivos(archivo):
    if not os.path.exists(archivo):
        logico=open(archivo,"w+b")
    else:
        logico=open(archivo,"r+b")
    return logico

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
def formatear(obj,b):
    if b==0:
        obj.cod=str(obj.cod)
        obj.cod=obj.cod.ljust(10," ")
        obj.nombre=obj.nombre.ljust(20," ")

def mostrar(vr,archf,archl):
    t=os.path.getsize(archf)
    archl.seek(0)
    if t== 0:
        print("No hay nda")
    else:
        while archl.tell() < t:
            vr=pickle.load(archl)
            print(vr.cod,vr.nombre)

def producto(car):
    opcion=input("").upper()
    clear("cls")
    match opcion:
        case "A":
            print("---------Alta---------")
            t=os.path.getsize(afp)
            alp.seek(t)
            codigo=input("[0-Salir] Codigo de producto: ")
            while validar_tipo(int,codigo,0,1000):
                print("Numero entre [1-1000]")
                codigo=input("[0-Salir] Codigo de producto: ")
            codigo=int(codigo)
            while codigo != 0:
                car.cod=codigo 
                car.nombre=input("Nombre de producto: ")
                while len(car.nombre) <0 or len(car.nombre) >20:
                    print("El producto debe tener como maximo 20 caracteres")
                    car.nombre=input("Nombre de producto: ")
                formatear(car,0)
                pickle.dump(car,alp)
                alp.flush()
                codigo=input("[0-Salir] Codigo de producto: ")
                while validar_tipo(int,codigo,0,1000):
                    print("Numero entre [1-1000]")
                    codigo=input("[0-Salir] Codigo de producto: ")
                codigo=int(codigo)
            mostrar(car,afp,alp)
            os.system("pause")
        case "B":
            print("")
        case "C":
            print("")
        case "M":
            print("")
        case "Z":
            print("")
        case "V":
            pass
        case _:
            pass

    

def menu():
    opc=""
    while opc != "0":
        clear("cls")
        menu_visible()
        opc=input("")
        match opc:
            case "1":
                administraciones()
            case "2":
                print("hola")
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

def administraciones():
    opc=""
    while opc != "V":
        clear("cls")
        adminstracion_visible()
        opc=input("").upper()
        match opc:
            case "A":
                construccion()
            case "B":
                clear("cls")
                submenu_administacion_visible()
                car=Productos()
                producto(car)
            case "C":
                submenu_administacion_visible()

            case "D":
                submenu_administacion_visible()
            case "E":
                submenu_administacion_visible()
            case "F":
                construccion()
            case "G":
                construccion()
            case "V":
                pass
            case _:
                pass                


menu()





