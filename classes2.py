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
        return f"{self.__name} is driving!"

    def drift(self):
        return f"{self.__name} is drifting!!"

    def carry_cargo(self):
        return f"{self.__name} is carrying cargo!!"


class Bus(Vehicle):
    
    def __init__(self, brand : str, name : str, color : str, capacity : int, plate_number : str, wight : int):
        super().__init__(brand, name, color, capacity, plate_number)
        self.wight = wight
    
    def drive(self):
        return f"{self.get_name} is driving!"

    def drift(self):
        return f"{self.get_name} is drifting!!"

    def carry_cargo(self):
        return f"{self.get_name} is carrying cargo!!"

class Truck(Vehicle):
    
    def __init__(self, brand : str, name : str, color : str, capacity : int, plate_number : str, hight : float):
        super().__init__(brand, name, color, capacity, plate_number)
        self.hight = hight

    def drive(self):
        return f"{self.get_name} is driving!"

    def drift(self):
        return f"{self.get_name} is drifting!!"

    def carry_cargo(self):
        return f"{self.get_name} is carrying cargo!!"


car = Vehicle("toyota","supra","white",2,"gta2030")

bus = Bus("Mercedes-Benz","Daimler","silver",23,"sub0302",19.14)
bus.set_brand("Mercedes-Benz")
bus.set_name("Daimler")
bus.set_color("silver")
bus.set_capacity(23)
bus.set_plate_number("sub0302")

truck = Truck("Peterbilt","579EV","white",2,"tuk8050",80000)
truck.set_brand("Peterbilt")
truck.set_name("579EV")
truck.set_color("white")
truck.set_capacity(2)
truck.set_plate_number("tuk8050")

print(car.get_brand())
print(bus.wight)