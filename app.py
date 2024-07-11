from flask import Flask, render_template, request, redirect, url_for
from service import ToDoService

app = Flask(__name__)
service = ToDoService()

@app.route('/')
def index():
    todos = service.get_all_todos()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form['title']
    description = request.form['description']
    due_date = request.form['due_date']
    user_id = 7  # Assuming a single user for simplicity
    service.add_todo(title, description, due_date, user_id)
    return redirect(url_for('index'))

@app.route('/update/<int:todo_id>', methods=['POST'])
def update_todo(todo_id):
    title = request.form['title']
    description = request.form['description']
    due_date = request.form['due_date']
    is_done = 'is_done' in request.form
    service.update_todo(todo_id, title, description, due_date, is_done)
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    service.delete_todo(todo_id)
    return redirect(url_for('index'))

@app.route('/deleted')
def deleted_todos():
    deleted_todos = service.get_deleted_todos()
    return render_template('deleted.html', todos=deleted_todos)

@app.route('/completed')
def completed_todos():
    completed_todos = service.get_completed_todos()
    return render_template('completed.html', todos=completed_todos)

if __name__ == '__main__':
    app.run(debug=True)
