import abc  # we can make it abstract using this lib


class Employee:
    def __init__(self, ID, name, birthDate, martialStatus, numberOfChilds, gender,
                 contactInfo, empType, status, department, startingTime, basicSalary, isInsured):
        self.__isInsured = isInsured
        self.__basicSalary = basicSalary
        self.__startingTime = startingTime
        self.__department = department
        self.__status = status
        self.__empType = empType
        self.__contactInfo = contactInfo
        self.__gender = gender
        self.__numberOfChilds = numberOfChilds
        self.__name = name
        self.__martialStatus = martialStatus
        self.__birthDate = birthDate
        self.__ID = ID

    # setters and getters in a fancy pythonic way

    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, value):
        self.__ID = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def birthDate(self):
        return self.__birthDate

    @birthDate.setter
    def birthDate(self, value):
        self.__birthDate = value

    @property
    def martialStatus(self):
        return self.__martialStatus

    @martialStatus.setter
    def martialStatus(self, value):
        self.__martialStatus = value

    @property
    def numberOfChilds(self):
        return self.__numberOfChilds

    @numberOfChilds.setter
    def numberOfChilds(self, value):
        self.__numberOfChilds = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value

    @property
    def contactInfo(self):
        return self.__contactInfo

    @contactInfo.setter
    def contactInfo(self, value):
        self.__contactInfo = value

    @property
    def empType(self):
        return self.__empType

    @empType.setter
    def empType(self, value):
        self.__empType = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        self.__department = value

    @property
    def startingTime(self):
        return self.__startingTime

    @startingTime.setter
    def startingTime(self, value):
        self.__startingTime = value

    @property
    def basicSalary(self):
        return self.__basicSalary

    @basicSalary.setter
    def basicSalary(self, value):
        self.__basicSalary = value

    @property
    def isInsured(self):
        return self.__isInsured

    @isInsured.setter
    def isInsured(self, value):
        self.__isInsured = value
