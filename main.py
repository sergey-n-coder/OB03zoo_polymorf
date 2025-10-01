
import json

class Animal:
    def __init__(self,name ,age,species):
        self.name = name
        self.age = age
        self.species = species

    def __repr__(self):
        return f"{self.name}, {self.species}"

    def make_sound(self):
        pass

    def move(self):
        print('Ходит')

    def eat(self):
        pass


class Dog(Animal):
    def __init__(self, name, age, subt):
        super().__init__(name,age,"Собака")
        self.subType = subt

    def make_sound(self):
        print("гав")


class Cat(Animal):
    def __init__(self, name, age, subt):
        super().__init__(name,age,"Кошка")
        self.subType = subt
    def make_sound(self):
        print("мяу")


class Cow(Animal):
    def make_sound(self):
        print("мууу")


class Bird(Animal):
    def __init__(self, name, age, species):
        super().__init__(name,age,"Птица")

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
    def __init__(self):
        self.list_staff = []

        # Загружаем существующее состояние зоопарка
        try:
            with open("zoo.json", 'r') as file:
                data = json.load(file)
                self.animals = [Animal(animal['name'], animal['age'], animal['species']) for animal in data]
        except FileNotFoundError:
            print("Файл зоопарка не найден.")
            self.animals = []

    def add_animal_new(self, name, age,species):
        new_animal = Animal(name, age,species)
        self.animals.append(new_animal)
        print(f'Животное "{new_animal}" успешно добавлено.')

    def add_animal(self,new_animal):
        self.animals.append(new_animal)
        print(f'Животное "{new_animal.name}" успешно добавлено.')


    def list_animals(self):
        if not self.animals:
            print('Зоопарк пуст!')
        else:
            print('Список животных:')
            for i, animal in enumerate(self.animals, start=1):
                print(f'{i}. {animal}')

    def save_state(self):
        animals_data = [
            {'name': animal.name, 'age': animal.age,'species': animal.species}
            for animal in self.animals
        ]
        with open("zoo.json", 'w') as file:
            json.dump(animals_data, file, indent=4)
        print('Состояние зоопарка сохранено.')

    def zoo_animal_sound(self):
        print ('звуки зоопарка')
        for a in self.animals :
            a.make_sound()
    def add_staff(self,staff_new):
        self.list_staff.append(staff_new)


zoo = Zoo()
direct = Staff('Igor',32)
zoo.add_staff(direct)
#dog = Dog('полкан',4,'<tityyfz')
#cat =Cat('серая кошка',4,'Неизвестная')
#zoo.add_animal(dog)
#zoo.add_animal(cat)

#zoo.zoo_animal_sound()
if __name__ == "__main__":
   # zoo = Zoo()

    while True:
        action = input(
            "\nВыберите действие:\n"
            "1. Посмотреть список животных\n"
            "2. Добавить Собаку\n"
            "3. Добавить Кошку\n"
            "5. Слушать звуки\n"
            "4. Сохранить и выйти\n"
            "> "
        )

        if action == '1':
            zoo.list_animals()

        elif action == '2':
            name = input("Имя животного: ")
            age = input("Возраст животного: ")
            dog = Dog(name, age,'СЛуживая')
          #  species = input("Вид животного: ")
            zoo.add_animal(dog ) #species)
        elif action == '3':
            name = input("Имя Кошки: ")
            age = input("Возраст животного: ")
            cat = Cat(name, age, 'Плешивая')
            #  species = input("Вид животного: ")
            zoo.add_animal(cat)  # species)

        elif action == '5':
            zoo.zoo_animal_sound()
        else :
            zoo.save_state()
            break

