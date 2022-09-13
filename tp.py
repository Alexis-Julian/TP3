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
        self.codpro=0
        self.nompro=""
class Rubros():
    def __init__(self) -> None:
        self.codrubro=0
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


def menu_visible():
    print("[1] ADMINISTRACIONES \n[2] ENTREGA DE CUPOS \n[3] RECEPCION \n[4] REGISTRAR CALIDAD \n[5] REGISTRAR PESO BRUTO[6] REGISTRAR DESCARGA\n[7] REGISTRAR TARA\n[8] REPORTES\n[0] Fin del programa")


def menu():
    opc="-1"
    while opc != "0":
        clear("cls")
        menu_visible()
        opc=input("")
        match opc:
            case "1":
                print("hola")
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
menu()




# lang = input("What's the programming language you want to learn? ")

# match lang:
#     case "1":
#         ("You can become a web developer.")

#     case "2":
#         ("You can become a Data Scientist")

#     case "3":
#         ("You can become a backend developer")
    
#     case "4":
#         ("You can become a Blockchain developer")

#     case "5":
#         ("You can become a mobile app developer")
#     case _:
#         ("The language doesn't matter, what matters is solving problems.")

