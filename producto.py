
class Articulo:
    "Clase que construye Articulo"

    def __init__(self, nombres, codigo, precio):
        
        self.nombres = nombres        
        self.codigo = codigo
        self.precio = precio        
        print(self.imprimir_cadena(),"SE REGISTRO CON EXITO")

    def imprimir_cadena(self):
        return print(" | ", self.nombres, " | ", self.codigo, " | ",self.precio," | ")
