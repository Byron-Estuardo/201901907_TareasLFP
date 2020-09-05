Palabra = '__servidor1'
PalabraU = '3servidor'
PalabraUP = Palabra.upper()
PalabraUUP = PalabraU.upper()
def AFD(entrada):
    estado = 0
    for i in range(len(entrada)):
        if estado == 0:
            if entrada[i] == '_':
                estado = 1
            elif entrada[i].isalpha() == True:
                estado = 2
            else:
                print('Error, Entrada Incorrecta')
                return
        elif estado == 1:
            if entrada[i] == '_':
                estado = 1
            elif entrada[i].isalpha() == True:
                estado = 3
            else:
                print('Error, Entrada Incorrecta')
                return
        elif estado == 2:
            if entrada[i].isalpha() == True:
                estado = 2

            elif entrada[i].isnumeric() == True:
                estado = 4
            else:
                print('Error, Entrada Incorrecta')
                return

        elif estado == 3:
            if entrada[i].isnumeric() == True:
                estado = 4
            else:
                print('Error, Entrada Incorrecta')
                return


        elif estado == 4:
            print('Si Corre')
    print('La Entrada ')

AFD(PalabraUP)
AFD(PalabraUUP)