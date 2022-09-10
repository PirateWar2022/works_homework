import view

def get_data():
    with open('file.txt', 'r') as f:
        data = f.read().split('\n')
        return data

def add_data(a):
    with open('file.txt', 'a') as f:
        f.write(a)

def edit_data(a):
    with open('file.txt', 'w') as f:
        f.write(str(a))