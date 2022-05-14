from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class TaskList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


@app.route("/")
def home():
    task_list = TaskList.query.all()
    return render_template("TL_base.html", task_list=task_list)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_task = TaskList(title=title, complete=False)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/update/<int:task_id>")
def update(task_id):
    task = TaskList.query.filter_by(id=task_id).first()
    task.complete = not task.complete
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/delete/<int:task_id>")
def delete(task_id):
    task = TaskList.query.filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
