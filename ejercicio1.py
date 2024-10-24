def menu():
    print('Seleccione el proceso que desea aplicar')
    print('1: Ingresar puntuación y comentario')
    print('2: Comprueba los resultados obtenidos hasta ahora.')
    print('3: Finalizar')
    
def puntuar_y_comentar():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        
        if point.isdecimal():
            point = int(point)
            
            if point < 1 or point > 5:
                print('Por favor, introduzca un valor entre el 1 y 5')
            else:
                print('Por favor, introduzca un comentario')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                break
        else:
            print('Por favor, introduzca la puntuación en números')
            
def ver_resultados():
    print('Resultados hasta la fecha.')
    read_file = open("data.txt", "r")
    print(read_file.read())
    read_file.close()
        
def finalizar():
    print('Finalizando')
    
def principal():
    while True:
        menu()
        num = input()
        
        if num.isdecimal():
            num = int(num)
            if num == 1:
                puntuar_y_comentar()
            elif num == 2:
                ver_resultados()
            elif num == 3:
                finalizar()
                break
            else:
                print('Introduzca un número del 1 al 3')
        else:
            print('Introduzca un número del 1 al 3')
            
            
principal()