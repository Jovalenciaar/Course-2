
# def convertidor_binario (number):
#     binary = []
#     while number >= 1:
#         if number%2 == 0:
#             binary.append(0)
#         elif number%2!= 0:
#             binary.append(1)            
#         return (binary[::-1])

# if __name__ == '__main__':
#     number = int(input('Ingresa un numero'))
#     binary = convertidor_binario(number)
#     print(f'{binary} es le numero en Binario de {number}')


def old (Mensaje):
    if Mensaje >= 18:
        print("You can enter to the party, Welcome!!")
    
    else:
        print("Sorry!! You can't enter to the party")




if __name__ == '__main__':
    Mensaje = int(input("How old are you? "))
    old(Mensaje)


