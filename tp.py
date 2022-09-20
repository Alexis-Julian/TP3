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

""" --------------------------------------------------------- """
def busqueda_secuencial(al,af,instancia,cod):
    bus=instancia()
    noencontrado=True
    al.seek(0)
    t=os.path.getsize(af)
    pos = -1
    while al.tell() <t and noencontrado != False:
        bus=pickle.load(al)
        if int(bus.cod) == int(cod):
            noencontrado=False
            pos=al.tell()
    return pos

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

def alta_producto_rubro(car,nombre,al,af):
    clear("cls")
    print("---------Alta---------")
    t=os.path.getsize(af)
    al.seek(t)
    print("[0-Salir] Codigo de",nombre,": ")
    codigo=input("")
    while validar_tipo(int,codigo,0,1000):
        print("Numero entre [1-1000]")
        print("[0-Salir] Codigo de",nombre,":")
        codigo=input("")
    codigo=int(codigo)
    while codigo != 0:
        car.cod=codigo 
        print("Nombre de",nombre,": ")
        car.nombre=input("")
        while len(car.nombre) <0 or len(car.nombre) >20:
            print("El ",nombre,"debe tener como maximo 20 caracteres")
            print("Nombre de",nombre,":")
            car.nombre=input("")
        formatear(car,0)
        pickle.dump(car,al)
        al.flush()
        print("[0-Salir] Codigo de",nombre,":")
        codigo=input("")
        while validar_tipo(int,codigo,0,1000):
            print("Numero entre [1-1000]")
            print("[0-Salir] Codigo de",nombre,":")
            codigo=input("")
        codigo=int(codigo)
    mostrar(car,af,al)
    clear("pause")

def alta_silos_rubroxproducto(af,al,car):
    t=os.path.getsize(af)
    idx1=idx2=-1
    while idx1 == -1  or idx2==-1:
        rubro=input("Ingrese codigo de rubro: ")
        idx1=busqueda_secuencial(alr,afr,RubrosxProducto,rubro)
        resul=type(idx1)
        print(resul)
        codigo=input("Ingrese codigo de producto: ")
        idx2=busqueda_secuencial(alp,afp,RubrosxProducto,codigo)
        resul=type(idx2)
        print(resul)
        print(idx2)
        if  idx1 == -1:
            print("Error. El codigo de rubro ingresado no existe.")
        elif idx2== -1:
            print("Error. El codigo de producto ingresado no existe.")
    valmin,valmax=rubroxproducto_valminmax()
    al.seek(t)
    car.codrubro=rubro
    car.codpro=codigo
    car.valmin=valmin
    car.valmax=valmax
    formatear(car,1)
    pickle.dump(car,al)
    al.flush()
    
def rubroxproducto_valminmax():
    valmin=input("Ingrese el valor minimo: ")    
    while validar_tipo(int,valmin,0,100):
        print("Error. Debe ingresar un numero valido.")
        valmin=input("Intente nuevamente: ")
    valmax=input("Ingrese el valor maximos: ")
    while validar_tipo(int,valmax,int(valmin),100):
        print("Error. Debe ingresar un numero valido.")
        valmax=input("Intente nuevamente: ")
    return valmin,valmax
    

def submenu_administacion(opc1):
    opc=""
    while opc != "V":
        clear("cls")
        submenu_administacion_visible()
        opc=input("").upper()
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
        alta_producto_rubro(car,"Prodcutos",alp,afp)
    elif opc1== "C":
        rub=Rubros() 
        alta_producto_rubro(rub,"rubro",alr,afr)
    elif opc1=="D":
        car=RubrosxProducto() 
        alta_silos_rubroxproducto(afrxp,alrxp,car)

def administraciones():
    opc=""
    while opc != "V":
        clear("cls")
        adminstracion_visible()
        opc=input("").upper()
        if opc == "B"  or opc == "C" or opc== "D" or opc == "E":
            submenu_administacion(opc)
        elif opc == "A" or opc =="F" or opc=="G":
            construccion()            
        elif opc != "V":
            print("Opcion invalida")
            clear("pause")

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





menu()

t=os.path.getsize(afrxp)
alrxp.seek(0)
if t  == 0:
    print("nO HAY ARCGIVOS")
else:
    while alrxp.tell() <t:
        car=pickle.load(alrxp)
        print(car.codrubro,car.codpro)






