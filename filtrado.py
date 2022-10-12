LIST = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Hector',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run ():

    all_personal_python = [worker['name'] for worker in LIST if worker['language'] == 'python']

    all_personal_python2 = list(filter(lambda worker: worker['language'] == 'python', LIST))
    all_personal_python2 = list(map(lambda worker: worker['name'], all_personal_python2))



    all_personal_platzi = [worker['name'] for worker in LIST if worker['organization'] == 'Platzi']
    
    all_personal_platzi2 = list(filter(lambda worker: worker['organization'] == 'Platzi', LIST))
    all_personal_platzi2 = list(map(lambda worker: worker['name'], all_personal_platzi2))
    
    
    adults = list(filter(lambda worker: worker['age'] >= 18, LIST))
    adults = list(map(lambda worker: worker['name'], adults))
    
    adults2 = [worker['name'] for worker in LIST if worker['age']> 18]

       
    old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, LIST))
    old_people2 = [worker | {'old': worker['age'] > 70} for worker in LIST]


    for worker in old_people2:
        print(worker)

if __name__ =='__main__':
    run()