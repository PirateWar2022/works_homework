import view
import logger
import model_emp

def button():
    a = view.menu()
    if a == 1:
        print(model_emp.search(view.get_info()))
    elif a == 2:
        logger.add_data(view.new_emp())
        print(logger.beautiful_print())
    elif a == 3:
        model_emp.edit()
    elif a == 4:
        model_emp.delete_info()


