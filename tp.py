import os 
import pickle
import os.path

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
        



