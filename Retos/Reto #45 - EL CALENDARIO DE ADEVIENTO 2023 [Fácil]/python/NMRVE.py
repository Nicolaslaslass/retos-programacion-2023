import random

if __name__ == "__main__":

    participantes = []
    b = True
    def ingresar_participante():
        nombre = input('Nombre participante:')
        part = nombre.lower()
        if part in participantes:
            print('Ese nombre ya existe!')
        else:
            participantes.append(part)
        return True

    def borrar_participante():
        if participantes:
            quien = input('Nombre de tu eliminado:')
            eliminado = quien.lower()
            if eliminado in participantes:    
                participantes.remove(eliminado)
                print(f'{quien} fue eliminado')
            else:
                print(f'No existe {quien}')
            return True
        else:
            print('No hay participantes para eliminar :(')
            return True

    def mostrar_participantes():
        n = 1
        print('Estos son los participantes que están en sorteo:')
        for i in participantes:
            nombre = i.capitalize()
            print(f'{n}.- {nombre}')
            n += 1
        return True

    def lanzar_sorteo():
        if participantes:
            numero_ganador = random.randint(0,len(participantes)-1)
            ganador = participantes[numero_ganador]
            print(f'ganó {ganador.capitalize()}!!')
            participantes.remove(ganador)
        else:
            print('no hay participantes para sortear ')

        return True
    
    def salir():
        print('Adios!')
        return False
        

###################################################################

    print("#### Calendario de adviento ####")
    while b:
        dic_opt = {1: ingresar_participante, 
                   2: borrar_participante, 
                   3: mostrar_participantes, 
                   4: lanzar_sorteo, 
                   5: salir}
        
        print("Ingresa tu opción \n 1.- Añadir participante \n 2.- Eliminar participante \n 3.- Mostrar participantes \n 4.- Lanzar sorteo \n 5.- Salir")
        
        try:
            a = int(input('Opción:'))

            if a in dic_opt:
                b = dic_opt[a]()
            else:
                print('Opción inválida')
        except:
            print('Opción inválida')
