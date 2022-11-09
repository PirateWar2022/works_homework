

def menu():
    print('Choice the action (1 - find employee, 2 - add the employee)')
    res = int(input())
    return res

def get_info():
    return input('Enter information about employee')


def new_emp():
    fio = input('FIO: ')
    date = input('Date: ')
    title = input('Title: ')
    salary = input('Salary: ')
    phone_number = input('Phone number: ')

    record = '\n' + fio + '|' + date + '|' + title + '|' + salary + '|' + phone_number

    return record
