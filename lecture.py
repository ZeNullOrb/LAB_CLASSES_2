#classes

#to define a class
class Person:
    #class Attribute / Property
    kind = "Human"

    def __init__(self, name : str, age : int, gender : str):
        #initialize object / instance attributes
        self.__name = name #attribute is private / encapsulation
        self.__age = age
        self.__gender = gender
    

    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    

    def set_age(self, age):
        if not type(age) == int:
            raise ValueError("Please provide a valid age")
        elif age <=0 or age > 200:
            raise ValueError("Please provide an age between 1 and 200")

        self.__age = age
    
    def get_age(self):
        return self.age
    
    def introduce_self(self):
        return f"Hi, I am {self.__name} and I am {self.__age} years old"


#inheritance
class Employee(Person):
    
    def __init__(self, name : str, age : int, gender : str, job : str, employee_number : int):
        super().__init__(name, age, gender)
        self.job = job
        self.employee_number = employee_number
    
    def list_tasks(self):
        return f"You need to check the emails"
    
    #overriding the function / polymorphism
    def introduce_self(self):
        return f"I am an employee {self.get_name()}, my job is {self.job} and my employee number is {self.employee_number}"

    def submit_suggestion(self, content) -> bool:
        if self.__check_open_suggestion():
            return "You have an open suggestion"
        
        self.__email_suggestion_to_manager(content)
        return "Suggestion was sent"


    #Abstract the method
    def __check_open_suggestion(self):
        return False
    
    def __email_suggestion_to_manager(self, content):
        return "Emailed the manager"



#to create a new object/instance from the class Person
person1 = Person("Mohammed", 20, "Male")
person2 = Person("Nora", 18, "Female")

person1.set_age(34)

#to read an isntance attribute
print("first person name is: " , person1.get_name())

#to change an instance attribute value
person1.set_name("Ahmed")
print(person1.get_name())

#to read a class attribute
print("The kind of person: ", Person.kind)

#to change a class attribute value
Person.kind = "Bird"

print(person1.kind)


#calling a method
print(person1.introduce_self())



employee1 = Employee("Mohammed", 30, "Male", "Assitant", 3426)
print(employee1.job)
print(employee1.list_tasks())
print(employee1.introduce_self())


print(employee1.submit_suggestion("Please raise the salary"))
