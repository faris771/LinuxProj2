import employee as emp


class Academic(emp.Employee):
    def __init__(self, ID, name, birthDate, martialStatus, numberOfChilds, gender,
                 contactInfo, empType, status, department, startingTime, basicSalary, isInsured, academicExp):
        super().__init__(ID, name, birthDate, martialStatus, numberOfChilds, gender,
                         contactInfo, empType, status, department, startingTime, basicSalary, isInsured)

        self.__academicExp = academicExp

    @property
    def academicExp(self):
        return self.__academicExp

    @academicExp.setter
    def academicExp(self, value):
        self.__academicExp = value

