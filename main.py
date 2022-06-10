from functions import *





def main():
    # e1 = emp.Employee(1,1,1,23,3,12321,3,1,23,13,2,3,4)
    # e1.name = 'faris'
    # print(e1.name)
    #
    line()

    welcome()
    line()
    print('PLEASE INPUT GENERAL EMPLOYEES DATA FILE: ')
    GAFile = input()
    # GAFile = "GAttributes.txt"
    readGA(GAFile)

    while True:
        # for key, val in DATA_BASE.items():
        #     print(key, val.name)
        menu()
        #

        ch = (input("PLEASE SELECT A NUMBER  "))

        if ch == '1':
            # for key, val in DATA_BASE.items():
            #     print(key, val.name)
            #

            cmd1()
            # print(DATA_BASE)
            # if DATA_BASE.__contains__('1'):
            #     print(DATA_BASE['1'].name)

            for key, val in DATA_BASE.items():
                print(key, val.name)

            line()
            print('')


        elif ch == '2':
            cmd2()
            line()
            print('')

        elif ch == '3':
            # omar
            print('')
        elif ch == '4':

            cmd4()
            print('')
        elif ch == '5':
           emp_stastics()
           line()
           print('')
        elif ch == '6':
            # omar

            print('')
        elif ch == '7':
            cmd7()
            line()
            print('')
        elif ch == '8':
            # omar

            print('')


        elif ch == '9':

            Admin_stastics()
            line()
            print('')
            

        elif ch == '10':
            cmd10()
            line()
            print('')


        elif ch == '-1':
            green()
            print("THANK YOU COME AGAIN ")

            reset()
            return
        else:
            red()
            print('INVALID INPUT TRY AGAIN')
            reset()


if __name__ == '__main__':
    main()

"""
GAttributes.txt
Administrative.txt
Academic.txt

"""
