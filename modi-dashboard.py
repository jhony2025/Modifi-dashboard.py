import os

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Contenido de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def agregar_nota(ruta_archivo):
    ruta_absoluta = os.path.abspath(ruta_archivo)
    print("\nEscribe tu nota. Para finalizar, deja una línea vacía y presiona Enter.")
    lineas = []
    while True:
        linea = input()
        if linea == "":
            break
        lineas.append(linea)
    try:
        with open(ruta_absoluta, 'a', encoding='utf-8') as archivo:
            archivo.write("\n".join(lineas) + "\n")
        print("Nota agregada correctamente.")
    except Exception as e:
        print(f"No se pudo guardar la nota: {e}")

def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'CODIGOS-DE-PYTHON-2DO-SEMESTRE/COSTRUCTORES Y DESTRUCTORES/Constructores y Destructores.py',
        '2': 'manejo-de-archivo/Control-archivos.py',
        '3': 'manejo-de-archivo/POO_Biblioteca.py',
        '4': 'manejo-de-archivo/ejemplo.txt',
        '5': 'CODIGOS-DE-PYTHON-2DO-SEMESTRE/README.md',
        '6': 'registro_avances.txt'  # Archivo para tus notas o avances
    }

    print("\n======================== DASHBOARD PERSONAL DE JOHNNY VERA ========================")
    print("Edad: 44 años | Universidad Estatal Amazónica (UEA)")
    print("Carrera: Tecnología de la Información\n")

    while True:
        for key, value in opciones.items():
            print(f"{key} - {value}")
        print("7 - Agregar nota rápida a registro_avances.txt")
        print("0 - Salir")

        eleccion = input("Elige una opción: ")
        if eleccion == '0':
            print("¡Hasta luego, Johnny!")
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        elif eleccion == '7':
            ruta_nota = os.path.join(ruta_base, opciones['6'])
            agregar_nota(ruta_nota)
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
