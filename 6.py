def int_func(txt):
    Text = text[0].upper() + text[1:].lower()
    return Text
    '''
    Get the word capitalised
    :param text: str
    :return: int_func: str
    '''
text = input("Введите любое слово латинскими буквами: ")
print(int_func('txt'))

string = input("Введите слова через пробел: ")
for text in string.split(' '):
    print(f'{int_func(text)}', end=' ')
