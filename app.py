from flask import Flask, render_template, request, redirect, url_for
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)

class ToDoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200))
    summary = db.Column(db.String(500))

with app.app_context():
    db.create_all()

resource_fields = {
    'id': fields.Integer,
    'task': fields.String,
    'summary': fields.String
}

task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task", type=str, help="Task is required.", required=True)
task_post_args.add_argument("summary", type=str, help="Summary is required.", required=True)

task_update_args = reqparse.RequestParser()
task_update_args.add_argument("task", type=str)
task_update_args.add_argument("summary", type=str)

# Home route to render the main page
@app.route('/')
def index():
    tasks = ToDoModel.query.all()
    return render_template('index.html', tasks=tasks)

# To handle the form submission for adding a new task
@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form['task']
    task_summary = request.form['summary']
    new_task = ToDoModel(task=task_content, summary=task_summary)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

# To handle the form submission for updating an existing task
@app.route('/update/<int:id>', methods=['POST'])
def update_task(id):
    task = ToDoModel.query.get_or_404(id)
    task.task = request.form['task']
    task.summary = request.form['summary']
    db.session.commit()
    return redirect(url_for('index'))

# To handle the deletion of a task
@app.route('/delete/<int:id>', methods=['POST'])
def delete_task(id):
    task = ToDoModel.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

# RESTful API routes
class ToDolist(Resource):
    def get(self):
        tasks = ToDoModel.query.all()
        todos = {}
        for task in tasks:
            todos[task.id] = {"task": task.task, "summary": task.summary}
        return todos

class ToDo(Resource):
    @marshal_with(resource_fields)
    def get(self, todo_id):
        task = ToDoModel.query.filter_by(id=todo_id).first()
        if not task:
            abort(404, message="Could not find task with that id...")
        return task

    @marshal_with(resource_fields)
    def post(self, todo_id):
        args = task_post_args.parse_args()
        task = ToDoModel.query.filter_by(id=todo_id).first()
        if task:
            abort(409, message="Task ID taken...")
        todo = ToDoModel(id=todo_id, task=args['task'], summary=args['summary'])
        db.session.add(todo)
        db.session.commit()
        return todo, 201

    @marshal_with(resource_fields)
    def put(self, todo_id):
        args = task_update_args.parse_args()
        task = ToDoModel.query.filter_by(id=todo_id).first()
        if not task:
            abort(404, message="Task does not exist, cannot update.")
        if args['task']:
            task.task = args["task"]
        if args['summary']:
            task.summary = args["summary"]
        db.session.commit()
        return task

    def delete(self, todo_id):
        task = ToDoModel.query.filter_by(id=todo_id).first()
        if not task:
            abort(404, message="Task does not exist.")
        db.session.delete(task)
        db.session.commit()
        return 'ToDo deleted', 204

api.add_resource(ToDolist, '/todos')
api.add_resource(ToDo, '/todos/<int:todo_id>')

if __name__ == "__main__":
    app.run(debug=True)
