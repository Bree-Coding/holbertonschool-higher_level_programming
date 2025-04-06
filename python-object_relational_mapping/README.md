# Python Object Relational Mapping (ORM) 🐍🗄️

This project focuses on using **Python** to interact with **MySQL databases** via **MySQLdb** and **SQLAlchemy**. Below are the tasks and their descriptions:

---

## Requirements 🛠️

### Install MySQL 8.0 on Ubuntu 20.04 LTS
1. Update your package list:
   ```bash
   $ sudo apt update
   ```
2. Install MySQL server:
   ```bash
   $ sudo apt install mysql-server
   ```
3. Verify the installation:
   ```bash
   $ mysql --version
   mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
   ```

4. Connect to your MySQL server:
   ```bash
   $ sudo mysql
   Welcome to the MySQL monitor.  Commands end with ; or \g.
   Your MySQL connection id is 11
   Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

   mysql> quit
   Bye
   ```

---

### Install MySQLdb module version 2.0.x
1. Ensure MySQL is installed.
2. Install the required dependencies:
   ```bash
   $ sudo apt-get install python3-dev
   $ sudo apt-get install libmysqlclient-dev
   $ sudo apt-get install zlib1g-dev
   ```
3. Install the `mysqlclient` module:
   ```bash
   $ sudo pip3 install mysqlclient
   ```
4. Verify the installation:
   ```bash
   $ python3
   >>> import MySQLdb
   >>> MySQLdb.version_info 
   (2, 0, 3, 'final', 0)
   ```

---

### Install SQLAlchemy module version 1.4.x
1. Install the `SQLAlchemy` module:
   ```bash
   $ sudo pip3 install SQLAlchemy
   ```
2. Verify the installation:
   ```bash
   $ python3
   >>> import sqlalchemy
   >>> sqlalchemy.__version__ 
   '1.4.22'
   ```

3. If you see the following warning, you can safely ignore it:
   ```
   /usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be removed in a future release.")                                                                                                                    
     cursor.execute(statement, parameters)  
   ```

---

## 0. Get all states 🗂️
Write a script that lists all states from the database `hbtn_0e_0_usa`.

- **File**: `0-select_states.py`
- **Description**: Connects to the database and retrieves all states sorted by `id`.
- **Command**:
  ```bash
  ./0-select_states.py <mysql_username> <mysql_password> <database_name>
  ```
- **Example Output**:
  ```
  (1, 'California')
  (2, 'Arizona')
  (3, 'Texas')
  ```

---

## 1. Filter states 🔍
Write a script that lists all states with names starting with `N` from the database `hbtn_0e_0_usa`.

- **File**: `1-filter_states.py`
- **Description**: Filters states whose names start with `N`.
- **Command**:
  ```bash
  ./1-filter_states.py <mysql_username> <mysql_password> <database_name>
  ```
- **Example Output**:
  ```
  (4, 'New York')
  (5, 'Nevada')
  ```

---

## 2. Filter states by user input 🧑‍💻
Write a script that takes in an argument and displays all values in the `states` table where `name` matches the argument.

- **File**: `2-my_filter_states.py`
- **Description**: Displays states matching the user-provided name.
- **Command**:
  ```bash
  ./2-my_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>
  ```
- **Example Output**:
  ```
  (2, 'Arizona')
  ```

---

## 3. SQL Injection... 🚨
Write a script that is safe from SQL injection and displays all values in the `states` table where `name` matches the argument.

- **File**: `3-my_safe_filter_states.py`
- **Description**: Uses parameterized queries to prevent SQL injection.
- **Command**:
  ```bash
  ./3-my_safe_filter_states.py <mysql_username> <mysql_password> <database_name> <state_name>
  ```
- **Example Output**:
  ```
  (2, 'Arizona')
  ```

---

## 4. Cities by states 🏙️
Write a script that lists all cities from the database `hbtn_0e_4_usa`.

- **File**: `4-cities_by_state.py`
- **Description**: Retrieves all cities and their corresponding states.
- **Command**:
  ```bash
  ./4-cities_by_state.py <mysql_username> <mysql_password> <database_name>
  ```
- **Example Output**:
  ```
  (1, 'San Francisco', 'California')
  (2, 'San Jose', 'California')
  ```

---

## 5. All cities by state 🗺️
Write a script that lists all cities of a given state.

- **File**: `5-filter_cities.py`
- **Description**: Displays cities of a specific state.
- **Command**:
  ```bash
  ./5-filter_cities.py <mysql_username> <mysql_password> <database_name> <state_name>
  ```
- **Example Output**:
  ```
  Dallas, Houston, Austin
  ```

---

## 6. First state model 🏛️
Write a Python file that contains the class definition of a `State`.

- **File**: `model_state.py`
- **Description**: Defines the `State` class and links it to the `states` table.
- **Command**:
  ```bash
  ./6-model_state.py <mysql_username> <mysql_password> <database_name>
  ```

---

## 7. All states via SQLAlchemy 🗃️
Write a script that lists all `State` objects from the database `hbtn_0e_6_usa`.

- **File**: `7-model_state_fetch_all.py`
- **Description**: Retrieves all states using SQLAlchemy.
- **Command**:
  ```bash
  ./7-model_state_fetch_all.py <mysql_username> <mysql_password> <database_name>
  ```
- **Example Output**:
  ```
  1: California
  2: Arizona
  ```

---

## 8. First state 🥇
Write a script that prints the first `State` object from the database.

- **File**: `8-model_state_fetch_first.py`
- **Description**: Retrieves the first state in the database.
- **Command**:
  ```bash
  ./8-model_state_fetch_first.py <mysql_username> <mysql_password> <database_name>
  ```
- **Example Output**:
  ```
  1: California
  ```

---

## 9. Contains `a` 🔤
Write a script that lists all `State` objects containing the letter `a`.

- **File**: `9-model_state_filter_a.py`
- **Description**: Filters states containing the letter `a`.
- **Command**:
  ```bash
  ./9-model_state_filter_a.py <mysql_username> <mysql_password> <database_name>
  ```
- **Example Output**:
  ```
  1: California
  2: Arizona
  ```

---

## 10. Get a state 🔎
Write a script that prints the `State` object with the name passed as an argument.

- **File**: `10-model_state_my_get.py`
- **Description**: Retrieves a state by name.
- **Command**:
  ```bash
  ./10-model_state_my_get.py <mysql_username> <mysql_password> <database_name> <state_name>
  ```
- **Example Output**:
  ```
  3
  ```

---

## 11. Add a new state ➕
Write a script that adds the `State` object “Louisiana” to the database.

- **File**: `11-model_state_insert.py`
- **Description**: Adds a new state to the database.
- **Command**:
  ```bash
  ./11-model_state_insert.py <mysql_username> <mysql_password> <database_name>
  ```
- **Example Output**:
  ```
  6
  ```

---

## 12. Update a state ✏️
Write a script that changes the name of the `State` object with `id = 2` to “New Mexico”.

- **File**: `12-model_state_update_id_2.py`
- **Description**: Updates a state's name.
- **Command**:
  ```bash
  ./12-model_state_update_id_2.py <mysql_username> <mysql_password> <database_name>
  ```

---

## 13. Delete states ❌
Write a script that deletes all `State` objects with a name containing the letter `a`.

- **File**: `13-model_state_delete_a.py`
- **Description**: Deletes states containing the letter `a`.
- **Command**:
  ```bash
  ./13-model_state_delete_a.py <mysql_username> <mysql_password> <database_name>
  ```

---

## 14. Cities in state 🏙️
Write a Python file `model_city.py` and a script to print all `City` objects.

- **File**: `model_city.py`, `14-model_city_fetch_by_state.py`
- **Description**: Prints all cities with their states.
- **Command**:
  ```bash
  ./14-model_city_fetch_by_state.py <mysql_username> <mysql_password> <database_name>
  ```
- **Example Output**:
  ```
  California: (1) San Francisco
  California: (2) San Jose
  ```