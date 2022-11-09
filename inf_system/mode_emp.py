import logger
import view

def search(emp):
    book = logger.get_data()
    ans = []
    flag = False
    for i in book:
        if i.find(emp) != -1:
            flag = True
        if flag == True:
            return ans
        else:
            return 'Not find'



def edit():
    book = logger.get_data()
    emp = view.get_info()
    for i in range(len(book)):
        if book[i].find(emp) != -1:
            book[i] = view.new_emp()
    logger.edit_data(book)