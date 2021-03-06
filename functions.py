import administrative
import employee as emp
import academic
import admin
import datetime
from datetime import date

import re

"""
       Color Codes
Black: \033[0;30m
Red: \033[0;31m
Green: \033[0;32m
Yellow: \033[0;33m
Blue: \033[0;34m
Magenta: \033[0;35m
Cyan: \033[0;36m
White: \033[0;37m
        Style
Normal: \033[0;3?m
Bold:   \033[1;3?m
Reset: \033[0m
"""


def Admin_stastics():
    for key1 in DATA_BASE:
        if (DATA_BASE[key1].empType == "Administrative"):
            print("employee:" + DATA_BASE[key1].ID)
            n = sum(int(x) for x in DATA_BASE[key1].NoVacations.values())
            print("total numbers of vacations for this employee : ")
            print(n)
            print("avg numbers  per year  for this employee : ")
            print(n / len(DATA_BASE[key1].NoVacations))


def line():
    print("===================================================================")


def checkEmail(s):
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if re.match(pat, s):
        return True
    return False


def menu():
    print("1. Add a new employee record\n"
          "2. Update general attributes\n"
          "3. Add/update administrative employee attribute:\n"
          "4. Add/update academic employee attribute:\n"
          "5. Employee’s statistics\n"
          "6. Salary statistics\n"
          "7. Retirement information\n"
          "8. Courses statistics:\n"
          "9. Administrative employees’ statistics:\n"
          "10.Academic employees’ statistics:\n"
          "-1. EXIT"

          )
    line()


def welcome():
    green()
    print("                 _                              \n"
          "                | |                             \n"
          " __      __ ___ | |  ___  ___   _ __ ___    ___ \n"
          " \\ \\ /\\ / // _ \\| | / __|/ _ \\ | '_ ` _ \\  / _ \\\n"
          "  \\ V  V /|  __/| || (__| (_) || | | | | ||  __/\n"
          "   \\_/\\_/  \\___||_| \\___|\\___/ |_| |_| |_| \\___|\n"
          "                                                \n"
          "                                                \n")
    reset()


def green():
    print("\033[0;32m")


def reset():
    print("\033[0m")


def red():
    print("\033[0;31m")


# what u can do: make the 2 classes,  handle when indx 7 what object you will use and add then in to the constructor!!

DATA_BASE = {}


# DATA_BASE["faris"] = 1

def readAcademic(fileName, id):
    expDict = {}

    try:
        with open(fileName) as ACA:
            Lines = ACA.readlines()
            for line in Lines:
                splited = line.split(';')
                if splited[0] == "Employee ID":
                    continue

                if splited[0].strip() == id:
                    year_sem = str(splited[1].strip()) + '-' + str(splited[2].strip())
                    coursesInSem = splited[3].strip()
                    coursesInSem = coursesInSem.split(" ")

                    expDict[year_sem] = coursesInSem
        return expDict

    except FileNotFoundError:
        red()
        print('FILE NOT FOUND!')
        reset()
        exit(1)

        return


def AdminRead(fileName, id):
    NoVacations = {}

    try:
        with open(fileName) as AD:
            lines = AD.readlines()
            for line in lines:
                splited = line.split(';')
                if splited[0] == "Employee ID":
                    continue

                if splited[0].strip() == id:
                    year = splited[1].strip()
                    NumberOfVacations = splited[2].strip()
                    NoVacations[year] = NumberOfVacations

        return NoVacations


    except FileNotFoundError:
        red()
        print('FILE NOT FOUND!')
        reset()
        exit(1)

        return


def readGA(fileName):
    AcaFile = ""
    AcaFlag = int(1)
    AdminFile = ""
    AdminFlag = int(1)

    try:
        with open(fileName) as GA:
            Lines = GA.readlines()

            for line in Lines:
                line = line.strip()

                # print(line)
                splited = line.split(';')
                fullName = splited[1]
                fullName = fullName.split(',')
                # print(fullName) # 0:first 1:mid , 2:last
                contactInfo = splited[6]
                contactInfo = contactInfo.split(',')  # email , num, fax
                TYPE = splited[7]  # THE FLAG! SO U CAN HANDLE THE TYPE OF EMPLOYEE
                # print(TYPE)

                if TYPE.strip() == "Type":
                    continue

                if TYPE.strip().lower() == "administrative":
                    # print(splited[0])
                    if AdminFlag == 1:
                        print('input admin file name:')
                        AdminFile = input()

                        # AdminFile = "Administrative.txt"

                        AdminFlag = 0
                    NoVacations = AdminRead(AdminFile, splited[0].strip())
                    tmpAdmin = administrative.Administrative(splited[0].strip(), fullName, splited[2].strip(),
                                                   splited[3].strip(),
                                                   splited[4].strip(), splited[5].strip(), splited[6].strip(),
                                                   splited[7].strip(), splited[8].strip(),
                                                   splited[9].strip(), splited[10].strip(), splited[11].strip(),
                                                   splited[12].strip(), NoVacations)

                    # print(tmpAcademic.academicExp)
                    DATA_BASE[tmpAdmin.ID] = tmpAdmin
                    # print(NoVacations)



                elif TYPE.strip().lower() == "academic":

                    """
                    ID, name, birthDate, martialStatus, numberOfChilds, gender,
                     contactInfo, empType, status, department, startingTime, basicSalary, isInsured, academicExp):

                    """
                    if AcaFlag == 1:
                        print('input academic file name:')
                        AcaFile = input()
                        # AcaFile = "Academic.txt"

                        AcaFlag = 0

                    expDict = readAcademic(AcaFile, splited[0].strip())
                    # print(expDict)

                    tmpAcademic = academic.Academic(splited[0].strip(), fullName, splited[2].strip(),
                                                    splited[3].strip(),
                                                    splited[4].strip(), splited[5].strip(), splited[6].strip(),
                                                    splited[7].strip(), splited[8].strip(),
                                                    splited[9].strip(), splited[10].strip(), splited[11].strip(),
                                                    splited[12].strip(), expDict)

                    # print(tmpAcademic.academicExp)
                    DATA_BASE[tmpAcademic.ID] = tmpAcademic

                    # print('s')

                else:
                    print("INVALID TYPE!")

                # print(splited)



    except FileNotFoundError:
        print('FILE NOT FOUNDdd!')
        exit(1)

        return


def cmd2():
    tmpEmp = ''
    print('PLEASE INPUT EMPLOYEE ID :  ')
    ID = input()
    if DATA_BASE.__contains__(ID):
        tmpEmp = DATA_BASE[ID]

    else:

        red()
        print('ID NOT FOUND!')
        reset()

        return

    while True:
        green()
        print('input -1 to exit this mode')
        reset()

        atrb = input(
            'CHANGE:\n1)Name{First Name, Middle Name,Last Name}\n2)Date of birth \n3)Martial status\n4)Number of childs\n5)Gender\n'
            '6)Contact information {email, mobile number, fax}\n7)Type\n8)Status\n9)Department\n10)Starting Time\n11)Basic Salary\n12)health insurance  ')

        if atrb.lower() == '1':
            newName = ['', '', '']
            newName[0] = input('PLEASE INPUT NEW FIRST  NAME  ')
            newName[1] = input('PLEASE INPUT NEW MID NAME  ')
            newName[2] = input('PLEASE INPUT NEW LAST NAME ')

            tmpEmp.name = newName

        elif atrb.lower() == "2":
            while True:
                try:
                    birthDate = (input("INPUT NEW BIRTH DATE  "))
                    datetime.datetime.strptime(birthDate, '%d/%m/%Y')
                except ValueError:
                    red()
                    print('INVALID DATE ')
                    reset()
                    continue
                tmpEmp.birthDate = birthDate

                break




        elif atrb.lower() == '3':

            while True:
                martialStatus = (input("INPUT NEW martial Status 'single' 'maried'  "))
                if martialStatus.lower() != 'single' and martialStatus.lower() != 'maried':
                    red()
                    print('INVALID STATUS   ')
                    reset()
                    print('TRY AGAIN ')
                    continue
                tmpEmp.martialStatus = martialStatus
                break

        elif atrb.lower() == '4':
            numberOfChilds = input("INPUT NEW NUMBER  OF CHILDS")
            tmpEmp.numberOfChilds = numberOfChilds

        elif atrb.lower() == '5':
            while True:

                gender = (input("INPUT NEW gender   "))

                if gender.lower() != 'male' and gender.lower() != 'female':
                    red()
                    print('INVALID gender   ')
                    reset()
                    print('TRY AGAIN ')
                    continue

                tmpEmp.gender = gender
                break

        elif atrb.lower() == '6':
            contactInfo = ['', '', '']

            while True:

                contactInfo[0] = (input("INPUT E-MAIL "))

                if not checkEmail(contactInfo[0]):
                    red()
                    print('INVALID contactInfo  ')
                    reset()
                    print('TRY AGAIN ')
                    continue
                break

            while True:
                contactInfo[1] = input('MOBILE NUMBER ')
                if len(contactInfo[1]) != 10:
                    red()
                    print('INVALID MOBLIE NUMBER! (must be 10 digits)')
                    reset()
                    continue
                break

            contactInfo[2] = input('NEW FAX NUMBER ')

            tmpEmp.contactInfo = contactInfo


        elif atrb.lower() == '8':
            while True:
                status = (input("INPUT  status 'Part-time' 'Full-time' 'left-university' "))
                if status.lower() != 'part-time' and status.lower() != 'full-time' and status.lower() != 'left-university':
                    red()
                    print('INVALID INPUT   ')
                    reset()
                    print('TRY AGAIN ')
                    continue

                break

                tmpEmp.status = status

                break

        elif atrb == '9':
            department = (input("INPUT NEW department   "))
            tmpEmp.department = department


        elif atrb == '10':
            while True:
                startingTime = (input("INPUT starting time  month:  "))
                if int(startingTime) > 12 or int(startingTime) <= 0:
                    red()
                    print("INVALID MONTH")
                    reset()
                    continue

                break
            while True:
                startingTimeYear = (input("INPUT starting time  year:  "))
                if int(startingTimeYear) > int(date.today().year):
                    red()
                    print("YOU HAVEN'T STARTED IN THE FUTURE DO YOU ??")
                    reset()
                    continue
                break

            startingTime = str(startingTime) + '/' + str(startingTimeYear)

            tmpEmp.startingTime = startingTime


        elif atrb == '11':
            basicSalary = (input("INPUT NEW basic Salary "))
            tmpEmp.basicSalary = basicSalary

        elif atrb == '12':
            while True:
                isInsured = (input("INPUT NEW HEALTH INSURANCE STATUS (true or false) "))
                if isInsured.lower() != 'true' and isInsured.lower() != 'false':
                    red()
                    print('INVALID INPUT   ')
                    reset()
                    print('TRY AGAIN ')
                    continue

                tmpEmp.isInsured = isInsured
                break

        elif atrb == '7':

            while True:
                empType = (input("INPUT NEW Type (academic or  administrative ) "))
                if empType.lower() != "academic" and empType.lower() != 'administrative':
                    red()
                    print('INVALID INPUT   ')
                    reset()
                    print('TRY AGAIN ')
                    continue
                tmpEmp.empType = empType
                break


        elif atrb == '-1':
            return




        else:
            red()

            print("INVALID INPUT")

            reset()

            """
            self, ID, name, birthDate, martialStatus, numberOfChilds, gender,
                 contactInfo, empType, status, department, startingTime, basicSalary, isInsured):

            """


def cmd4():
    print('PLEASE INPUT EMPLOYEE ID :  ')
    ID = input()
    if not DATA_BASE.__contains__(ID):
        red()
        print("ID DOESN'T EXIST")
        reset()
        return
    if DATA_BASE[ID].empType.lower() != 'academic':
        red()
        print("NOT AN ACADEMIC EMPLOYEE ")
        reset()
        return

    if DATA_BASE[ID].status.lower().strip() == "left-university":
        red()
        print("EMPLOYEE LEFT THE UNIVERSITY")
        reset()
        return

    print("PLEASE INPUT YEAR ")

    while True:

        year = input()

        if int(year) < int(DATA_BASE[ID].startingTime.split('/')[1]):
            red()
            print('YEAR MUST NOT BE LESS THAN STARTING YEAR')
            reset()
            continue

        break

    while True:
        sem = input("PLEASE INPUT SEMESTER ")
        if int(sem) > 3 or int(sem) <= 0:
            red()
            print('INVALID SEMSETER (MUST BE 1 OR 2 OR 3 ')
            reset()
            continue

        break

    year_sem = str(year).strip() + '-' + str(sem).strip()
    courses = []

    while True:

        print("input courses in this semester, press -1 to quit adding courses")
        tmpCourse = input()

        if tmpCourse == '-1':
            break

        courses.append(tmpCourse)
    DATA_BASE[ID].academicExp[year_sem] = courses

    print(DATA_BASE[ID].academicExp[year_sem])


def canServe(x):
    year = x.birthDate
    year = year.split('/')
    year = year[2]

    sTime = x.startingTime
    sTime = sTime.split('/')
    sTime = sTime[1]

    if abs(int(date.today().year) - int(year) <= 64 and (int(date.today().year) - int(sTime)) < 35):

        return True
    else:
        return False


def cmd7():
    for key, val in DATA_BASE.items():
        if canServe(val):
            print(val.name[0].strip(), val.name[1].strip(), val.name[2].strip())


def cmd10():
    for key, val in DATA_BASE.items():
        cnt = int(0)

        if val.empType.lower() == 'academic':
            print("EMPLOYEE: ", val.ID, val.name[0])
            for key2, val2 in val.academicExp.items():
                cnt += len(val2)

            print("number of courses employee taught: {}".format((cnt)))
            try:
                print("The average number of courses the employee taught per semester: {:.2f} ".format(
                    cnt / val.academicExp.__len__()))

            except ZeroDivisionError:
                continue


        print("----------------------------------------------------------------------")


def Admin_stastics():
    for key1 in DATA_BASE:
        if (DATA_BASE[key1].empType.strip().lower() == "administrative"):
            print("employee:" + DATA_BASE[key1].ID)
            n = sum(int(x) for x in DATA_BASE[key1].NoVacations.values())
            print("total numbers of vacations for this employee : ")
            print(n)
            print("avg numbers  per year  for this employee : ")
            print(n / len(DATA_BASE[key1].NoVacations))


def cmd1():
    green()

    print("PLEASE INPUT NEW EMPLOYEE RECORD: ")

    while True:

        ID = input("PLEASE INPUT ID ")
        if len(ID) != 5:
            red()
            print('ID MUST BE 5 DIGITS LENGTH')
            reset()
            continue

        if not ID.isnumeric():
            red()
            print('ID MUST BE DIGITS only LENGTH')
            reset()
            continue

        break

    if DATA_BASE.__contains__(ID):
        red()
        print("ID ALREADY EXIST")
        reset()
        return

    name = ['', '', '']
    name[0] = input('PLEASE  INPUT FIRST  NAME  ')
    name[1] = input('PLEASE INPUT MID NAME  ')
    name[2] = input('PLEASE INPUT LAST NAME ')

    while True:
        try:
            birthDate = (input("INPUT NEW BIRTH DATE  'dd/mm/yy' "))
            datetime.datetime.strptime(birthDate, '%d/%m/%Y')
        except ValueError:
            red()
            print('INVALID DATE ')
            reset()
            continue
        break
    while True:
        martialStatus = (input("INPUT NEW martial Status 'single' 'maried'  "))
        if martialStatus.lower() != 'single' and martialStatus.lower() != 'maried':
            red()
            print('INVALID MARTIAL STATUS   ')
            reset()
            print('TRY AGAIN ')
            continue
        break

    numberOfChilds = (input("input  number of childs   "))

    while True:

        gender = (input("INPUT  gender   "))

        if gender.lower() != 'male' and gender.lower() != 'female':
            red()
            print('INVALID gender   ')
            reset()
            print('TRY AGAIN ')
            continue
        break

    contactInfo = ['', '', '']

    while True:

        contactInfo[0] = (input("INPUT E-MAIL "))

        if not checkEmail(contactInfo[0]):
            red()
            print('INVALID contactInfo  ')
            reset()
            print('TRY AGAIN ')
            continue
        break

    while True:
        contactInfo[1] = input('MOBILE NUMBER ')
        if len(contactInfo[1]) != 10:
            red()
            print('INVALID MOBLIE NUMBER! (must be 10 digits)')
            reset()
            continue
        break

    contactInfo[2] = input('NEW FAX NUMBER ')

    while True:
        status = (input("INPUT  status 'Part-time' 'Full-time' 'left-university' "))
        if status.lower() != 'part-time' and status.lower() != 'full-time' and status.lower() != 'left-university':
            red()
            print('INVALID INPUT   ')
            reset()
            print('TRY AGAIN ')
            continue

        break

    department = (input("INPUT NEW department   "))

    while True:
        startingTime = (input("INPUT starting time  month:  "))
        if int(startingTime) > 12 or int(startingTime) <= 0:
            red()
            print("INVALID MONTH")
            reset()
            continue

        break

    while True:
        startingTimeYear = (input("INPUT starting time  year:  "))
        if int(startingTimeYear) > int(date.today().year):
            red()
            print("YOU HAVEN'T STARTED IN THE FUTURE DO YOU ??")
            reset()
            continue
        break

    startingTime = str(startingTime) + '/' + str(startingTimeYear)

    basicSalary = (input("INPUT NEW basicSalary "))

    while True:
        isInsured = (input("INPUT 'true' 'false' for health insurance  "))
        if isInsured.lower().strip() != 'true' and isInsured.lower().strip() != 'false':
            red()
            print('INVALID INPUT   ')
            reset()
            print('TRY AGAIN ')
            continue
        break

    while True:
        empType = (input("INPUT  Type  'academic' 'administrative' "))
        if empType.lower().strip() != "academic" and empType.lower() != 'administrative':
            red()
            print('INVALID INPUT   ')
            reset()
            print('TRY AGAIN ')
            continue
        break

    reset()

    # tmpEmp = emp.Employee(ID, birthDate, martialStatus, numberOfChilds, gender, contactInfo, empType, status,
    #                       department, startingTime, basicSalary, isInsured)
    emptyDict = {}

    if empType.strip().lower() == "academic":
        newEmp = academic.Academic(ID, name, birthDate, martialStatus, numberOfChilds, gender, contactInfo, empType,
                                   status,
                                   department, startingTime, basicSalary, isInsured, emptyDict)

    elif empType.strip().lower() == "administrative":

        newEmp = admin.Administrative(ID, name, birthDate, martialStatus, numberOfChilds, gender, contactInfo, empType,
                                      status,
                                      department, startingTime, basicSalary, isInsured, emptyDict)
    else:
        red()
        print('INVALID TYPE')
        reset()
        return

    DATA_BASE[newEmp.ID] = newEmp


def salary_satstics():
    SalDect = {}
    total_Admin = 0
    total_Acadimic = 0
    nAdmin = 0
    nAcadimic = 0
    for key1 in DATA_BASE:
        if (DATA_BASE[key1].empType.lower().strip() == "administrative"):
            nAdmin += 1
            Final_Salary = int(DATA_BASE[key1].basicSalary)
            if (DATA_BASE[key1].martialStatus.lower().strip() == 'maried' and DATA_BASE[
                key1].isInsured.lower().strip() == 'true'):
                Final_Salary = Final_Salary + 20 + (
                        15 * (int(DATA_BASE[key1].numberOfChilds)) - 12 * (
                            1 + (1 + int(DATA_BASE[key1].numberOfChilds))))
            elif (DATA_BASE[key1].martialStatus.lower().strip() == 'maried' and DATA_BASE[
                key1].isInsured.lower().strip() == 'false'):
                Final_Salary = Final_Salary + 20 + (
                        15 * (int(DATA_BASE[key1].numberOfChilds)))
            total_Admin += Final_Salary
            SalDect[key1] = Final_Salary


        elif (DATA_BASE[key1].empType.lower().strip() == "academic"):
            nAcadimic += 1
            Final_Salary = int(DATA_BASE[key1].basicSalary)
            if (DATA_BASE[key1].martialStatus.lower() == 'maried' and DATA_BASE[key1].isInsured == 'true'):
                Final_Salary = Final_Salary + 20 + (
                        15 * (int(DATA_BASE[key1].numberOfChilds)) - 12 * (
                            1 + (1 + int(DATA_BASE[key1].numberOfChilds))))
            elif (DATA_BASE[key1].martialStatus.lower() == 'maried' and DATA_BASE[key1].isInsured == 'false'):
                Final_Salary = Final_Salary + 20 + (
                        15 * (int(DATA_BASE[key1].numberOfChilds)))
            total_Acadimic += Final_Salary
            SalDect[key1] = Final_Salary
    try:
        print("Average salary for Adminstrative employee is : " + str(total_Admin / nAdmin))
    except ZeroDivisionError:
        print("No Administrative employees :( ")


    try:
        print("Average salary for Acadimic empolyee is : " + str(total_Acadimic / nAcadimic))
    except ZeroDivisionError:
        print(" No Administrative employees :(")

    print("enter a number to print the names of all employees above it  ")
    numberr = input()
    for key in SalDect:
        if (SalDect[key] >= int(numberr)):
            print(DATA_BASE[key].name)


def emp_stastics():
    nAdmin = 0
    nAcadimic = 0
    nMale = int(0)
    nFemale = 0
    nFull = 0

    for key1 in DATA_BASE:

        if (DATA_BASE[key1].gender.lower().strip() == "male"):
            nMale += 1

        if (DATA_BASE[key1].empType.lower().strip() == "administrative"):
            nAdmin += 1
        elif (DATA_BASE[key1].empType.lower().strip() == "academic"):
            nAcadimic += 1
        if (DATA_BASE[key1].status.lower().strip() == "full-time"):
            nFull += 1

    nFemale = len(DATA_BASE) - int(nMale)
    print("Number of academic employees :" + str(nAcadimic))
    print("Number of administrative employees :" + str(nAdmin))
    print("Number of male employees :" + str(nMale))
    print("Number of female employees :" + str(nFemale))
    print("percantege of full time employees :" + str((nFull / len(DATA_BASE)) * 100))


def c3():
    print("enter employee id :")
    n = input()
    if not DATA_BASE.__contains__(n):
        red()
        print("ID NOT FOUND !")
        reset()
        return

    if (DATA_BASE[n].empType.strip().lower() == "administrative"):
        if n.strip() in DATA_BASE:
            if (DATA_BASE[n].status.lower().strip() != "left-university"):

                while True:
                    print("please enter year .")
                    year = input()
                    if int(year) < int(DATA_BASE[n].startingTime.split('/')[1]):
                        red()
                        print('YEAR MUST NOT BE LESS THAN STARTING YEAR')
                        reset()
                        continue

                    break





                print("please enter number of vacation days .")
                day = input()



                if (year.strip() in DATA_BASE[n].NoVacations):
                    DATA_BASE[n].NoVacations.update(
                        {year: DATA_BASE[n].NoVacations[year], year: DATA_BASE[n].NoVacations[year] + day})
                else:
                    DATA_BASE[n].NoVacations[year] = day


            else:
                print(" this employee has left the uni ")
                reset()
                return
        else:
            print("no user with such id exists ")
            reset()
            return

    else:
        print("this isn't an administrative employee")
        reset()
        return



def cmd8():

    coursesSet =set([])
    coursesSet = set(coursesSet)

    for key, val in DATA_BASE.items():
        if  val.empType.lower() == 'academic':

            for key2, course in  val.academicExp.items():
                for c in course:
                    coursesSet.add(c)



    for course in coursesSet:
        SETTTTTTT = set([])

        cnt = int(0)
        print(course)

        for key, val in DATA_BASE.items():
            if val.empType.lower() == 'academic':

                for key2, course2 in val.academicExp.items():
                    for c in course2:
                        if c == course:
                            cnt += 1
                            SETTTTTTT.add(key2)

        print("NUMBER OF TIMES TAUGHT:", cnt,"NUMBER OF TEACHERS TAUGHT IT ", len(SETTTTTTT))


