text = 'Новый год'
target = input('Введите символ для поиска >> ')


def search(text, target):
    for i in range(len(text)):
        if text[i] == target:
            print('True')
        else:
            print('False')

def length(text):
    print(len(text))
