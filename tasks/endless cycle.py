HELP = """
help - Печать справки о программе
add - Добавить задачу в список, команда запрашивает у юзера название и дату
show - Вывести все добавленные задачи
exit - завершение программы
"""

tasks_tooday = []
tasks_tomorrow = []
tasks_other = []

run = True

while run:
    command = input('Введите команду: ')
    if command == 'help':
        print(HELP)
    elif command == 'show':
        print(f'Задачи на сегодня: {tasks_tooday}\nЗадачи на завтра: {tasks_tomorrow}\nПрочие задачи: {tasks_other}')
    elif command == 'add':
        task = input('Введите название задачи: ')
        date = input('Когда ее необходимо сделать? ')
        if date == 'сегодня':
            tasks_tooday.append(task)
            print(f'Задача {task} добавлена! Ее необходимо выполнить сегодня!')
        elif date == 'завтра':
            tasks_tomorrow.append(task)
            print(f'Задача {task} добавлена! Ее необходимо выполнить завтра!')
        else:
            tasks_other.append(task)
            print(f'Задача {task} добавлена! Ее необходимо выполнить не в ближайшее время!')
    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        break
    else:
        print('Неизвестная команнда, для получения списка команд введите "help"')