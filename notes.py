from random import choice as choice

HELP = """
help - Печать справки о программе
add - Добавить задачу в список, команда запрашивает у юзера название и дату
show - Вывести все добавленные задачи
random - добавление случайной задачи на сегодня
exit - завершение программы
"""
tasks = {}
RANDOM_TASKS = ('Улыбнуться', 'Позвонить родителям', 'Сделать зарядку', 'Сходить погулять')

run = True

def add_task(task, date):
    if date in tasks:
        tasks[date].append(task)
    else:
        tasks[date] = [task]
    print(f'Задача "{task}" добавлена! Её необходимо сделать {date}!')

def show_tasks():
    date = input('Введите дату для отображения списка задач: ')
    date.lower
    if date in tasks:
        print(f'На {date} запланированные следующие задачи:')
        for task in tasks[date]:
            print(f'- {task}')

while run:
    command = input('Введите команду: ')
    if command == 'help':
        print(HELP)
    elif command == 'show':
        show_tasks()
    elif command == 'add':
        task = input('Введите название задачи: ')
        date = input('Когда ее необходимо сделать? ')
        date.lower
        add_task(task, date)
    elif command == 'random':
        task = choice(RANDOM_TASKS)
        add_task(task, 'сегодня')
    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        break
    else:
        print('Неизвестная команнда, для получения списка команд введите "help"')