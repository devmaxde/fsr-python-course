
# Python Objects

## Introduction to Objects

Objects in Python represent an encapsulation of variables (properties) and functions (methods) into a single entity. Objects are created from classes, which can be thought of as blueprints for the object.

### Basic Concepts

- **Object**: An instance of a class containing properties and methods.
- **Class**: A blueprint for creating objects, providing initial values for properties, and implementations of methods.

**Example**
```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"This is a {self.year} {self.brand} {self.model}")

my_car = Car("Ford", "Mustang", 1964)
my_car.display_info()
```

### Properties

Properties are variables that belong to an object.

**Example**
```python
print(my_car.brand)  # Accessing the 'brand' property of the 'my_car' object
```

### Methods

Methods are functions that belong to an object.

**Example**
```python
my_car.display_info()  # Calling the 'display_info' method of the 'my_car' object
```

## Class Definition

### Basic Structure

A class is defined using the `class` keyword, followed by the class name and a colon.

**Syntax**
```python
class ClassName:
    # properties and methods
```

### The `__init__` Method

The `__init__` method is a special method called a constructor, used for initializing properties of an object.

**Syntax**
```python
class ClassName:
    def __init__(self, parameter1, parameter2):
        self.property1 = parameter1
        self.property2 = parameter2
```

## Object-Oriented Concepts

### Inheritance

Inheritance allows a new class to extend an existing class, inheriting its properties and methods.

**Example**
```python
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_size):
        super().__init__(brand, model, year)
        self.battery_size = battery_size
```

### Encapsulation

Encapsulation involves restricting access to properties and methods, often using private and protected access modifiers.

### Polymorphism

Polymorphism allows methods to do different things based on the object it is acting upon.

## Class and Instance Variables

- **Class variables** are shared by all instances of a class.
- **Instance variables** are unique to each instance.

**Example**
```python
class Dog:
    species = "Canis familiaris"  # Class variable

    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable
```

## Recap

| Concept             | Description                                           | Example                                             |
|---------------------|-------------------------------------------------------|-----------------------------------------------------|
| Class               | Blueprint for creating objects                        | `class Dog: pass`                                   |
| Object              | An instance of a class                                | `my_dog = Dog()`                                    |
| Properties          | Variables belonging to an object                      | `my_dog.name = 'Rex'`                               |
| Methods             | Functions belonging to an object                      | `def bark(self): print("Woof!")`                    |
| Inheritance         | Extending the functionality of a class                | `class Bulldog(Dog): pass`                          |
| Encapsulation       | Restricting access to properties and methods          | Using `_` or `__` to denote private/protected attributes |
| Polymorphism        | Methods can act differently based on the object type  | Overriding methods in child classes                 |
| Class Variable      | Variable shared by all instances of a class           | `Dog.species = 'Canis familiaris'`                  |
| Instance Variable   | Unique to each instance                               | `self.name = name` in the `__init__` method         |

## Best Practices

- Use proper naming conventions (CamelCase for classes, lowercase_with_underscores for functions and variables).
- Keep class definitions simple and focused on a single responsibility.
- Document classes and methods clearly for maintainability.
