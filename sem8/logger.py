import view
def beautiful_print():
    with open("file.txt",'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            print(line.strip())

def get_data():
    with open("file.txt", 'r') as file:
         data = file.read().split(f'\n')
         return  data

def add_data(a):
    with open("file.txt",'a') as file:
        file.write(a)


def edit_data(a, b):
    with open('file.txt', 'r') as f:
        old_data = f.read()

    new_data = old_data.replace(a, b)

    with open('file.txt', 'w') as f:
        f.write(new_data)


def delete(a):
    with open('file.txt', 'r') as f:
        old_data = f.read()

    b = ''
    new_data = old_data.replace(a, b)

    with open('file.txt', 'w') as f:
        f.write(new_data)