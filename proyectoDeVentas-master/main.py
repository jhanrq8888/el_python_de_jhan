from persona import Persona
from zapatilla import Zapatilla
from factura import Factura
from factura_detalle import FacturaDetalle
from reportlab.pdfgen import canvas
from tkinter import *

personas: Persona = []
zapatillas: Zapatilla = []
factutas: Factura = []



def persona():
    dni: str = str(input("Ingrese DNI: "))
    nombres: str = str(input("Ingrese Nombres: "))
    apellidos: str = str(input("Ingrese Apellidos: "))
    direccion: str = str(input("Ingrese Direccion: "))
    telefono: str = str(input("Ingrese Telefono: "))
    persona: Persona = Persona(dni, nombres, apellidos, direccion, telefono)
    personas.append(persona)


def listar_personas():
    for persona in personas:
        Persona.convertir_a_string(persona)


def buscar_persona():
    dni: str = str(input("Ingrese DNI para buscar persona: "))
    for persona in personas:
        if persona.dni == dni:
            Persona.convertir_a_string(persona)
            return persona


def editar_persona():
    dni: str = str(input("Ingrese DNI para editar persona: "))
    for persona in personas:
        if persona.dni == dni:
            Persona.convertir_a_string(persona)
            persona.nombres = str(input("Ingrese nuevo nombre: "))
            Persona.convertir_a_string(persona)


def eliminar_persona():
    dni: str = str(input("Ingrese DNI para eliminar persona: "))
    for indice, persona in enumerate(personas):
        if persona.dni == dni:
            personas.pop(indice)


def zapatilla():
    codigo: str = str(input("Ingrese código del zapatilla: "))
    precio: float = float(input("Ingrese precio del zapatilla: "))
    marca: str = str(input("Ingrese marca del zapatilla: "))
    talla: float = float(input("Ingrese la talla de la zapatilla: "))
    color: str = str(input("Ingrese el color de la zapatilla: "))
    actividad: str = str(input("Ingrese para que se usara la zapatilla: "))
    zapatilla: Zapatilla = Zapatilla(codigo, precio, marca, talla, color, actividad)
    zapatillas.append(zapatilla)


def listar_zapatilla():
    for zapatilla in zapatillas:
        Zapatilla.convertir_a_string(zapatilla)


def buscar_zapatilla():
    codigo: str = str(input("Ingrese Código para buscar la zapatilla: "))
    for zapatilla in zapatillas:
        if zapatilla.codigo == codigo:
            Zapatilla.convertir_a_string(zapatilla)
            return zapatilla

def editar_zapatilla():
    codigo: str = str(input("Ingrese codigo para editar zapatilla: "))
    for zapatilla in zapatillas:
        if zapatilla.codigo == codigo:
            Zapatilla.convertir_a_string(zapatilla)
            zapatilla.precio = str(input("Ingrese nuevo precio: "))
            zapatilla.marca = str(input("Ingrese nueva marca: "))
            zapatilla.talla = str(input("Ingrese nueva talla: "))
            zapatilla.color = str(input("Ingrese nuevo color: "))
            zapatilla.actividad = str(input("Ingrese nueva actividad: "))
            Zapatilla.convertir_a_string(zapatilla)
            
def eliminar_zapatilla():
    codigo: str = str(input("Ingrese codigo para eliminar zapatilla: "))
    for indice, zapatilla in enumerate(zapatillas):
        if zapatilla.codigo == codigo:
            zapatillas.pop(indice)



def nueva_factura():
    print("para generar una factura busca un cliente")
    cliente: Persona = buscar_persona()
    factura: Factura = Factura(len(factutas)+1, cliente)
    continuar: bool = True

    while continuar:

        zapatilla: Zapatilla = buscar_zapatilla()
        cantidad: int = int(input("Ingrese la cantidad: "))
        factura.detalle.append(FacturaDetalle(
            zapatilla.codigo, cantidad, zapatilla.precio, zapatilla.talla))
        
        condicion: str = str(input("SI para agregar zapatillas: "))

        if condicion == "SI":
            continuar = True
        else:
            continuar = False
            factura.calcular_igv()
            factutas.append(factura)


def listar_factura():
    for factura in factutas:
        Factura.convertir_a_string(factura)

def buscar_factura():
    numero:int=int(input("Ingrese el numero de la factura: "))
    for factura in factutas:
        if factura.numero==numero:
            Factura.convertir_a_string(factura)
            print("===========================")
            for detalle in factura.detalle:
                FacturaDetalle.convertir_a_string(detalle)

def crear_pdf():
     canvas = canvas.Canvas("factura.pdf")
     canvas.drawString(470, 780, "R.U.C")
     canvas.drawString(450, 765, "20220134123")
     canvas.drawString(200,800, "ZAPATILLAS LOS CARIÑOSOS")
     canvas.rect(400,130 - 300, 150, 80 )
     canvas.drawString(50, 770, "Datos del Cliente:")
     canvas.drawString(50, 750, "TOTAL:")
     canvas.drawString(50, 730, "CANTIDAD:")
     canvas.drawString(50, 710, "IGV:")
     canvas.save()
     FacturaDetalle.convertir_a_string(Factura)

def main():
    continuar: bool = True

    while continuar:
        print("*****************************************")
        print("***********SISTEMA DE VENTAS*************")
        print("                                         ")
        print("===================MENÚ==================")
        print("**************INGRESE OPCIONES***********")
        print("       1: PARA AGREGAR PERSONA")
        print("       2: PARA LISTAR PERSONAS")
        print("       3: PARA BUSCAR PERSONA")
        print("       4: PARA EDITAR PERSONA")
        print("       5: PARA ELIMINAR PERSONA")
        print("       6: PARA AGREGAR ZAPATILLA")
        print("       7: PARA LISTAR ZAPATILLA")
        print("       8: PARA EDITAR ZAPATILLA")
        print("       9: PARA ELIMINAR ZAPATILLA")
        print("       10: PARA BUSCAR ZAPATILLA")
        print("       15: PARA CREAR FACTURA")
        print("       16: PARA LISTAR  FACTURA")
        print("       17: PARA BUSCAR FACTURA")
        print("       18: PARA IMPRIMIR FACTURA")
        print("       20: PARA SALIR")
        caso: str = str(input("INGRESE OPCIÓN: "))
        match caso:
            case "1":
                persona()
            case "2":
                listar_personas()
            case "3":
                buscar_persona()
            case "4":
                editar_persona()
            case "5":
                eliminar_persona()
            case "6":
                zapatilla()
            case "7":
                listar_zapatilla()
            case "8":
                editar_zapatilla()
            case "9":
                eliminar_zapatilla()
            case "10":
                buscar_zapatilla()
            case "15":
                nueva_factura()
            case "16":
                listar_factura()
            case "17":
                buscar_factura()
            case "18":
                crear_pdf()
            case "20":
                continuar = False


if __name__ == '__main__':
    main()
