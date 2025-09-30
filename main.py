

class Animal:
    def __init__(self,name ,age,species):
        self._name = name
        self._age = age
        self._species = species

    def __repr__(self):
        return f"{self._name}, {self._species}"

    def make_sound(self):
        pass

    def move(self):
        print('Ходит')

    def eat(self):
        pass

    def get_age(self):
        return self._age


    def set_age(self, age):
        self._age = age



class Dog(Animal):
    def make_sound(self):
        print("гав")


class Cat(Animal):
    def make_sound(self):
        print("мяу")


class Cow(Animal):
    def make_sound(self):
        print("мууу")


class Bird(Animal):
    def make_sound(self):
        print("кар")
    def move(self):
        print ('летает')



#опись соопарка и людей
class Staff :
    def __init__(self,name,age):
       self.age = age
       self.name = name

    def sleep (self):
        print ('сотрудник спит')

class Veterinarian(Staff):
    def __init__(self,name,age,level):
        super().__init__(name,age)
        self.level = level # ученая степень

class Zoo :
    def __init__(self,name,adres):

        self.list_staff =[]
        self.name = name
        self.adres = adres

        self.list_animals = []

    def zoo_info(self):
        print(f'персонал - {self.list_staff.name}')
        print(f'животные - {self.list_animals}')

    def add_staff(self,name,age):
        staff = Zoo(name,age)
        self.list_staff.append(staff)

    def add_animal(self,name,age,species):
        animal = Animal(name,age,species)
        self.list_animals.append(animal)

def animal_sound(animals):
    animals.make_sound()

zoo = Zoo('Московский зоопарк','Центральная 1')
zoo.add_staff('Ургант',30)
zoo.add_staff('Петя ',12)
zoo.add_animal('Питон',3.14)
zoo.zoo_info()

with open("hello.txt", "w") as myfile:
    print("Работа с файлом myfile")