# Python - Abstract Classes and Interfaces

# 🐍 0. Abstract Animal Class and its Subclasses

## 🎯 Objective:
- Create an abstract class named `Animal` using the ABC package.
- Create two subclasses of `Animal`: `Dog` and `Cat`. Implement the `sound` method in each subclass to return the strings “Bark” and “Meow” respectively.

## 📚 Resources:
- [Python ABC documentation](https://docs.python.org/3/library/abc.html)

## 📝 Instructions:
### Setting up the Abstract Class:
1. Import the necessary components from the `abc` module.
2. Define the `Animal` class, ensuring it inherits from `ABC` to mark it as abstract.
3. Inside the `Animal` class, declare an abstract method named `sound` using the `@abstractmethod` decorator.

### Implementing the Subclasses:
1. Create a subclass named `Dog` that inherits from the `Animal` class.
2. Implement the `sound` method in the `Dog` class to return the string “Bark”.
3. Similarly, create a subclass named `Cat` that also inherits from the `Animal` class.
4. Implement the `sound` method in the `Cat` class to return the string “Meow”.

## 💡 Hints:
- The abstract method in the base class doesn’t have a body. You need to provide the implementation in the subclasses.
- If you try to instantiate a class that hasn’t implemented all of its abstract methods, Python will raise a `TypeError`.

---

# 🟦 1. Shapes, Interfaces, and Duck Typing

## 🎯 Objective:
- Create an abstract class named `Shape` with two abstract methods: `area` and `perimeter`.
- Implement two concrete classes: `Circle` and `Rectangle`, both inheriting from `Shape`. Each class should provide implementations for the `area` and `perimeter` methods.
- Write a standalone function named `shape_info` that accepts an object of type `Shape` (by duck typing) and prints its area and perimeter.

## 📚 Resources:
- [Python ABC documentation](https://docs.python.org/3/library/abc.html)
- [Concept of Duck Typing](https://realpython.com/lessons/duck-typing/)

## 📝 Instructions:
### Shape Abstract Class:
1. Define an abstract class `Shape` using the ABC package.
2. Within `Shape`, declare two abstract methods: `area` and `perimeter`.

### Circle and Rectangle Classes:
1. Create a `Circle` class that inherits from `Shape`. The constructor (`__init__`) should accept a radius. Implement the `area` and `perimeter` methods.
2. Create a `Rectangle` class, also inheriting from `Shape`. Its constructor should accept the width and height. Implement the `area` and `perimeter` methods.

### shape_info Function:
1. Define a function named `shape_info` that takes a single argument.
2. Without explicitly checking the type of the argument, call its `area` and `perimeter` methods (relying on duck typing).
3. Print the area and perimeter of the shape passed to the function.

## 💡 Hints:
- While Python doesn’t enforce interfaces in the same way as statically-typed languages, abstract base classes provide a mechanism to ensure certain methods are implemented in subclasses.
- Duck typing in the `shape_info` function implies that you shouldn’t use `isinstance` checks. Instead, trust that the passed object adheres to the `Shape` interface.

---

# 📋 2. Extending the Python List with Notifications

## 🎯 Objective:
- Create a class named `VerboseList` that extends the Python list class. This custom class should print a notification message every time an item is added (using the `append` or `extend` methods) or removed (using the `remove` or `pop` methods).

## 📝 Instructions:
### Setting up the VerboseList Class:
1. Define a class `VerboseList` that inherits from the built-in list class.
2. Within `VerboseList`, override the methods that modify the list: `append`, `extend`, `remove`, and `pop`.

### Implementing Notifications:
1. For the `append` method: After adding the item to the list, print a message like “Added [item] to the list.”
2. For the `extend` method: After extending the list, print a message like “Extended the list with [x] items.” where [x] is the number of items added.
3. For the `remove` method: Before removing the item from the list, print a message like “Removed [item] from the list.”
4. For the `pop` method: Before popping the item from the list, print a message like “Popped [item] from the list.” If the index is not specified, default behavior is to pop the last item.

## 💡 Hints:
- Remember to call the original method of the list class using the `super()` function to ensure that the original functionality is retained. For example, for `append`: `super().append(item)`.
- Think about edge cases, such as trying to remove an item that doesn’t exist in the list.

---

# 🔢 3. CountedIterator - Keeping Track of Iteration

## 🎯 Objective:
- Create a class named `CountedIterator` that extends the built-in iterator obtained from the `iter` function. The `CountedIterator` should keep track of the number of items that have been iterated over.

## 📝 Instructions:
### Setting up the CountedIterator Class:
1. Define a class `CountedIterator`.
2. In the constructor (`__init__`), initialize two attributes: the iterator object (using the `iter` function) and a counter to track the number of items iterated.
3. Provide a method `get_count` to return the current value of the counter.

### Overriding the next Method:
1. Within the `CountedIterator` class, override the `__next__` method.
2. In this method, increment the counter each time the `__next__` method is called.
3. Fetch the next item from the original iterator and return it. If there are no items left to iterate, the method should raise the `StopIteration` exception.

## 💡 Hints:
- Remember that the `__next__` method should raise a `StopIteration` exception when there are no more items to iterate, so ensure this behavior is retained in your overridden method.
- You can initialize the iterator object in the `CountedIterator` constructor using: `self.iterator = iter(some_iterable)`.

---

# 🐟 4. The Enigmatic FlyingFish - Exploring Multiple Inheritance

## 🎯 Objective:
- Construct a `FlyingFish` class that inherits from both a `Fish` class and a `Bird` class. Within `FlyingFish`, override methods from both parents.

## 📝 Instructions:
### Parent Classes Setup:
1. Create a `Fish` class with methods `swim` (which prints “The fish is swimming”) and `habitat` (which prints “The fish lives in water”).
2. Create a `Bird` class with methods `fly` (which prints “The bird is flying”) and `habitat` (which prints “The bird lives in the sky”).

### Implementing FlyingFish:
1. Construct a `FlyingFish` class that inherits from both `Fish` and `Bird`.
2. Override the `fly` method to print “The flying fish is soaring!”.
3. Override the `swim` method to print “The flying fish is swimming!”.
4. Override the `habitat` method to print “The flying fish lives both in water and the sky!”.

## 💡 Hints:
- Consider the order in which you list the parent classes when defining `FlyingFish`. It affects the method resolution order.
- While multiple inheritance can be a powerful tool, it should be used judiciously, as it can make the code more complex and harder to read.

---

# 🐉 5. The Mystical Dragon - Mastering Mixins

## 🎯 Objective:
- Design two mixin classes, `SwimMixin` and `FlyMixin`, each equipped with methods `swim` and `fly` respectively. Next, construct a class `Dragon` that inherits from both these mixins.

## 📝 Instructions:
### Creating Mixins:
1. Design a mixin called `SwimMixin` with a method `swim` that prints “The creature swims!”.
2. Design another mixin called `FlyMixin` with a method `fly` that prints “The creature flies!”.

### Implementing Dragon:
1. Construct a class named `Dragon` that inherits from both `SwimMixin` and `FlyMixin`.
2. Within the `Dragon` class, you can add additional methods or attributes if desired, such as `roar`, which could print “The dragon roars!”.

## 💡 Hints:
- While designing mixins, remember that they should be focused, providing a single piece of functionality. They shouldn’t be overly broad or try to manage too much behavior.
- Mixins allow for code reusability and can be combined in various ways to give objects different capabilities without setting up complex inheritance hierarchies.