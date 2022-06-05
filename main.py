import employee as emp
import academic
import admin
import datetime
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


def checkEmail(s):
   pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(pat,s):
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
          "10.Academic employees’ statistics:"
          )


def welcom():
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
        return


def AdminRead(fileName, id):
    NoVacations = {}

    try:
        with open(fileName) as ACA:
            lines = ACA.readlines()
            for line in lines:
                splited = line.split(';')
                if splited[0] == "Employee ID":
                    continue

                if splited[0].strip() == id:
                    year = str(splited[1].strip())
                    NumberOfVacations = splited[2].strip()
                    NoVacations[year] = NumberOfVacations

        return NoVacations


    except FileNotFoundError:
        red()
        print('FILE NOT FOUND!')
        reset()
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

                if TYPE.strip() == "Administrative":

                    if AdminFlag == 1:
                        # print('input admin file name:')
                        # AdminFile = input()
                        AdminFile = "Administrative.txt"

                        AdminFlag = 0



                elif TYPE.strip() == "Academic":

                    """
                    ID, name, birthDate, martialStatus, numberOfChilds, gender,
                     contactInfo, empType, status, department, startingTime, basicSalary, isInsured, academicExp):

                    """
                    if AcaFlag == 1:
                        # print('input academic file name:')
                        # AcaFile = input()
                        AcaFile = "Academic.txt"

                        AcaFlag = 0

                    expDict = readAcademic(AcaFile, splited[0].strip())
                    # print(expDict)

                    tmpAcademic = academic.Academic(splited[0].strip(), fullName, splited[2].strip(),
                                                    splited[3].strip(),
                                                    splited[4].strip(), splited[5].strip(), splited[6].strip(),
                                                    splited[7].strip(), splited[8].strip(),
                                                    splited[9].strip(), splited[10].strip(), splited[11].strip(),
                                                    splited[12].strip(), expDict)

                    print(tmpAcademic.academicExp)
                    DATA_BASE[tmpAcademic.ID] = tmpAcademic

                    # print('s')

                else:
                    print("INVALID TYPE!")

                # print(splited)



    except FileNotFoundError:
        print('FILE NOT FOUNDdd!')
        return


def cmd1():
    green()

    print("PLEASE INPUT NEW EMPLOYEE RECORD: ")
    ID = input("PLEASE INPUT ID ")
    name =['','','']
    name[0] = input('PLEASE  INPUT FIRST  NAME  ')
    name[1] = input('PLEASE INPUT MID NAME  ')
    name[2] = input('PLEASE INPUT LAST NAME ')

    while True:
        try:
            birthDate = (input("INPUT NEW BIRTH DATE  "))
            datetime.datetime.strptime(birthDate, '%d/%m/%Y')
        except ValueError:
            red()
            print('INVALID DATE ')
            reset()
            continue
        break
    while True:
        martialStatus = (input("INPUT NEW martialStatus "))
        if martialStatus.lower() != 'single' and martialStatus.lower() != 'Maried' :
            red()
            print('INVALID STATUD   ')
            reset()
            print('TRY AGAIN ')
            continue
        break

    numberOfChilds = (input("INPUT NEW numberOfChilds   "))

    while True:

        gender = (input("INPUT NEW gender   "))

        if gender.lower() != 'male' and gender.lower() != 'female' :
            red()
            print('INVALID gender   ')
            reset()
            print('TRY AGAIN ')
            continue
        break

    while True:

        contactInfo = (input("INPUT NEW contactInfo "))

        if not checkEmail(contactInfo):
            red()
            print('INVALID contactInfo  ')
            reset()
            print('TRY AGAIN ')
            continue
        break


    while True:
        status = (input("INPUT NEW status   "))
        if status.lower() != 'part-time' and status.lower() != 'full-time':
            red()
            print('INVALID INPUT   ')
            reset()
            print('TRY AGAIN ')
            continue
        break


    department = (input("INPUT NEW department   "))
    startingTime = (input("INPUT NEW startingTime   "))
    basicSalary = (input("INPUT NEW basicSalary "))

    while True:
        isInsured = (input("INPUT NEW isInsured "))
        if isInsured.lower() != 'true' and isInsured.lower() != 'false':
            red()
            print('INVALID INPUT   ')
            reset()
            print('TRY AGAIN ')
            continue
        break



    while True:
        empType = (input("INPUT NEW Type "    ))
        if empType.lower() != "academic" and empType.lower() != 'administrative':

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

    if empType.strip() == "academic" :
        newEmp  = academic.Academic(ID,name, birthDate, martialStatus, numberOfChilds, gender, contactInfo, empType, status,
                                    department, startingTime, basicSalary, isInsured,emptyDict)

    elif empType.strip() == "administrative":

        newEmp = admin.Administrative(ID,name, birthDate, martialStatus, numberOfChilds, gender, contactInfo, empType, status,
                                   department, startingTime, basicSalary, isInsured, emptyDict)
    else:
        red()
        print('INVALID TYPE')
        reset()
        return

    DATA_BASE[newEmp.ID] = newEmp


def main():
    # e1 = emp.Employee(1,1,1,23,3,12321,3,1,23,13,2,3,4)
    # e1.name = 'faris'
    # print(e1.name)
    #
    welcom()
    # print('GENERAL EMPLOYEE DATA FILES: ')
    # GAFile = input()
    GAFile = "GAttributes.txt"
    readGA(GAFile)

    while True:
        menu()
        ch = int(input("PLEASE SELECT A NUMBER  "))

        if ch == 1:
            for key, val in DATA_BASE.items():
                print(key,val)
            cmd1()
            print(DATA_BASE)
            print(DATA_BASE['1'].name)




        elif ch == 2:
            print('')

        elif ch == 2:
            print('')
        elif ch == 2:
            print('')
        elif ch == 2:
            print('')
        elif ch == 2:
            print('')
        elif ch == 2:
            print('')
        elif ch == 2:
            print('')
        elif ch == -1:
            green()
            print("THANK YOU COME AGAIN ")

            reset()
            return


if __name__ == '__main__':
    main()

"""
GAttributes.txt
Administrative.txt
Academic.txt

"""
