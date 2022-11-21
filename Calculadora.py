
def suma (number_1, number_2):
    resultado = number_1 + number_2
    resultado = str(resultado)
    print("La Suma es: " + resultado)


def resta (number_1, number_2):
    resultado = number_1 - number_2
    resultado = str(resultado)
    print('La Resta es: ' + resultado)


def multiplicacion (number_1, number_2):
    resultado = number_1 * number_2
    resultado = str(resultado)
    print('La Multiplicacion es: ' + resultado)


def division (number_1, number_2):
    resultado = number_1 / number_2
    resultado = str(resultado)
    print('La Division es: ' + resultado)




if __name__ == '__main__':

    menu = """ 
    Welcome to the calculator
    Select the operation that you want to do

    1 - Suma 
    2 - Resta
    3 - Multiplicacion
    4 - Divicion
    """

    option = int(input(menu))
    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter the secound number: '))

    if option == 1:
        suma (number_1, number_2)

    elif option == 2:
        resta (number_1, number_2)
    
    elif option == 3:
        multiplicacion (number_1, number_2)

    elif option == 4:
        division (number_1, number_2)    

        

