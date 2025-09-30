import json


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name}, {self.species}"


class Zoo:
    def __init__(self):
        # Загружаем существующее состояние зоопарка
        try:
            with open("zoo.json", 'r') as file:
                data = json.load(file)
                self.animals = [Animal(animal['name'], animal['species']) for animal in data]
        except FileNotFoundError:
            print("Файл зоопарка не найден.")
            self.animals = []

    def add_animal(self, name, species):
        new_animal = Animal(name, species)
        self.animals.append(new_animal)
        print(f'Животное "{new_animal}" успешно добавлено.')

    def list_animals(self):
        if not self.animals:
            print('Зоопарк пуст!')
        else:
            print('Список животных:')
            for i, animal in enumerate(self.animals, start=1):
                print(f'{i}. {animal}')

    def save_state(self):
        animals_data = [
            {'name': animal.name, 'species': animal.species}
            for animal in self.animals
        ]
        with open("zoo.json", 'w') as file:
            json.dump(animals_data, file, indent=4)
        print('Состояние зоопарка сохранено.')


# Основной цикл программы
if __name__ == "__main__":
    zoo = Zoo()

    while True:
        action = input(
            "\nВыберите действие:\n"
            "1. Посмотреть список животных\n"
            "2. Добавить животное\n"
            "3. Сохранить и выйти\n"
            "> "
        )

        if action == '1':
            zoo.list_animals()

        elif action == '2':
            name = input("Имя животного: ")
            species = input("Вид животного: ")
            zoo.add_animal(name, species)

        elif action == '3':
            zoo.save_state()
            break