
clients = 'Pablo-Ricardo'

def create_client(client_name):
	global clients

	if client_name not in clients:
		clients += client_name
		_add_comma()
	else:
		print ('Client already is in the client\'s list')

def welcome():
	print ('WELCOME TO PLATZI VENTAS')
	print ('-' * 50)
	print ('What would you like to do today ? ')
	print ('[C]reate client')
	print ('[D]elete client')


def _add_comma():
    global clients  
    clients += '-'


def list_clients():
    global clients
    print(clients)

if __name__ == '__main__':
	welcome()

 