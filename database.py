import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_user_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )' )
        self.connection.commit()

    def add_user(self, username, password):
        self.cursor.execute('''INSERT INTO users (username, password) VALUES (?, ?)''', (username, password))
        self.connection.commit()

    def get_user(self, username):
        self.cursor.execute('''SELECT * FROM users WHERE username=?''', (username,))
        return self.cursor.fetchone()

    def create_payment_history_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            amount REAL,
            payment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )' )
        self.connection.commit()

    def add_payment(self, user_id, amount):
        self.cursor.execute('''INSERT INTO payments (user_id, amount) VALUES (?, ?)''', (user_id, amount))
        self.connection.commit()

    def get_payment_history(self, user_id):
        self.cursor.execute('''SELECT * FROM payments WHERE user_id=?''', (user_id,))
        return self.cursor.fetchall()

    def create_presentation_storage_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS presentations (
            id INTEGER PRIMARY KEY,
            title TEXT,
            content TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )' )
        self.connection.commit()

    def add_presentation(self, title, content):
        self.cursor.execute('''INSERT INTO presentations (title, content) VALUES (?, ?)''', (title, content))
        self.connection.commit()

    def get_presentations(self):
        self.cursor.execute('''SELECT * FROM presentations''')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

# Usage example
if __name__ == '__main__':
    db = DatabaseManager('app.db')
    db.create_user_table()
    db.create_payment_history_table()
    db.create_presentation_storage_table()