def search(text, target):
    '''
    Функция по поиску символа в введенном тексте
    :param text: str
    :param target: str
    :return: bool
    '''
    for i in range(len(text)):
        if text[i] == target:
            result = 'True'
        else:
            result = 'False'
    return result

#Функция по выводу длины введенной строки

def length(text):
    '''
    Функция по выводу длины введенного текста
    :param text: str
    :return: int
    '''
    print(len(text))

