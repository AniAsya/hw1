def print_personal_info(name, surname, year_of_birth, city_of_residence, email, tel_number):
    personal_info = f'{surname} {name}, {year_of_birth}, {city_of_residence}, {email}, {tel_number}'
    return personal_info
    '''
    Get personal information, write it down in one line
    :param name: str
    :param surname: str
    :param year_of_birth: int
    :param city_of_residence: str
    :param email: str
    :param tel_number: str
    :return: personal_info: str 
    '''

print(print_personal_info(name = 'Анна', surname = 'Аверина', year_of_birth = 1975, city_of_residence = 'Москва', email = 'oio@bk.ru', tel_number = '93874'))

