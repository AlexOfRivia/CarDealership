class car:

    def __init__(self, notLoadedFromFile): #Initializing new car object
        if notLoadedFromFile == True:
            self.carBrand = input("\nEnter car brand: ")
            self.carModel = input("Enter car model: ")
            self.engine = input("Enter engine: ")
            self.year = input("Enter production year: ")
            self.mileage = input("Enter mileage: ")
        else:
            return

    def loadCarInfo(self, brand, model, engine, year, mileage):
        self.carBrand = brand
        self.carModel = model
        self.engine = engine
        self.year = year
        self.mileage = mileage

    def printCarDetails(self): #Printing car details
        print(f"Car brand: {self.carBrand}")
        print(f"Car Model: {self.carModel}")
        print(f"Engine: {self.engine}")
        print(f"Production Year: {self.year}")
        print(f"Mileage: {self.mileage} Km\n")