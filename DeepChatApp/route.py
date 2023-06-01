from flask import render_template, redirect, request
from DeepChatApp import app
from DeepChatApp.models import User, Todo


@app.route('/landingP')
def landingP():
	return render_template("landP.html")
@app.route('/login')
def login():
	return render_template("login.html")

@app.route('/registeration')
def registeration():
	return render_template("registeration.html")
	
@app.route('/', methods=["GET", "POST"])
def Home():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error while adding the task'

   else:
        tasks = Todo.query.all()
        return render_template("index.html", tasks=task)

@app.route('/about')
def about():
	return render_template("about.html")
