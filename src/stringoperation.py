#  функция для конкатинации двух строк: str1 и str2
def concatenation(str1: str,str2: str ) -> str:
    return str1 + str2

#  функция для овторения строки str3  num раз
def repetition(str3: str, num1: int) -> str:
    return str3 * num1

#  функция для поиска str4  в str5
def search_inline(str4: str, str5: str) -> bool:
    if str4 in str5:
        return True
    else:
        return False