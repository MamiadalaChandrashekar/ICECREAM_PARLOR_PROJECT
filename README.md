# ICECREAM_PARLOR_PROJECT


## Steps to Run the Application

### Using Python and Streamlit

1. **Navigate to Project Directory**:
    ```bash
    cd path_to_your_project/ice_cream_parlor_project
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r src/requirements.txt
    ```

3. **Run the Streamlit Application**:
    ```bash
    streamlit run src/app.py
    ```

4. **Access the Application**:
    Open your browser and go to `http://localhost:8501`.

### Using Docker

1. **Build the Docker Image**:
    ```bash
    docker build -t ice_cream_parlor_app .
    ```

2. **Run the Docker Container**:
    ```bash
    docker run -p 8501:8501 ice_cream_parlor_app
    ```

3. **Access the Application**:
    Open your browser and go to `http://localhost:8501`.

## Documentation of Test Steps

1. **Add a New Flavor**:
    - Open the application.
    - Enter a flavor name in the "Flavor Name" text input.
    - Check the "Is Seasonal" checkbox if the flavor is seasonal.
    - Click the "Add Flavor" button.
    - Verify that a success message is displayed and the new flavor appears in the list of flavors.

2. **View All Flavors**:
    - Open the application.
    - Scroll down to the "Flavors" section.
    - Verify that the list of flavors is displayed correctly.

## SQL Query or ORM Abstraction Implementation

The application uses SQLite for data storage. The SQL queries are implemented using the `sqlite3` module in Python. For example:

```python
def add_flavor(db_path, name, is_seasonal):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO flavors (name, is_seasonal) VALUES (?, ?)', (name, is_seasonal))
    conn.commit()
    conn.close()


![image](https://github.com/MamiadalaChandrashekar/ICECREAM_PARLOR_PROJECT/assets/130646818/1c9d11c4-0926-404b-835b-490c518b4546)
![image](https://github.com/MamiadalaChandrashekar/ICECREAM_PARLOR_PROJECT/assets/130646818/8688c850-f7a8-46a2-98ef-009c4456bc9a)
![image](https://github.com/MamiadalaChandrashekar/ICECREAM_PARLOR_PROJECT/assets/130646818/a34434e6-c599-4dca-a77a-a73812f41879)
