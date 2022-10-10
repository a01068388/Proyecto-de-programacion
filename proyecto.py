#!/usr/bin/env python

"""
Título del proyecto:
Fecha:

Autores:
A01066843 - Facundo Bautista Barbera - Avenida de Ciencias Aplicadas
A01067607 - Alejandro Cazares Juarez - Avenida de Innovación y Transformación
A00000000 - Nombre

Version de Python: 3.10.0
"""

# Iniciar lista de trabajadores
trabajadores = list()


# Esta clase actua como un modelo para todos los trabajadores
class Trabajador:

    # Constructor de la clase
    def __init__(self, nombre, grado_de_estudios, habilidad):
        self.nombre = nombre
        self.grado_de_estudios = grado_de_estudios
        self.habilidad = habilidad

    # Método de clase para cambiar el nombre de un trabajador
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    # Método de clase para cambiar el grado de estudios de un trabajador
    def cambiar_grado_de_estudios(self, nuevo_grado_de_estudios):
        self.grado_de_estudios = nuevo_grado_de_estudios

    # Método de clase para cambiar la habilidad de un trabajador
    def cambiar_habilidad(self, nueva_habilidad):
        self.habilidad = nueva_habilidad


# Función principal y menu principal
def main():
    # Bucle de menu principal
    while True:

        # Mostrar opciones
        print('----')  # Separador
        print(f'1 - Consultar o modificar trabajador.')
        print(f'2 - Registrar trabajador.')
        print(f'3 - Listar trabajadores.')
        print(f'4 - Salir.')

        # Pedir selección
        while True:
            # Entrada del usuario
            seleccion = input('Seleccione una opción: ')

            # Revisar si la selección es válida
            if seleccion in ['1', '2', '3', '4']:

                # Decidir que hacer y salir del bucle
                if seleccion in ['1', '2', '3']:
                    break

                # Salir del programa
                elif seleccion == '4':
                    exit()

            # Respuesta no fue válida
            else:
                print('Opción no válida.')

        # Consultar o modificar trabajador
        if seleccion == '1':

            # Revisar si hay trabajadores registrados
            print('----')  # Separador
            if len(trabajadores) == 0:
                print('No hay trabajadores registrados.')
                continue
            else:
                # Revisar cantidad de trabajadores
                if len(trabajadores) == 1:
                    cantidad_de_trabajadores = 'solo existe el trabajador con indice 0'
                else:
                    cantidad_de_trabajadores = f'puede seleccionar los números entre 0 y {len(trabajadores) - 1}'

                # Pedir selección
                while True:

                    # Revisar si la selección es válida
                    try:
                        seleccion = int(input(f'Seleccione un trabajador, actualmente {cantidad_de_trabajadores}: '))

                    # En caso de que no pueda ser un entero lo reportamos y repetimos
                    except ValueError:
                        print('Opción no válida.')

                    # Revisar si la selección es válida y salir del bucle o repetir
                    else:
                        if seleccion in range(len(trabajadores)):
                            break
                        else:
                            print('Opción no válida.')

                # Presentar resultados de la selección
                print('----')  # Separador
                print('Se seleccionó el trabajador con indice', seleccion)
                print(f'Nombre: {trabajadores[seleccion].nombre}')
                print(f'Grado de estudios: {trabajadores[seleccion].grado_de_estudios}')
                print(f'Habilidad: {trabajadores[seleccion].habilidad}')

                # Editar trabajador
                menu_editar_trabajador(trabajadores[seleccion], seleccion)

        elif seleccion == '2':
            print('----')  # Separador
            # Registrar nuevo trabajador
            trabajador = registrar_trabajador()
            print(f"Trabajador registrado: {trabajador.nombre}")

        elif seleccion == '3':
            if len(trabajadores) != 0:
                # Listar trabajadores
                print('----')  # Separador
                print('Trabajadores registrados:')

                for trabajador in trabajadores:
                    print('----')  # Separador
                    print(f'Indice de trabajador: {trabajadores.index(trabajador)}')
                    print(f'Nombre: {trabajador.nombre}')
                    print(f'Grado de estudios: {trabajador.grado_de_estudios}')
                    print(f'Habilidad: {trabajador.habilidad}')

            else:
                print('----')  # Separador
                print('No hay trabajadores registrados.')


# Menu para editar trabajador
def menu_editar_trabajador(trabajador, numero_de_trabajador):
    # Bucle de menu de edición
    while True:
        print('----')  # Separador
        print(f"1 - Cambiar nombre.")
        print(f"2 - Cambiar grado de estudios.")
        print(f"3 - Cambiar habilidad.")
        print(f"4 - Borrar trabajador.")
        print(f"5 - Salir.")

        while True:
            seleccion = input('Seleccione una opción: ')

            if seleccion in ['1', '2', '3', '4']:
                break
            else:
                print('Opción no válida.')

        # Cambiar nombre
        if seleccion == '1':
            nuevo_nombre = input('Nuevo nombre: ')
            trabajador.cambiar_nombre(nuevo_nombre)
            print(f'Nombre cambiado a {trabajador.nombre}')

        # Cambiar grado de estudios
        elif seleccion == '2':
            nuevo_grado_de_estudios = input('Nuevo grado de estudios: ')
            trabajador.cambiar_grado_de_estudios(nuevo_grado_de_estudios)
            print(f'Grado de estudios cambiado a {trabajador.grado_de_estudios}')

        # Cambiar habilidad
        elif seleccion == '3':
            nueva_habilidad = input('Nueva habilidad: ')
            trabajador.cambiar_habilidad(nueva_habilidad)
            print(f'Habilidad cambiada a {trabajador.habilidad}')

        # Borrar trabajador
        elif seleccion == '4':
            trabajadores.pop(numero_de_trabajador)
            print('Trabajador borrado.')
            break

        # Salir
        elif seleccion == '5':
            break

        # Preguntar si se desea editar otro dato
        print('----')  # Separador
        print('¿Desea editar otro dato del trabajador?')
        print(f"1 - Si.")
        print(f"2 - No.")

        # Pedir selección
        while True:
            seleccion = input('Seleccione una opción: ')

            if seleccion in ['1', '2']:
                break
            else:
                print('Opción no válida.')

        # Continuar o salir
        if seleccion == '1':
            continue
        elif seleccion == '2':
            break


# Función para registrar trabajador
def registrar_trabajador():
    # Pedir datos
    nombre = input('Nombre: ')
    grado_de_estudios = input('Grado de estudios: ')
    habilidad = input('Habilidad: ')

    # Crear objeto
    trabajador = Trabajador(nombre, grado_de_estudios, habilidad)

    # Agregar a la lista
    trabajadores.append(trabajador)

    # Devolver objeto
    return trabajador


# Iniciar script
if __name__ == '__main__':
    main()
