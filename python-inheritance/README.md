# Python Inheritance 🐍📚

This project covers the concepts of inheritance in Python. Below is a description of the various files and classes defined in this directory.

## Files and Classes 📂

### 0-lookup.py 🔍
- **Function**: `lookup`
- **Description**: Returns the list of available attributes and methods of an object.
- **Prototype**: `def lookup(obj):`

### 1-my_list.py 📜
- **Class**: `MyList`
- **Description**: A subclass of list that provides a method to print the list in sorted order.
- **Method**: `def print_sorted(self):`

### 2-is_same_class.py 🧩
- **Function**: `is_same_class`
- **Description**: Returns True if the object is exactly an instance of the specified class; otherwise False.
- **Prototype**: `def is_same_class(obj, a_class):`

### 3-is_kind_of_class.py 🔍
- **Function**: `is_kind_of_class`
- **Description**: Returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise False.
- **Prototype**: `def is_kind_of_class(obj, a_class):`

### 4-inherits_from.py 🧬
- **Function**: `inherits_from`
- **Description**: Returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.
- **Prototype**: `def inherits_from(obj, a_class):`

### 5-base_geometry.py 📐
- **Class**: `BaseGeometry`
- **Description**: An empty class for geometry objects.

### 6-base_geometry.py 📏
- **Class**: `BaseGeometry`
- **Description**: A class for geometry objects with a method `area` that raises an Exception.
- **Method**: `def area(self):`

### 7-base_geometry.py 📏
- **Class**: `BaseGeometry`
- **Description**: A class for geometry objects with methods `area` and `integer_validator`.
- **Methods**: 
  - `def area(self):`
  - `def integer_validator(self, name, value):`

### 8-rectangle.py 🟧
- **Class**: `Rectangle`
- **Description**: A class that inherits from `BaseGeometry` and defines a rectangle.
- **Methods**: 
  - `def __init__(self, width, height):`

### 9-rectangle.py 🟧
- **Class**: `Rectangle`
- **Description**: A class that inherits from `BaseGeometry` and defines a rectangle with an `area` method and a `__str__` method.
- **Methods**: 
  - `def __init__(self, width, height):`
  - `def area(self):`
  - `def __str__(self):`

### 10-square.py 🟦
- **Class**: `Square`
- **Description**: A class that inherits from `Rectangle` and defines a square.
- **Methods**: 
  - `def __init__(self, size):`
  - `def area(self):`

### 11-square.py 🟦
- **Class**: `Square`
- **Description**: A class that inherits from `Rectangle` and defines a square with a `__str__` method.
- **Methods**: 
  - `def __init__(self, size):`
  - `def area(self):`
  - `def __str__(self):`

## Usage 🛠️

Each file can be executed individually to test the classes and their methods. Make sure you have Python 3 installed on your machine.

```bash
python3 0-main.py
python3 1-main.py
# etc.