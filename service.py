from models import Database

class ToDoService:
    def __init__(self):
        self.db = Database()

    def get_all_todos(self):
        return self.db.get_all_todos()

    def add_todo(self, title, description, due_date, user_id):
        self.db.add_todo(title, description, due_date, user_id)

    def update_todo(self, todo_id, title, description, due_date, is_done):
        self.db.update_todo(todo_id, title, description, due_date, is_done)

    def delete_todo(self, todo_id):
        self.db.delete_todo(todo_id)

    def get_deleted_todos(self):
        return self.db.get_deleted_todos()

    def get_completed_todos(self):
        return self.db.get_completed_todos()
