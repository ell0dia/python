# Создать сотрудника Mary, пользуясь классом
# Employee и перенести его в другую программу,
# используя модуль Pickle и файловую систему.
# Узнать про + и - модуля Pickle.


import pickle


class Employee:
    def __init__(self, name, salary, phone, department):
        self.name = name
        self.salary = salary
        self.phone = phone
        self.department = department


new_employee = Employee('Mary', 40000, +996789078, 'QA')
file = open('info.txt', 'wb')
pickle.dump(new_employee, file)
file.close()


file = open('info.txt', 'rb')
employee_info = pickle.load(file)
file.close()


