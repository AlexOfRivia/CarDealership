class car:

    def __init__(self): #Initializing new car object
        self.carBrand = input("Enter car brand: ")
        self.carModel = input("Enter car model: ")
        self.engine = input("Enter engine: ")
        self.year = input("Enter production year: ")
        self.mileage = input("Enter mileage: ")

    def loadCarInfo(self, brand, model, engine, year, mileage):
        self.carBrand = brand
        self.carModel = model
        self.engine = engine
        self.year = year
        self.mileage = mileage

    def printCarDetails(self): #Printing car details
        print(f"\nCar brand: {self.carBrand}")
        print(f"Car Model: {self.carModel}")
        print(f"Engine: {self.engine}")
        print(f"Production Year: {self.year}")
        print(f"Mileage: {self.mileage} Km")