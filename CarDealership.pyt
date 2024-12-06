from car import car #Importing the class file

def addCar(inputList): #Adding a new car to the list
    newCar = car()
    inputList.append(newCar)

def printAllCars(inputList): #Displaying all cars in the list
    i=1
    for car in inputList:
        print(f"\n{i}: ")
        car.printCarDetails()
        i+=1

def removeCar(inputList): #Removing the selected car from list
    print()
    #Print all cars and ask which one to remove, then remove as usual

def menu():
        strs = ('\n1. Add New Car\n'
                '2. Show All Cars\n'
                '3. Edit Cars\n'
                '4. Remove Car\n'
                '5. Exit\n'
                'Enter Choice: ')
        while True:
            choice = input(strs)
            try:
                choice = int(choice)
                if 1 <= choice <= 5: #Checking if given choice is within bounds
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
    #elif choice == 3:
        
    elif choice == 4:
        removeCar(carList)
    elif choice == 5:
        break