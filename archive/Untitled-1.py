from datetime import datetime
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if Singleton._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    

from datetime import datetime
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    @classmethod
    def create_from_birth_year(cls, name, birth_year):
        current_year = datetime.now().year
        age = current_year - birth_year
        return cls(name, age)
    
    
    @staticmethod
    def sum_numbers(a, b):
        return a*b

person = Person('Tagir', 15)
print(person.create_from_birth_year(name='tagir', birth_year=2010))



class Point:
    Max_coord = 100
    Min_coord = 0

    
    def __init__(self, y, x):
        self.x = x
        self.y = y

    
    def set_coord(self, x, y):
        if self.Max_coord <= x <= self.Max_coord:
            self.x = x
            self.y = y
    
    
    @classmethod
    def set_bound(cls, left):
        cls.Min_coord = left 
    
    
    def __getattribute__(self, name):
        if name == 'x':#если обращаемся к иксу то вызываем ошибку
            raise ValueError('нельзя обращаться')
        else:
            return object.__getattribute__(self, name)#вызывается если мы обращаемся к кокому-то атрибуту класса
        
    
    def __setattr__(self, name, value):
        if name == "z":
            raise ValueError
        else:
            return object.__setattr__(self, name, value)#вызывается всегда когда мы присваеваем какое-то значение атрибуту класса
        
    
    
    def __getattr__(self, name):# обращаемя к несущ атрибуту
        return False

    
    def __delattr__(self, name):
        return object.__delattr__(self, name)#вызывается если мы удаляем какой-то атрибут
    
    #паттерн моносостояние - все атибуты класса будут иметь одинаковые значения
class ThereadData:
    __shread_attrs = {
        'name':'thread1',
        'data':{},
        'id':1
    }


    def __init__(self):
        self.__dict__ = self.__shread_attrs
          
#Метод properti
class Piople:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def old(self):
        return self.__old
    
    @old.setter       
    def old(self, old):
        self.__old = old

p = Piople('Tagir', 15)
print(p.old)



class Intenger:
    def __set_name__(self, owner, name):
        self.name = "_"+name


    def __get__(self, instance, owner):
        return instance.__dict__(self.name)
    

    def __set__(self, instance, value):
        print(f'__set__: {self.name} = {self.value}')
        instance.__dict__[self.name] = value



class Point3D:
    x = Intenger()
    y = Intenger()
    x = Intenger()
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


