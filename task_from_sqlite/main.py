import sqlite3
import os


class DataBase:
    def __init__(self, path: str):
        self.path = path
        self.connection = None
        self.cursor = None


    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self.cursor


    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.connection.rollback()
        else:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()


    def is_closed(self):
        connection_closed = True
        cursor_closed = True

        if self.connection is not None and self.cursor is not None:
            try:
                self.connection.execute('SELECT 1;')
                connection_closed = False
                self.cursor.execute('SELECT 1;')
                cursor_closed = False
            except sqlite3.ProgrammingError:
                pass

        print(f'Cursor open: {not cursor_closed}')
        print(f'Connection open: {not connection_closed}')

        return not all([cursor_closed, connection_closed])


path = os.path.join('C:/Users/User', 'database.db')
db = DataBase(path)

with db as my_cursor:
    print('The database is ready for use') if db.is_closed() else print('The database is not ready for use')
    my_cursor.execute('SELECT * FROM students')
    print(my_cursor.fetchall())
    print('The database is ready for use') if db.is_closed() else print('The database is not ready for use')
print('The database is ready for use') if db.is_closed() else print('The database is not ready for use')
