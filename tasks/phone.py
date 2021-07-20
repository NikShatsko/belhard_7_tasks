"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""


class Phone:
    brand: str
    model: str
    issue_year: int
    name: str

    def __init__(self, brand: str, model: str, issue_year: int, name: str):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.name = name

    def receive_call(self):
        print(f"Звонит {self.name}")

    def __str__(self):
        return f"Бренд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}"


phone_list = Phone('Samsung', 'S20', 2020, "Абонент")
print(phone_list)
phone_list.receive_call()