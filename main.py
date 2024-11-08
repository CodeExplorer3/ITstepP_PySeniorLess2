class Person:
    имя: str
    фамилия: str
    возраст: int
    пенсия: bool

    def __init__(self, имя: str, фамилия: str, возраст: int):
        self.имя = имя
        self.фамилия = фамилия
        self.возраст = возраст
        self.установить_пенсию(self.возраст)

    def установить_пенсию(self, значение: int):
        self.пенсия = значение >= 60

    def информация_о_персоне(self):
        print(f'Персона:\t{self.имя} | {self.фамилия} | {self.возраст}')

# Создаем класс Group (Группа)
class Группа:
    название: str
    количество_студентов: int
    возрастная_категория: str

    def __init__(self, название: str, количество_студентов: int, возрастная_категория: str):
        self.название = название
        self.количество_студентов = количество_студентов
        self.возрастная_категория = возрастная_категория

    def информация_о_группе(self):
        print(f'Группа:\t{self.название} | Студенты: {self.количество_студентов} | Возрастная категория: {self.возрастная_категория}')

# Создаем класс Student (Студент)
class Студент(Person):
    успеваемость: str
    группа: Группа

    def __init__(self, имя: str, фамилия: str, возраст: int, успеваемость: str, группа: Группа):
        super().__init__(имя, фамилия, возраст)
        self.успеваемость = успеваемость
        self.группа = группа

    def информация_о_студенте(self):
        self.информация_о_персоне()
        print(f'Студент:\tУспеваемость: {self.успеваемость}')
        self.группа.информация_о_группе()

# Создаем класс Worker (Работник)
class Работник(Person):
    должность: str
    обязанности: str

    def __init__(self, имя: str, фамилия: str, возраст: int, должность: str, обязанности: str):
        super().__init__(имя, фамилия, возраст)
        self.должность = должность
        self.обязанности = обязанности

    def информация_о_работнике(self):
        self.информация_о_персоне()
        print(f'Работник:\tДолжность: {self.должность} | Обязанности: {self.обязанности}')

# Пример использования
группа1 = Группа(название="ИВТ-101", количество_студентов=25, возрастная_категория="18-22")
студент = Студент(имя="Иван", фамилия="Иванов", возраст=20, успеваемость="Отлично", группа=группа1)
работник = Работник(имя="Анна", фамилия="Петрова", возраст=45, должность="Инженер", обязанности="Разработка ПО")

студент.информация_о_студенте()
работник.информация_о_работнике()
