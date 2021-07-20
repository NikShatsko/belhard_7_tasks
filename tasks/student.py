"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5
"""


class Student:
    surname: str
    name: str
    group: str
    average_score: float

    def __init__(self, surname: str, name: str, group: str, average_score: float):
        self.surname = surname
        self.name = name
        self.group = group
        self.average_score = average_score

    def __eq__(self, other):
        return self.average_score == other.average_score

    def __gt__(self, other):
        return self.average_score > other.average_score

    def score(self):
        if self.average_score > 5:
            return self.average_score

    def __repr__(self):
        return f"Student name = {self.name}, score = {self.average_score}"


student_list = [
    Student('a', 'a', 'a', 7.2),
    Student('b', 'b', 'b', 8.3),
    Student('c', 'c', 'c', 6),
    Student('d', 'd', 'd', 7.2),
    Student('e', 'e', 'e', 4.2)
]

print(sorted(student_list))
print(sorted(student_list, reverse=True))

