import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nik$$puppy99",
            database="todo_list"
        )
        self.cursor = self.conn.cursor()
        self.create_user_table()
        self.create_todo_table()

    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS User (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(30) NOT NULL UNIQUE
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def create_todo_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS Todo (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            description TEXT,
            created_on DATE DEFAULT (CURRENT_DATE),
            due_date DATE,
            is_deleted TINYINT(1) DEFAULT 0,
            is_done TINYINT(1) DEFAULT 0,
            user_id INT,
            FOREIGN KEY (user_id) REFERENCES User(id)
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def get_all_todos(self):
        query = "SELECT id, title, description, created_on, due_date, is_done FROM Todo WHERE is_deleted = 0"
        self.cursor.execute(query)
        todos = self.cursor.fetchall()
        return [{'id': row[0], 'title': row[1], 'description': row[2], 'created_on': row[3], 'due_date': row[4], 'is_done': row[5]} for row in todos]

    def add_todo(self, title, description, due_date, user_id):
        query = "INSERT INTO Todo (title, description, due_date, user_id) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (title, description, due_date, user_id))
        self.conn.commit()

    def update_todo(self, todo_id, title, description, due_date, is_done):
        query = "UPDATE Todo SET title=%s, description=%s, due_date=%s, is_done=%s WHERE id=%s"
        self.cursor.execute(query, (title, description, due_date, is_done, todo_id))
        self.conn.commit()

    def delete_todo(self, todo_id):
        query = "UPDATE Todo SET is_deleted = 1 WHERE id=%s"
        self.cursor.execute(query, (todo_id,))
        self.conn.commit()

    def get_deleted_todos(self):
        query = "SELECT id, title, description, created_on, due_date, is_done FROM Todo WHERE is_deleted = 1"
        self.cursor.execute(query)
        todos = self.cursor.fetchall()
        return [{'id': row[0], 'title': row[1], 'description': row[2], 'created_on': row[3], 'due_date': row[4], 'is_done': row[5]} for row in todos]

    def get_completed_todos(self):
        query = "SELECT id, title, description, created_on, due_date, is_done FROM Todo WHERE is_done = 1 AND is_deleted = 0"
        self.cursor.execute(query)
        todos = self.cursor.fetchall()
        return [{'id': row[0], 'title': row[1], 'description': row[2], 'created_on': row[3], 'due_date': row[4], 'is_done': row[5]} for row in todos]

    def __del__(self):
        self.cursor.close()
        self.conn.close()
