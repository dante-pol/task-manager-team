#Функция по поиску символа в строке

def search(text, target):
    for i in range(len(text)):
        if text[i] == target:
            result = 'True'
        else:
            result = 'False'
    return result

#Функция по выводу длины введенной строки

def length(text):
    print(len(text))

