PASSWORD = '12345'


def decoradora(func):
    def intermedio():
        password = input('What is your password?')

        if password == PASSWORD:
            return func()
        else:
            print('The password is not correct!')
    return intermedio

# @decoradora
# este deocrador nos permite ejecuar primero la funcion decoradora
def needs_password():
    print("The password is correct")


# def upper (func):
#     def wrapper(*args, **kwargs):
        


# def say_my_name(name):
#     print('Hello, {}'.format(name))   

if __name__ =='__main__':
    needs_password()
    # say_my_name("Jonnathan")