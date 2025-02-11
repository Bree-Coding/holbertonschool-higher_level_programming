# Python Serialization Tasks 📦

## 0. Basic Serialization 📝

Create a basic serialization module that adds the functionality to serialize a Python dictionary to a JSON file and deserialize the JSON file to recreate the Python Dictionary.

### Instructions:
- Write a Python module named `task_00_basic_serialization.py` with the following functions:
  - `serialize_and_save_to_file(data, filename)`: Serialize and save data to the specified file.
  - `load_and_deserialize(filename)`: Load and deserialize data from the specified file.

### Functions:
- `serialize_and_save_to_file(data, filename)`
  - `data`: A Python Dictionary with data.
  - `filename`: The filename of the output JSON file. If the output file already exists it should be replaced.
- `load_and_deserialize(filename)`
  - `filename`: The filename of the input JSON file. This function returns a Python Dictionary with the deserialized JSON data from the file.

## 1. Pickling Custom Classes 🥒

Learn how to serialize and deserialize custom Python objects using the pickle module.

### Instructions:
1. Create a custom Python class named `CustomObject` with the following attributes:
   - `name` (a string)
   - `age` (an integer)
   - `is_student` (a boolean)
   - A method `display` to print out the object’s attributes.
2. Implement two methods within this class:
   - `serialize(self, filename)`: Serialize the current instance of the object and save it to the provided filename.
   - `@classmethod deserialize(cls, filename)`: Load and return an instance of the `CustomObject` from the provided filename.
3. Save your code in a file named `task_01_pickle.py`.

## 2. Converting CSV Data to JSON Format 📊➡️📄

The objective of this exercise is to gain experience in reading data from one format (CSV) and converting it into another format (JSON) using serialization techniques.

### Instructions:
- Define a function named `convert_csv_to_json` that takes the CSV filename as its parameter and writes the JSON data to `data.json`.
- Handle exceptions, such as file not found. The function should return `False` in this case.
- Save your work in `task_02_csv.py`.

## 3. Serializing and Deserializing with XML 📄➡️📦

In this exercise, we’ll explore serialization and deserialization using XML as an alternative format to JSON.

### Instructions:
- Define two main functions:
  - `serialize_to_xml(dictionary, filename)`: Serialize the dictionary into XML and save it to the given filename.
  - `deserialize_from_xml(filename)`: Read the XML data from that file and return a deserialized Python dictionary.
- Be cautious about data types. XML doesn’t differentiate between numbers and strings, etc., like Python does. You might need to manage type conversions.
- Save your work in `task_03_xml.py`.

## Repository 📂

- **GitHub repository**: `holbertonschool-higher_level_programming`
- **Directory**: python-serialization

Happy coding! 🚀
