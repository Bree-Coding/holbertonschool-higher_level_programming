# Python - Test-driven Development 🐍✅

This repository contains tasks and exercises focused on **Test-driven Development (TDD)** in Python. Each task demonstrates the importance of writing tests before implementing functionality.

## Table of Contents 📋

1. [0. Integers addition ➕](#0-integers-addition-)
2. [1. Divide a matrix ➗](#1-divide-a-matrix-)
3. [2. Say my name 🗣️](#2-say-my-name-)
4. [3. Print square ⬛](#3-print-square-)
5. [4. Text indentation ✍️](#4-text-indentation-)
6. [5. Max integer - Unittest 🔢](#5-max-integer---unittest-)

---

### 0. Integers addition ➕

Write a function that adds 2 integers.

- **Prototype**: `def add_integer(a, b=98):`
- **Requirements**:
  - `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception.
  - Returns an integer: the addition of `a` and `b`.
  - You are not allowed to import any module.

---

### 1. Divide a matrix ➗

Write a function that divides all elements of a matrix.

- **Prototype**: `def matrix_divided(matrix, div):`
- **Requirements**:
  - `matrix` must be a list of lists of integers or floats.
  - Each row of the matrix must have the same size.
  - `div` must be a number (integer or float) and cannot be `0`.
  - Returns a new matrix with elements rounded to 2 decimal places.

---

### 2. Say my name 🗣️

Write a function that prints `My name is <first name> <last name>`.

- **Prototype**: `def say_my_name(first_name, last_name=""):`
- **Requirements**:
  - `first_name` and `last_name` must be strings, otherwise raise a `TypeError` exception.
  - You are not allowed to import any module.

---

### 3. Print square ⬛

Write a function that prints a square with the character `#`.

- **Prototype**: `def print_square(size):`
- **Requirements**:
  - `size` must be an integer, otherwise raise a `TypeError` exception.
  - If `size` is less than `0`, raise a `ValueError` exception.
  - Prints a square of size `size`.

---

### 4. Text indentation ✍️

Write a function that prints a text with 2 new lines after each of these characters: `.`, `?`, and `:`.

- **Prototype**: `def text_indentation(text):`
- **Requirements**:
  - `text` must be a string, otherwise raise a `TypeError` exception.
  - There should be no space at the beginning or at the end of each printed line.

---

### 5. Max integer - Unittest 🔢

Write unittests for the function `def max_integer(list=[])`.

- **Requirements**:
  - Your test file should be inside a folder `tests`.
  - Use the `unittest` module.
  - Test edge cases, including empty lists, single-element lists, and mixed data types.

---

## How to Run 🏃‍♂️

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/holbertonschool-higher_level_programming.git