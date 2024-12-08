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
        print("There Are No Cars In Your List")
    else:
        printAllCars(inputList) #Printing all cars in list
        pos = int(input("Which Car Do You Wish To Remove: ")) #Inputing the position of the car
        pos-=1 #Decrementing, so that it matches the index
        inputList.pop(pos) #Removing the indexed element

def editCar(inputList): #Editing the selected  car from list
    if len(inputList) == 0:
        print("There Are No Cars In Your List")
    else:
        printAllCars(inputList) #Printing all cars in list
        pos = int(input("Which Car Do You Wish To Edit: ")) #Inputing the position of the car
        pos-=1 #Decrementing to match the index
        newCar = car(True)
        inputList[pos] = newCar

def loadFromFile(inputList):
    fileName = input("Enter file name to load from: ")
    with open(fileName, 'r') as inputFile:
        for line in inputFile:
            textList = (line.strip().split(";"))
            if len(textList) == 5:  # Check if the line has 5 elements
                try:
                    newCar = car(False)
                    newCar.loadCarInfo(*textList)  # Unpack the list into arguments
                    inputList.append(newCar)
                except IndexError:
                    print("Error: The file does not have enough lines.")
            

def menu():
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

carList = [] #A list with all cars

while True: #use while True
    choice = menu()
    if choice == 1:
        addCar(carList)
    elif choice == 2:
        printAllCars(carList)
    elif choice ==3:
        loadFromFile(carList)
    elif choice == 4:
        editCar(carList)
    elif choice == 5:
        removeCar(carList)
    elif choice == 6:
        break