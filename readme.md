# Database Setup

Before running the application, ensure you have a PostgreSQL database named 'fruits' and execute the following SQL commands:

```sql
-- Create basket tables
CREATE TABLE basket_a (
   a INT PRIMARY KEY,
   fruit_a VARCHAR (100) NOT NULL
);

CREATE TABLE basket_b (
   b INT PRIMARY KEY,
   fruit_b VARCHAR (100) NOT NULL
);

-- Insert initial data
INSERT INTO basket_a (a, fruit_a)
VALUES
   (1, 'Apple'),
   (2, 'Orange'),
   (3, 'Banana'),
   (4, 'Cucumber');

INSERT INTO basket_b (b, fruit_b)
VALUES
   (1, 'Orange'),
   (2, 'Apple'),
   (3, 'Watermelon'),
   (4, 'Pear');

```
## Installation

### Setting Up Virtual Environment

1. Install Python 3 virtual environment package:
```bash
sudo apt-get install python3-venv
```
2. Create a virtual enviroment 
```bash
python3 -m venv python_venv
```
3. Activate the virtual Enviroment
```bash
source python_venv/bin/activate
```
### Installing dependencies
```bash
pip3 install -r requirements.txt
```

## Configuration

### Database Connection Setup

Open `main.py` and locate the `get_db_connection()` function. Update the database credentials with your PostgreSQL username and password:

```python
def get_db_connection():
   return psycopg2.connect(
       dbname="fruits",
       user="insertyourusernamehere",
       password="insertyourpasswordhere",
       host="localhost",
       port="5432"
   )
```
## Running the Application

1. Ensure your virtual environment is activated:
```bash
source python_venv/bin/activate
```
2, Run the Application : 
```bash
python main.py
```
3. Access the endpoints in your web browser :
```plaintext
http://127.0.0.1:5000/api/update_basket_a
http://127.0.0.1:5000/api/unique
```
Note: The server will run in production mode. To edit this change Debug = True with the main.py file. 