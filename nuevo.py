import csv
import os



CLIENT_TABLE = './archivos/.client.csv'
CLIENT_ITEMS = ['name', 'surname', 'company', 'email', 'position']
# Estos son los parametros o Items que necesitamos conocer
clients = []


def inicialize_client():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_ITEMS)
# ROW in Spanish is RENGLON
        for row in reader:
            clients.append(row)


def _save_clients():
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_ITEMS)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE)
    os.rename(tmp_table_name, CLIENT_TABLE)


def welcome():
    global clients
    print("Welcome to Platzi ventas")
    print('-'*40)
    print("What are you gonna do today?")
    print('[C]reate client')
    print('[D]elate client')
    print('[U]pdate client')
    print('[S]earch client')
    print('[L]ist client')


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print("The client is in the client\'s list")


# def _add_comma():
#     global clients
#     clients += "-"


def list_client(): 
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {surname} | {company} | {email} | {position}'.format(
            uid = idx,
            name = client['name'],
            surname = client['surname'],
            company = client['company'],
            email = client['email'],
            position = client['position']))
# Usamos los corchetes para asignar las 2 variable sen este caso el Idx y el nobre dle cliente
# con el .format() asiganamos esos valores


def update_client(client_id, updated_client):
    global clients

    if len(clients) - 1 >= client_id:
        clients[client_id] = updated_client
    else:
        print('Client not in client\'s list')


def delete_client(client_id):
    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx] 
            break


def search_client(client_name):       
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def _get_client_quiestion(field_name):
    field = None

    while not field:
        field = input('What is the client {}?'.format(field_name))
    
    return field


# def _get_name():
#     client_name = None

#     while not client_name:
#         client_name = input('What is the client name?')

#         if client_name =='exit':
#             client_name == None
#             break

#     if not client_name:
#             sys.exit()

#     return client_name
def _get_client_start():
    client = {
        'name': _get_client_quiestion('name'),
        'surname': _get_client_quiestion('surname'),
        'company':_get_client_quiestion('company'),
        'email': _get_client_quiestion('email'),
        'position': _get_client_quiestion('position'),
    }
    return client




if __name__ == "__main__":
    
    inicialize_client()

    welcome()

    command = input()
    command = command.capitalize()

    if command =='C':
        client = _get_client_start()
        create_client(client)
        
    elif command == 'U':
        client_id = int(_get_client_quiestion('Id'))
        updated_client = _get_client_start()
        update_client (client_id, updated_client)
        
    elif command == 'D':
        client_id = int(_get_client_quiestion('Id'))
        delete_client(client_id)
            
    elif command == 'S':
        client = _get_client_quiestion('name')
        found = search_client(client)

        if found:
            print('The client is in the list')

        else:
            print('The client is no in the list')

    elif command == 'L':
        list_client()
 
    else:
        print("Invalid command")

_save_clients()