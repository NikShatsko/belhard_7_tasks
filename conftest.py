# class MyList:
#     inner_list: list
#
#     def __init__(self, a):
#         self.inner_list = a
#
#     def __getitem__(self, item):
#         return self.inner_list[item]
#
#     def __getattr__(self, name):
#         if name not in self.__dict__:
#             self.__dict__[name] = 321
#             return self.__dict__[name]
#
#
# some = MyList([1, 5, 8])
# print(some[2])
#
# print(some.inner_list)

# class SomeClass:
#     a: int
#
#     def __init__(self, a: int):
#         self.a = a
#
#     def __and__(self, other):
#         if self.a >= 0 and other.a >= 0:
#             return True
#         else:
#             return False
#
#     def __repr__(self):
#         return f"Some a = {self.a}"
#
#
# result = SomeClass(10) & SomeClass(-1)
# print(result)

class NewClass:
    a: list

    def __init__(self, a):
        self.a = a

    def __len__(self):
        return len(self.a)

    def __getitem__(self, item):
        return self.a[item]

    def __setitem__(self, key, value):
        return self.a.insert(key, value)

    def __repr__(self):
        return f"a = {self.a}"


some_list = NewClass([1, 23, 5, 6])
some_list[2] = 4
print(some_list)


"""
Объект как функция
"""
def __call__(self, *args, **kwargs):
    print('wow Phone')

"""
Магические методы сравнения
"""
def __gt__(self, other):
    return self.average_score > other.average_score
print(sorted(student_list))

"""
Магические методы арифметических операций
"""
def __add__(self, other):
    h = self.h + other.h
    m = self.m + other.m
    s = self.s + other.s
    return Time(h, m, s)
a = Time(2, 16, 48)
b = Time(3, 51, 22)
print(a + b)

"""
Магические методы логических операторов
"""
    def __and__(self, other):
        if self.a >= 0 and other.a >= 0:
            return True
        else:
            return False
result = SomeClass(10) & SomeClass(-1)

"""
Контейнеры
"""
def __getitem__(self, item):
    return self.a[item]

def __setitem__(self, key, value):
    return self.a.insert(key, value)

def __len__(self):
    return len(self.a)

"""
Доступ к атрибутам
"""
    def __getattr__(self, name):
        if name not in self.__dict__:
            self.__dict__[name] = 321
            return self.__dict__[name]

class Config():
    def __init__(self, filename):
        self.file = open(filename, "w")
        self.filename = filename

    def __setattr__(self, attr, val):
        if not (attr in ('filename', 'file')):
            print (attr, val)
        self.__dict__[attr] = val


# class MyList:
#     inner_list: list
#
#     def __init__(self, a):
#         self.inner_list = a
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#
#         if self.name in instance.__dict__:
#             print("Атрибут объекта")
#             return instance.__dict__.get(self.name, None)
#         else:
#             print("Атрибут класса")
#             return owner.__dict__.get(self.name, None)
#
#     def __set_name__(self, owner, name):
#         print("Call get")
#         self.name = name
#
#     def __set__(self, instance, value):
#         print("Call set")
#         instance.__dict__[self.name] = value
#
# class A:
#     some = MyList([1, 2, 3])
#
# aaa = A()
# print(aaa.some)
# aaa.some = MyList([3, 2, 1])
# print(aaa.some)



# class Phone:
#     price: int
#     model: str
#     color: str = "Black"
#
#     def __init__(self, price, model, color):
#         self.price = price
#         self.model = model
#         self.color = color
#
#     def make_sound(self):
#         print(f"incoming call to {self.model}")
#
#     def __call__(self, *args, **kwargs):
#         print('wow Phone')
#
#     @classmethod
#     def make_sound_class(cls):
#         print(f"I want to call")
#
#     @staticmethod
#     def name_of_phone():
#         print('iphone')
#
#
# phone = Phone(3000, 'Samsung', "white")
# phone.name_of_phone()