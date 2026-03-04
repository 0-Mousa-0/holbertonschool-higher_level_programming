# python-object_relational_mapping

This directory contains solutions for Object-Relational Mapping tasks using:

- **MySQLdb** (raw SQL from Python)
- **SQLAlchemy ORM** (model-based database access)

All Python files include:

- a shebang (`#!/usr/bin/python3`)
- a module docstring (Python-style comment/documentation)
- inline comments for key query or ORM steps

## Requirements

- Python 3
- MySQL server running on `localhost:3306`
- Packages:
  - `mysqlclient` (provides `MySQLdb`)
  - `SQLAlchemy`

Install dependencies:

```bash
pip install mysqlclient SQLAlchemy
```

## SQL setup snippets (with SQL comments)

Use these examples to prepare local databases before running scripts:

```sql
-- Setup for tasks 0 to 3 (states table)
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name)
VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
```

```sql
-- Setup for tasks 4 and 5 (states + cities)
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
```

## Files and explanation

### MySQLdb scripts

0. **0-select_states.py**  
   Lists all states ordered by `states.id`.

1. **1-filter_states.py**  
   Lists states where the name starts with upper-case `N`.

2. **2-my_filter_states.py**  
   Filters by user-provided state name using string formatting (`format`) as requested.

3. **3-my_safe_filter_states.py**  
   Same as task 2 but safe against SQL injection using query parameters.

4. **4-cities_by_state.py**  
   Lists all cities with state names, ordered by `cities.id` (single `execute()` call).

5. **5-filter_cities.py**  
   Lists city names for a provided state (injection-safe), printed as a comma-separated line.

### SQLAlchemy model

6. **model_state.py**  
   Defines:
   - `Base = declarative_base()`
   - `State` class mapped to `states` with:
     - `id` (PK, int, auto-generated, non-null)
     - `name` (string(128), non-null)

### SQLAlchemy query scripts

7. **7-model_state_fetch_all.py**  
   Prints all states as `id: name`.

8. **8-model_state_fetch_first.py**  
   Prints first state by `id`, or `Nothing` if table is empty.

9. **9-model_state_filter_a.py**  
   Prints states containing letter `a`.

10. **10-model_state_my_get.py**  
    Prints `id` of state matching given name, else `Not found`.

11. **11-model_state_insert.py**  
    Inserts `"Louisiana"` and prints new state id.

12. **12-model_state_update_id_2.py**  
    Updates state with `id = 2` to `"New Mexico"`.

13. **13-model_state_delete_a.py**  
    Deletes states containing letter `a`.

### City model and joined fetch

14. **model_city.py**  
    Defines `City` model mapped to `cities` with:
    - `id` (PK)
    - `name` (string(128), non-null)
    - `state_id` (FK to `states.id`, non-null)

15. **14-model_city_fetch_by_state.py**  
    Prints cities and related state names as:  
    `<state name>: (<city id>) <city name>`

## How to run

For MySQLdb tasks:

```bash
./0-select_states.py <mysql_user> <mysql_password> <database_name>
./1-filter_states.py <mysql_user> <mysql_password> <database_name>
./2-my_filter_states.py <mysql_user> <mysql_password> <database_name> <state_name>
./3-my_safe_filter_states.py <mysql_user> <mysql_password> <database_name> <state_name>
./4-cities_by_state.py <mysql_user> <mysql_password> <database_name>
./5-filter_cities.py <mysql_user> <mysql_password> <database_name> <state_name>
```

For SQLAlchemy tasks:

```bash
./7-model_state_fetch_all.py <mysql_user> <mysql_password> <database_name>
./8-model_state_fetch_first.py <mysql_user> <mysql_password> <database_name>
./9-model_state_filter_a.py <mysql_user> <mysql_password> <database_name>
./10-model_state_my_get.py <mysql_user> <mysql_password> <database_name> <state_name>
./11-model_state_insert.py <mysql_user> <mysql_password> <database_name>
./12-model_state_update_id_2.py <mysql_user> <mysql_password> <database_name>
./13-model_state_delete_a.py <mysql_user> <mysql_password> <database_name>
./14-model_city_fetch_by_state.py <mysql_user> <mysql_password> <database_name>
```
