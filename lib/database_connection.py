import os

import psycopg
from flask import g
from psycopg.rows import dict_row

# This class helps us interact with the database.
# It wraps the underlying psycopg library that we are using.


# If the below seems too complex right now, that's OK.
# That's why we have provided it!
class DatabaseConnection:

    def __init__(self, test_mode=False) -> None:
        self.test_mode = test_mode

    def connect(self) -> None:
        db_user = os.environ.get("POSTGRES_USER")
        db_password = os.environ.get("POSTGRES_PASSWORD")
        db_host = os.environ.get("POSTGRES_HOSTNAME")
        db_port = os.environ.get("POSTGRES_PORT")
        db_name = os.environ.get("POSTGRES_DB", "music_library")
        environment = os.environ.get("APP_ENV", "TESTING")
        if environment == "PRODUCTION":
            try:
                self.connection = psycopg.connect(
                    f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}", row_factory=dict_row
                )
            except psycopg.OperationalError:
                raise Exception( f"Couldn't connect -> {db_user}:PASSWORD@{db_host}:{db_port}/{db_name}")
        else:
            try:
                self.connection = psycopg.connect( 
                    f"postgresql://localhost/{db_name}", row_factory=dict_row
                )
            except psycopg.OperationalError:
                raise Exception( f"Couldn't connect -> localhost/{db_name}")


    # This method seeds the database with the given SQL file.
    # We use it to set up our database ready for our tests or application.
    def seed(self, sql_filename) -> None:
        self._check_connection()
        if not os.path.exists(sql_filename):
            raise Exception(f"File {sql_filename} does not exist")
        with self.connection.cursor() as cursor:
            cursor.execute(open(sql_filename).read())
            self.connection.commit()

    # This method executes an SQL query on the database.
    # It allows you to set some parameters too. You'll learn about this later.
    def execute(self, query, params=None):
        if params is None:
            params = []
        self._check_connection()
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            result = cursor.fetchall() if cursor.description is not None else None
            self.connection.commit()
            return result

    CONNECTION_MESSAGE = (
        ""
        "DatabaseConnection.exec_params: Cannot run a SQL query as "
        "the connection to the database was never opened. Did you "
        "make sure to call first the method DatabaseConnection.connect` "
        "in your app.py file (or in your tests)?"
    )

    # This private method checks that we're connected to the database.
    def _check_connection(self) -> None:
        if self.connection is None:
            raise Exception(self.CONNECTION_MESSAGE)

# This function integrates with Flask to create one database connection that
# Flask request can use. To see how to use it, look at example_routes.py
def get_flask_database_connection(app):
    if not hasattr(g, "flask_database_connection"):
        g.flask_database_connection = DatabaseConnection(
            test_mode=(
                (os.getenv("APP_ENV") == "test") or (app.config["TESTING"] is True)
            )
        )
        g.flask_database_connection.connect()
    return g.flask_database_connection
