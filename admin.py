import employee as emp


class Admin(emp.Employee):
    def __init__(self, ID, name, birthDate, martialStatus, numberOfChilds, gender,
                 contactInfo, empType, status, department, startingTime, basicSalary, isInsured, numOfVacations):
        super().__init__(ID, name, birthDate, martialStatus, numberOfChilds, gender,
                         contactInfo, empType, status, department, startingTime, basicSalary, isInsured)

        self.__numOfVacations = numOfVacations


        @property
        def numOfVacations(self):
            return self.__numOfVacations

        @numOfVacations.setter
        def numOfVacations(self, value):
            self.__numOfVacations = value


