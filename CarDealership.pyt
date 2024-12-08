from car import car #Importing the class file

def addCar(inputList): #Adding a new car to the list
    newCar = car(True)
    inputList.append(newCar)

def printAllCars(inputList): #Displaying all cars in the list
    i=1
    if len(inputList) == 0:
        print("There Are No Cars In Your List")
    else:
        for car in inputList:
            print(f"\n{i}: ")
            car.printCarDetails()
            i+=1

def removeCar(inputList): #Removing the selected car from list
    if len(inputList) == 0:
        print("\nThere Are No Cars In Your List")
    else:
        printAllCars(inputList) #Printing all cars in list
        pos = int(input("\nWhich Car Do You Wish To Remove: ")) #Inputing the position of the car
        pos-=1 #Decrementing, so that it matches the index
        inputList.pop(pos) #Removing the indexed element

def editCar(inputList): #Editing the selected  car from list
    if len(inputList) == 0:
        print("\nThere Are No Cars In Your List")
    else:
        printAllCars(inputList) #Printing all cars in list
        pos = int(input("\nWhich Car Do You Wish To Edit: ")) #Inputing the position of the car
        pos-=1 #Decrementing to match the index
        newCar = car(True) #Creating a new car object
        inputList[pos] = newCar #Asigning it to the edited option

def loadFromFile(inputList): #Loading a Car List from a file
    fileName = input("\nEnter file name to load from: ") #Entering the file name
    try: 
        with open(fileName, 'r') as inputFile: #Opening file
            for line in inputFile:
                textList = (line.strip().split(";")) #Spliting the text in each line
                if len(textList) == 5:  #Checking if the line has 5 elements
                    try:
                        newCar = car(False) #Creating a new car object with no input parameters
                        newCar.loadCarInfo(*textList) #Unpacking the list into arguments
                        inputList.append(newCar)
                    except IndexError:
                        print("\nError: The file does not have enough lines.")
    except FileNotFoundError:
        print("\nError: Invalid file.")

def saveToFile(inputList): #Saving current car list to file
    fileName = input("Enter File Name: ")
    with open(fileName, 'w') as saveFile:
        for car in inputList:
            saveFile.write(f"{car.carBrand};{car.carModel};{car.engine};{car.year};{car.mileage}\n")

def menu(): #Main menu
        strs = ('\n1. Add New Car\n'
                '2. Show All Cars\n'
                '3. Load From File\n'
                '4. Edit Cars\n'
                '5. Remove Car\n'
                '6. Exit\n'
                'Enter Choice: ')
        while True:
            choice = input(strs)
            try:
                choice = int(choice)
                if 1 <= choice <= 6: #Checking if given choice is within bounds
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
            except ValueError: #If inut value is not a number
                print("Invalid input. Please enter a number.") #Throw an error

def menu2(): #Choice menu
    strs = ('\n1. Load Cars from File\n'
                '2. Save Cars to File\n'
                '3. Cancel\n'
                'Enter Choice: ')
    while True:
            choice = input(strs)
            try:
                choice = int(choice)
                if 1 <= choice <= 3: #Checking if given choice is within bounds
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
            except ValueError: #If inut value is not a number
                print("Invalid input. Please enter a number.") #Throw an error

carList = [] #A list with all cars

while True: #use while True
    choice = menu()
    if choice == 1:
        addCar(carList)
    elif choice == 2:
        printAllCars(carList)
    elif choice ==3:
        while True:
            choice2 = menu2()
            if choice2 == 1:
                loadFromFile(carList)
                break
            elif choice2 == 2:
                saveToFile(carList)
                break
            elif choice2 == 3:
                break
    elif choice == 4:
        editCar(carList)
    elif choice == 5:
        removeCar(carList)
    elif choice == 6:
        break