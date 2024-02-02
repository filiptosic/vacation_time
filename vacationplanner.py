from datetime import datetime as dt
this_year = dt.now().year
print(this_year)

#create weeks of year dict

who_is_off = {}
for i in range(1, 53):
    who_is_off[i] = []

# create dict to contain weeks_of_year of entitlement

entitlement = {
    0: 1,
    1: 1,
    2: 2,
    3: 3,
    4: 3,
    5: 4,
    6: 4,
    7: 4,
    8: 4,
    9: 4,
    10: 5
}
# create start date dict for employees
start_date = []
#create employee class

class Employee:

    emp_list = []

    def __init__(self, name, hire_year, emp_number):
        self.name = name
        self.hire_year = hire_year
        self.emp_number = emp_number
        Employee.emp_list.append({"name": self.name,
                                  "hire_year": self.hire_year,
                                  "emp_number": self.emp_number})
        # start_date[self.name] = hire_year
        # self.seniority = start_date[self.name]
        try:
            self.weeks_of_entitlement = entitlement[2024 - hire_year]
        except KeyError:
            self.weeks_of_entitlement = 6
        Employee.emp_list.sort(key = lambda emp_list: emp_list['hire_year'])

    def get_desired_weeks(self):
        self.desired_weeks = []
        weeks_selected = 0
        while weeks_selected < self.weeks_of_entitlement:
            options = []
            attempts = 0
            while attempts < 3:
                try:
                    desired = int(input(f"Enter vacation week {weeks_selected + 1} option {attempts + 1} : "))
                    options.append(desired)
                except ValueError:
                    print("Please enter INT's only")
                attempts += 1
            self.desired_weeks.append(options)
            weeks_selected += 1
     
def apply_for_week(employee):
    
    for week in employee.desired_weeks[0]:
        print(week)
        if len(who_is_off[week]) < 2:
            who_is_off[week].append(employee.name)
            return True

emp1 = Employee("Jim", 2021, 175925)
emp2 = Employee("Pam", 2022, 918348)
emp3= Employee("Dwight", 2022, 192080)
emp4 = Employee("Michael", 2004, 49019)

emp1.get_desired_weeks()

emp2.get_desired_weeks()
emp3.get_desired_weeks()

apply_for_week(emp1)
apply_for_week(emp2)
apply_for_week(emp3)
print(who_is_off)




