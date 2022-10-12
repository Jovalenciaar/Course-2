

clients = 'Pablo-Ricardo-'


def create_client(client_name):
	global clients

	if client_name not in clients:
		clients += client_name
		_add_comma()
	else:
		print ('Client already is in the client\'s list')

def update_client(client_name, update_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + "-", update_name + '-')
    else:
        print('Client is not in client\'s list')


def delate_client(client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + '-', " " )
    else:
        print('Clients is no in clients list')


def list_clients ():
    global clients
    print(clients)


def search_client(client_name):
    clients_list = clients.split(',')
    
    for client in clients_list:
        if client != client_name:
         continue
        else:
            return True


def _get_name():
    return input("What is the client name?")
    

def _add_comma():
    global clients
    clients += "-"


def welcome():
    print('Welcome to Platzi ventas')
    print('-' * 40)
    print('What do you like today?')
    print('[C]reate client')
    print('[D]elate client')
    print('[U]pdate client')
    print('[S]earch client')
    print('[L]ist client')



if __name__ =='__main__':
    welcome()

    command = input()
    command = command.capitalize()

    if command == "C":
        client_name = _get_name()
        create_client(client_name)
        list_clients()

    elif command == "D":
        client_name = _get_name()
        delate_client(client_name)
        list_clients()

    elif command == "L":
        list_clients()

    elif command == "U":
        client_name = _get_name()
        update_name = input('What is the updated client name?')
        update_client(client_name, update_name)
        list_clients()

    elif command =="S":
        client_name = _get_name()
        found = search_client(client_name)
    
        if found:
            print('The client is in our list')
        else:
            print('The clients: {} is not in our list'.format(client_name))
		    
            
    else:
        print("Invalid command")

        
