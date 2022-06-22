from operator import concat


def hello(message):
    return message + ' ' + 'and'


first_message = hello(input('tipe your message!!! '))
second_message = input('tipe your second message!!')
print('You tiped --', str(first_message) + ' ', str(second_message))
print(f'You tiped -- {first_message} {second_message}')
print('ЭТО еще одно изменение из клонированного репозитория')
