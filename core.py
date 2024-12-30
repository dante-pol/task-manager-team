from random import randint
import os

def add_task(title: str, description: str, status='undone'):
    Folder = 'datas'
    exit = True
    while exit == True:
        id = str(randint(1000, 9999))
        if Folder not in os.listdir('task-manager-team'):
            os.makedirs(Folder)
        if id in os.listdir(Folder):
            exit = True
        else:
            exit = False
    file = open(os.path.join(Folder, id), 'w')
    file.write(f'{id};{title};{description};{status}')



