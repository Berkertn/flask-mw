def ensure_database_exists(config):
    """Ensure that the database exists, and create it if not."""
    from psycopg2 import sql
    import psycopg2

    db_name = config['DB_NAME']
    user = config['DB_USER']
    password = config['DB_PASSWORD']
    host = config['DB_HOST']
    port = config['DB_PORT']

    try:
        # try with wanted DB
        conn = psycopg2.connect(dbname=db_name, user=user, password=password, host=host, port=port)
        conn.close()
        print(f"Database '{db_name}' already exists.")
    except psycopg2.OperationalError as e:
        # If there's no DB for wanted name, first connect to postgres to ensure there's a DB we can connect to
        if "does not exist" in str(e):
            try:
                print(f"Database '{db_name}' does not exist. Creating...")
                conn = psycopg2.connect(dbname="postgres", user=user, password=password, host=host, port=port)
                conn.autocommit = True
                cursor = conn.cursor()

                # create db for wanted name
                cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
                print(f"Database '{db_name}' created successfully!")
            except Exception as create_error:
                print(f"Error while creating database: {create_error}")
            finally:
                if 'cursor' in locals():
                    cursor.close()
                if 'conn' in locals():
                    conn.close()
        else:
            print(f"Unexpected error: {e}")
