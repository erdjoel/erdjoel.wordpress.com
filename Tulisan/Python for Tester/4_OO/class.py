# -*- coding: utf-8 -*-


class MyClass(object):
    instance_count = 0  # class attribute, this could be called using MyClass.instance_count

    # def __new__(cls):
    # constructors are rarely used in Python unless inheriting from a built-in class

    def __init__(self, value):
        # initializer
        self.__value = value  # self.__value will be private internal property for this class instance
        MyClass.instance_count += 1
        print("instance No {} created".format(MyClass.instance_count))

    def a_method(self, a_value):
        self.__value *= a_value

    def __str__(self):
        # special method used to return a formatted string so that instances passed to the print function
        return "A MyClass instance with value: " + str(self.__value)

    def __del__(self):
        # The destructor __del__() decrements the class variable instance_count when the object is destroyed.
        MyClass.instance_count -= 1

    # method overloading by providing default value
    # how_many parameter become optional
    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound)
        else:
            print(self.get_sound() * how_many)


my_instance = MyClass()

my_instance.a_method(66)
MyClass.a_method(my_instance, 66)  # more explicit invocation
print(my_instance)  # __str__() method in action

print(MyClass.instance_count)  # 1
myInstance1 = MyClass(44)
print(MyClass.instance_count)  # 2
del (myInstance1)
print(MyClass.instance_count)  # 1


class MyCircle:
    def __init__(self, radius):
        self.__radius = radius

    def __set_radius(self, new_value):  # private function with name mangling
        if new_value >= 0:
            self.__radius = new_value
        else:
            raise ValueError("Value must be positive")

    radius = property(None, __set_radius)  # a property with no getter, and __set_radius as setter function

    # getting radius will throw AttributeError: unreadable attribute
    # property(getter=None, setter=None, deleter=None, doc_string=None)

    @property
    def area(self):  # function disguised as property. behave as read-only attribute.
        return 3.14159 * (self.__radius ** 2)


c2 = MyCircle(42)
c2.area  # 5541.76476
print(c2.radius)  # AttributeError: unreadable attribute
c2.radius = 12
c2.area  # 452.38896
c2.radius = -4  # ValueError: Value must be positive


# INHERITANCE
# inherit all of the variables and methods from another class


class SubClass(MyClass):  # sub class of MyClass
    def __init__(self, a_value):
        super().__init__(a_value)  # call to parent's __init__() method


class Oval(MyCircle):
    def __init__(self, radius1, radius2):
        super().__init__(radius1)
        self.__radius2 = radius2

    def __set_radius2(self, new_value):  # new function specific to child class
        if new_value >= 0:
            self.__radius2 = new_value
        else:
            raise ValueError("Value must be positive")

    radius2 = property(None, __set_radius2)

    # We can overwrite functions in the super class
    @property
    def area(self):  # function disguised as property. behave as read-only attribute.
        return 3.14159 * (self.__radius ** self.__radius2)

# polymorphism??
