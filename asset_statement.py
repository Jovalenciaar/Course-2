def divisors(num):
    # divisors =[]
    # for i in range(1, num + 1):
    #     if num % i ==0:
    #         divisors.append(i)
    # return divisors
    divisors = [i for i in range (1, num +1) if num % i ==0]
    return divisors
       

def run():
    try:
        num = input('Ingresa un numero: ')
        assert num.isnumeric(), 'Debes ingresar un numero'
        print(divisors(int(num)))
        print('Termino mi programa')
        
    except AssertionError:
        print('Debes ingresar un numero positivo')
        run()


if __name__ =="__main__":
    run()