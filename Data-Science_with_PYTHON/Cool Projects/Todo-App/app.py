from flask import Flask, render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean())

@app.route("/")
def index():
    todo_list = Todo.query.all()  # Retrieve all to-do items from the database
    return render_template('index.html', todo_list=todo_list)




@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")  # Get the title from the form
    new_todo = Todo(title=title, complete=False)  # Create a new Todo object
    db.session.add(new_todo)  # Add the new object to the database session
    db.session.commit()  # Commit the session to save changes to the database
    return redirect(url_for("index"))  # Redirect back to the index page



@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()  # Get the to-do item by ID
    todo.complete = not todo.complete  # Toggle the `complete` status
    db.session.commit()  # Save changes to the database
    return redirect(url_for("index"))  # Redirect to the index page



@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()  # Find the to-do item by ID
    db.session.delete(todo)  # Delete the item
    db.session.commit()  # Save changes to the database
    return redirect(url_for("index"))  # Redirect to the index page




if __name__ == "__main__":
    # Ensure database tables are created within the app context
    with app.app_context():
        db.create_all()

    # Start the Flask application
    app.run(debug=True)
