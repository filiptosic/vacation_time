class Seniority_List:
    seniority = {}
    def __init__(self, hire_date, name):
        self.hire_date = hire_date
        self.name = name
        start_date[self.name] = self.hire_date

    def get_seniority(self):
        seniority_level = start_date[self.name]
        return seniority_level