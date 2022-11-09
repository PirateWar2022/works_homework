import view
import logger
import mode_emp

def button():
    d = view.menu()
    if d == 1:
        print(mode_emp.search(view.get_info()))

    elif d == 2:
        print(logger.add_data(view.new_emp()))

    elif d == 3:
        mode_emp.edit()
        print(logger.edit_data())