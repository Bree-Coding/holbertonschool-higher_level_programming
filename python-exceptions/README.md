# Python - Exceptions 🐍

This project focuses on handling exceptions in Python. Below are the tasks and their descriptions:

---

## 0. Safe list printing ✅
Write a function that prints `x` elements of a list.

- **Prototype**: `def safe_print_list(my_list=[], x=0):`
- **Details**:
  - Prints elements of `my_list` on the same line followed by a new line.
  - Returns the real number of elements printed.
  - Handles cases where `x` is greater than the length of `my_list`.
  - Uses `try` / `except`.
- **File**: `0-safe_print_list.py`

---

## 1. Safe printing of an integers list 🔢
Write a function that prints an integer using `"{:d}".format()`.

- **Prototype**: `def safe_print_integer(value):`
- **Details**:
  - Prints the integer followed by a new line.
  - Returns `True` if the value is an integer and was printed successfully, otherwise `False`.
  - Uses `try` / `except`.
- **File**: `1-safe_print_integer.py`

---

## 2. Print and count integers 🔍
Write a function that prints the first `x` elements of a list and only integers.

- **Prototype**: `def safe_print_list_integers(my_list=[], x=0):`
- **Details**:
  - Prints integers on the same line followed by a new line.
  - Skips non-integer elements silently.
  - Returns the real number of integers printed.
  - Uses `try` / `except`.
- **File**: `2-safe_print_list_integers.py`

---

## 3. Integers division with debug ➗
Write a function that divides 2 integers and prints the result.

- **Prototype**: `def safe_print_division(a, b):`
- **Details**:
  - Prints the result in the `finally` block preceded by `Inside result:`.
  - Returns the result of the division, or `None` if division by zero occurs.
  - Uses `try` / `except` / `finally`.
- **File**: `3-safe_print_division.py`

---

## 4. Divide a list 📋
Write a function that divides element by element 2 lists.

- **Prototype**: `def list_division(my_list_1, my_list_2, list_length):`
- **Details**:
  - Returns a new list with the division results.
  - Handles:
    - Division by zero (`division by 0`).
    - Non-numeric elements (`wrong type`).
    - Out-of-range indices (`out of range`).
  - Uses `try` / `except` / `finally`.
- **File**: `4-list_division.py`

---

## 5. Raise exception 🚨
Write a function that raises a type exception.

- **Prototype**: `def raise_exception():`
- **Details**:
  - Raises a `TypeError` exception.
- **File**: `5-raise_exception.py`

---

## 6. Raise a message 📨
Write a function that raises a name exception with a message.

- **Prototype**: `def raise_exception_msg(message=""):`
- **Details**:
  - Raises a `NameError` exception with the provided message.
- **File**: `6-raise_exception_msg.py`

---

## Repository 📂
- **GitHub Repository**: [holbertonschool-higher_level_programming](https://github.com/holbertonschool-higher_level_programming)
- **Directory**: `python-exceptions`