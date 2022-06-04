import employee as emp


class Administrative(emp.Employee):
    def __init__(self, ID, name, birthDate, martialStatus, numberOfChilds, gender,
                 contactInfo, empType, status, department, startingTime, basicSalary, isInsured, NoVacations):
        super().__init__(ID, name, birthDate, martialStatus, numberOfChilds, gender,
                         contactInfo, empType, status, department, startingTime, basicSalary, isInsured)

        self.__NoVacations = NoVacations

    @property
    def NoVacations(self):
        return self.__NoVacations

    @NoVacations.setter
    def NoVacations(self, value):
        self.__NoVacations = value
