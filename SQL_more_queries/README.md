# SQL_more_queries

This directory contains SQL scripts for MySQL privilege management, database/table creation, and advanced query tasks.

Each task file:

- Is named exactly as required by the project statement.
- Starts with a first-line SQL comment using `--`.
- Can be executed by piping it into `mysql`.

## Requirements

- MySQL server running locally (`localhost`)
- A MySQL account with enough privileges (usually `root`)
- The `mysql` client available in your shell

## How to run scripts

From the repository root:

```bash
cat SQL_more_queries/<file>.sql | mysql -hlocalhost -uroot -p
```

If the task requires a specific database argument:

```bash
cat SQL_more_queries/<file>.sql | mysql -hlocalhost -uroot -p <database_name>
```

---

## Task-by-task explanation

### 0-privileges.sql
Lists grants for:

- `user_0d_1@localhost`
- `user_0d_2@localhost`

Useful to verify whether users exist and what privileges they have.

### 1-create_user.sql
Creates `user_0d_1@localhost` if it does not exist, sets password to `user_0d_1_pwd`, then grants all privileges on `*.*`.

### 2-create_read_user.sql
Creates database `hbtn_0d_2` if needed, creates `user_0d_2@localhost` if needed with password `user_0d_2_pwd`, then grants `SELECT` only on `hbtn_0d_2.*`.

### 3-force_name.sql
Creates table `force_name` with:

- `id INT`
- `name VARCHAR(256) NOT NULL`

Ensures `name` is mandatory.

### 4-never_empty.sql
Creates table `id_not_null` with:

- `id INT DEFAULT 1`
- `name VARCHAR(256)`

If `id` is omitted during insert, it becomes `1`.

### 5-unique_id.sql
Creates table `unique_id` with:

- `id INT DEFAULT 1 UNIQUE`
- `name VARCHAR(256)`

Ensures each `id` value is unique.

### 6-states.sql
Creates database `hbtn_0d_usa` if needed, selects it with `USE`, then creates table `states`:

- `id INT NOT NULL AUTO_INCREMENT PRIMARY KEY`
- `name VARCHAR(256) NOT NULL`

### 7-cities.sql
Creates database `hbtn_0d_usa` if needed, selects it, then creates table `cities`:

- `id INT NOT NULL AUTO_INCREMENT PRIMARY KEY`
- `state_id INT NOT NULL`
- `name VARCHAR(256) NOT NULL`
- Foreign key from `cities.state_id` to `states.id`

### 8-cities_of_california_subquery.sql
Lists cities that belong to California using a subquery (without `JOIN`) and sorts by `cities.id` ascending.

### 9-cities_by_state_join.sql
Lists all cities with their matching state names:

- `cities.id`
- `cities.name`
- `states.name`

Uses one `SELECT` statement and sorts by `cities.id` ascending.

### 10-genre_id_by_show.sql
From TV shows tables, lists only shows that have at least one genre:

- `tv_shows.title`
- `tv_show_genres.genre_id`

Uses one `SELECT` with `INNER JOIN` and sorts by title, then genre ID.

### 11-genre_id_all_shows.sql
Lists all shows, including those without genres:

- `tv_shows.title`
- `tv_show_genres.genre_id` (can be `NULL`)

Uses one `SELECT` with `LEFT JOIN` and sorts by title, then genre ID.

---

## Notes

- These scripts are intentionally idempotent where required (`IF NOT EXISTS`).
- For query-only tasks, scripts assume the required database/tables already exist.
