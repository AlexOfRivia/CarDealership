from car import car #Importing the class file

def addCar(inputList):
    newCar = car()
    inputList.append(newCar)

def printAllCars(inputList):
    for car in inputList:
        car.printCarDetails()

carList = []

addCar(carList)
printAllCars(carList)