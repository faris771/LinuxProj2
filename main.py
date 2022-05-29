import employee as emp

#what u can do: make the 2 classes,  handle when indx 7 what object you will use and add then in to the constructor!!


def readGA(fileName):


    try:
        with open(fileName) as GA:
            Lines = GA.readlines()
            for line in Lines:
                # print(line)
                splited = line.split(';')
                fullName = splited[1]
                fullName = fullName.split(',')
                # print(fullName) # 0:first 1:mid , 2:last
                contactInfo = splited[6]
                contactInfo = contactInfo.split(',')# email , num, fax
                type = splited[7] # THE FLAG! SO U CAN HANDLE THE TYPE OF EMPLOYEE
                print(type)

                # print(splited)


    except FileNotFoundError:
        print('FILE NOT FOUND!')




def main():

    # e1 = emp.Employee(1,1,1,23,3,12321,3,1,23,13,2,3,4)
    # e1.name = 'faris'
    # print(e1.name)
    #
    readGA('GAttributes.txt')




if __name__ =='__main__':

    main()

