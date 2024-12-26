# AI-MW-Project:

***Description: This is a MW project to connect DB to get,post,update the analysis, test cases and project sends data to
UI***

**Capabilities:**

- DB creation will be done automatically by the application according to selected env from config file.
    - preconditions:
        - postgresql is installed and running
        - port, user creds should add config.py
- tables will create automatically
- /get endpoint will be implemented and return all the analysis from analysis table
- global exceptions added to ensure the application is running without any crash

**TODO:**

- get analysis with filters (filter will be giving as list)
- logger implementation
- post analysis to add analyse data to table
- go project will be use MW to add or get data
- config.py can be orchestrated better way? (yaml, env file or something else)

**Tech:**

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- psycopg2 (postgresql)
- flask-restx
- SQLAlchemy

**Table Column Changes:**

- if you want to upgrade your changes like table columns

```bash
flask db migrate -m "Added created_at column to Analysis"
flask db upgrade
```

- if you want to downgrade (version is under the app/migrations folder), you can use `flask db downgrade`

```bash
flask db downgrade <target_version>
```
