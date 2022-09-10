def menu():
    print("Выберите действие (1 - поиск сотрудника, 2 - добавление сотрудника, 3 - редактирование, 4 - удаление)")
    res = int(input())
    return res

def get_info():
    return input("введите информацию о сотруднике: ")

def choice_info():
    pass

def change0():
    return input('введите информацию которую вы хотите заменить: ')

def change():
    return input('введите информацию на которую хотите заменить: ')



def new_emp():
    fio = input("Fio: ")
    date = input("Date: ")
    work = input("Position: ")
    salary = input("Salary: ")
    phone = input("Phone: ")

    zap ="\n" + fio + " | " + date + " | " + work + " | "  + salary + " | " + phone

    return zap