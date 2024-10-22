print("Task 1".center(40, "="))


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello! My name is {self.name}, I am {self.age} years old.")


class Builder(Human):
    def __init__(self, name, age, experience):
        super().__init__(name, age)
        self.experience = experience

    def introduce(self):
        super().introduce()
        print(f"I'm a builder with {self.experience} years of experience.")


class Sailor(Human):
    def __init__(self, name, age, rank):
        super().__init__(name, age)
        self.rank = rank

    def introduce(self):
        super().introduce()
        print(f"I'm a sailor with {self.rank} rank.")


class Pilot(Human):
    def __init__(self, name, age, flight_hours):
        super().__init__(name, age)
        self.flight_hours = flight_hours

    def introduce(self):
        super().introduce()
        print(f"I'm a pilot with {self.flight_hours} flight hours.")


person = Human("Kate", 21)
person.introduce()

builder = Builder("John", 35, 10)
builder.introduce()

sailor = Sailor("Alice", 29, "Captain")
sailor.introduce()

pilot = Pilot("Bob", 40, 5000)
pilot.introduce()

print("Task 2".center(40, "="))


# Base class Passport
class Passport:
    def __init__(self, full_name: str, birth_date: str, passport_number: str, nationality: str):
        self.full_name = full_name
        self.birth_date = birth_date
        self.passport_number = passport_number
        self.nationality = nationality

    def display_info(self):

        print(f"Passport Holder: {self.full_name}")
        print(f"Date of Birth: {self.birth_date}")
        print(f"Passport Number: {self.passport_number}")
        print(f"Nationality: {self.nationality}")


class ForeignPassport(Passport):
    def __init__(self, full_name, birth_date, passport_number, nationality, foreign_passport_number, visas):
        super().__init__(full_name, birth_date, passport_number, nationality)
        self.foreign_passport_number = foreign_passport_number
        self.visas = visas

    def display_info(self):
        print(self.visas)
        str_visas = ', '.join(self.visas) if len(self.visas) else "Empty"
        super().display_info()
        print(f"Foreign passport number: {self.foreign_passport_number}.")
        print(f"Visas: {str_visas}.")

    def add_visa(self, *args):
        self.visas.extend(list(args))


passport = Passport("John Doe", "1985-07-20", "123456789", "USA")
passport.display_info()
print()

foreign_passport = ForeignPassport("John Doe", "1985-07-20", "123456789",
                                   "USA", "987654321", [])
foreign_passport.display_info()
print()
foreign_passport.add_visa("France", "Tourist", "2025-12-31")
foreign_passport.add_visa("Germany", "Work", "2024-06-15")
foreign_passport.display_info()
print()

print("Task 3".center(60, "="))


class Animal:
    def __init__(self, name="N\\A", age=0, kind_animal="N\\A", kind_food="N\\A"):
        self.name = name
        self.age = age
        self.kind_animal = kind_animal
        self.kind_food = kind_food

    def eat(self):
        print(f"This is {self.kind_animal}. His name is {self.name}. It is {self.age} years old."
              f" It eats {self.kind_food}.")


class Tiger(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Tiger", "meat")

    def run(self):
        print(f"The tiger {self.name} running.")

    def roar(self):
        print(f"The tiger {self.name} say 'rrrrrrrrrrrrrrrrrrrrrrrrrr'.")


class Crocodile(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Crocodile", "meat")

    def swim(self):
        print(f"The crocodile {self.name} is swimming.")


class Kangaroo(Animal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, "Crocodile", "meat")

    def jump(self):
        print(f"The crocodile {self.name} is jumping.")


tiger = Tiger("Sheru", 5)
tiger.eat()
tiger.roar()
tiger.run()

crocodile = Crocodile("Kroko", 12)
crocodile.eat()
crocodile.swim()

kangaroo = Kangaroo("Jack", 3)
kangaroo.eat()
kangaroo.jump()