from persona import Persona
personas: Persona = []


def crear_persona():
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
    dni: str = str(input("Ingrese DNI para buscar: "))
    for persona in personas:
        if persona.dni == dni:
            Persona.convertir_a_string(persona)


def editar_persona():
    dni: str = str(input("Ingrese DNI para Editar: "))
    for persona in personas:
        if persona.dni == dni:
            persona.nombres = str(input("Ingrese un nuevo nombre: "))


def eliminar_persona():
    dni: str = str(input("Ingrese DNI para Eliminar: "))
    for index, persona in enumerate(personas):
        if persona.dni == dni:
            personas.pop(index)


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
        print("       10: PARA SALIR")
        caso: str = str(input("INGRESE OPCIÓN: "))
        match caso:
            case "1":
                crear_persona()
            case "2":
                listar_personas()
            case "3":
                buscar_persona()
            case "4":
                editar_persona()
            case "5":
                eliminar_persona()
            case "10":
                continuar = False


if __name__ == '__main__':
    main()
