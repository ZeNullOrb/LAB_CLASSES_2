class Vehicle:

    def __init__(self, brand : str, name : str, color : str, capacity : int, plate_number : str):
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

    #brand
    def set_brand(self, brand):
        self.__brand = brand
    
    def get_brand(self):
        return self.__brand
    #name
    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    #color
    def set_color(self, color):
        self.__color = color
    
    def get_color(self):
        return self.__color
    #capacity
    def set_capacity(self, capacity:int):
        self.__capacity = capacity
    
    def get_capacity(self):
        return self.__capacity
    #plate_number
    def set_plate_number(self, plate_number):
        self.__plate_number = plate_number
    
    def get_plate_number(self):
        return self.__plate_number
    
    #--------------------------------------

    def drive(self):
        return print(f"{self.__name} is driving!!")

    def drift(self):
        return print(f"{self.__name} is drifting!!")

    def carry_cargo(self):
        return print(f"{self.__name} is carrying cargo!!")

class Bus(Vehicle):
    
    def __init__(self, brand : str, name : str, color : str, capacity : int, plate_number : str, wight : int):
        super().__init__(brand, name, color, capacity, plate_number)
        self.wight = wight

    def drift(self):
        return print(f"{self.get_name()} is stoping!!")

    def carry_cargo(self):
        return print(f"{self.get_name()} is Full!!")

class Truck(Vehicle):
    
    def __init__(self, brand : str, name : str, color : str, capacity : int, plate_number : str, hight : float):
        super().__init__(brand, name, color, capacity, plate_number)
        self.hight = hight

    def drift(self):
        return print(f"{self.get_name()} is loading!!")

car = Vehicle("toyota","supra","white",2,"gta2030")

bus = Bus("Mercedes-Benz","Daimler","silver",23,"sub0302",19.14)

truck = Truck("Peterbilt","579EV","white",2,"tuk8050",80000)

print(f"{car.get_brand()} \n{car.get_name()} \n{car.get_color()} \n{car.get_capacity()} \n{car.get_plate_number()}")

print("---"*10)

print(f"{bus.get_brand()} \n{bus.get_name()} \n{bus.get_color()} \n{bus.get_capacity()} \n{bus.get_plate_number()}")

print("---"*10)

print(f"{truck.get_brand()} \n{truck.get_name()} \n{truck.get_color()} \n{truck.get_capacity()} \n{truck.get_plate_number()}")

print("---"*10)

car.drive()
car.drift()

print("---"*10)

bus.drive()
bus.drift()
bus.carry_cargo()
bus.drive()

print("---"*10)

truck.drive()
truck.drift()
truck.carry_cargo()
truck.drive()