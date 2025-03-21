# 🐍 Python Server-Side Rendering

Welcome to the **Python Server-Side Rendering** project! This repository contains tasks that demonstrate how to use Flask and Jinja for dynamic web applications, file handling, and database integration.


## 📦 Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Jinja Documentation](https://jinja.palletsprojects.com/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)


## 📂 Project Structure

```
python-server_side_rendering/
├── database.py
├── items.json
├── products.csv
├── products.json
├── README.md
├── task_00_intro.py
├── task_01_jinja.py
├── task_02_logic.py
├── task_03_files.py
├── task_04_db.py
├── template.txt
├── templates/
│   ├── about.html
│   ├── contact.html
│   ├── footer.html
│   ├── header.html
│   ├── index.html
│   ├── items.html
│   ├── product_display.html
```

## 🚀 How to Run

1. **Install Flask:**
   ```bash
   pip install Flask
   ```

2. **Run a task:**
   For example, to run `task_01_jinja.py`:
   ```bash
   python3 task_01_jinja.py
   ```

3. **Access the application:**
   Open your browser and go to `http://localhost:5000`.

## 📝 Task Details

### Task 0: Creating a Simple Templating Program

**File:** [task_00_intro.py](task_00_intro.py)  
**Objective:** Generate personalized invitation files from a template with placeholders.

#### Instructions:
1. Use the provided `template.txt` file as a template.
2. Implement the function `generate_invitations(template, attendees)`.
3. Handle edge cases:
   - Empty template.
   - Empty list of attendees.
   - Missing data in attendee objects.

#### Example Data:
```python
attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]
```

---

### Task 1: Creating a Basic HTML Template in Flask

**File:** [task_01_jinja.py](task_01_jinja.py)  
**Objective:** Create a Flask application with reusable HTML templates.

#### Instructions:
1. Create a Flask app with routes for `/`, `/about`, and `/contact`.
2. Use `header.html` and `footer.html` for reusable headers and footers.
3. Add an `index.html` file with a simple list.

#### Example Routes:
- `/` → Displays the home page.
- `/about` → Displays the "About Us" page.
- `/contact` → Displays the "Contact Us" page.

---

### Task 2: Creating a Dynamic Template with Loops and Conditions

**File:** [task_02_logic.py](task_02_logic.py)  
**Objective:** Use Jinja loops and conditions to render dynamic content.

#### Instructions:
1. Create an `items.html` template to display a list of items.
2. Read data from `items.json` and pass it to the template.
3. Display "No items found" if the list is empty.

#### Example Data:
```json
{
    "items": ["Python Book", "Flask Mug", "Jinja Sticker"]
}
```

---

### Task 3: Displaying Data from JSON or CSV Files

**File:** [task_03_files.py](task_03_files.py)  
**Objective:** Read and display product data from JSON or CSV files.

#### Instructions:
1. Create a `product_display.html` template to display data in a table.
2. Implement routes to handle `source=json` or `source=csv`.
3. Filter products by `id` if provided.

#### Example Data:
- JSON: [products.json](products.json)
- CSV: [products.csv](products.csv)

---

### Task 4: Extending Dynamic Data Display to Include SQLite

**File:** [task_04_db.py](task_04_db.py)  
**Objective:** Add SQLite as a data source to the Flask application.

#### Instructions:
1. Set up a SQLite database with a `Products` table.
2. Extend the `/products` route to handle `source=sql`.
3. Reuse the `product_display.html` template to display data.

#### Example Database:
- Table: `Products`
- Columns: `id`, `name`, `category`, `price`

