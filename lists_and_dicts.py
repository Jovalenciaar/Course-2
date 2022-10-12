def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dicts ={
        'firtsname': 'Jonnathan', 
        'Lastname': 'Valencia'
    }
     

    Super_list = [ 
        {'firtsname': 'Jonnathan', 'Lastname': 'Valencia'},
        {'firtsname': 'Carlos', 'Lastname': 'Mendez'},
        {'firtsname': 'Erika', 'Lastname': 'Calderon'},
        {'firtsname': 'Alejandro', 'Lastname': 'Valencia'},
        {'firtsname': 'Felipe', 'Lastname': 'Restrepo'},
    ]           

    Super_dicts = {
        'natural_nums': [1, 2, 3, 4, 5,],
        'integer_nums': [-1, 2, 0, 1, 2],
        'floating_nums': [4.1, 4.5, 3.4,]
    }

    for key, value in Super_dicts.items():
        print(key, '-', value)

        
    for item in Super_list:
        print(item['firtsname'], '-',item['Lastname'])


if __name__ == '__main__':
    run()