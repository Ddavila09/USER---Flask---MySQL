from flask import  render_template, request, redirect, session

from flask_app.models.user_model import User


from flask_app import app

app.secret_key = "poggers"



@app.route('/')
def form_main():
    
    people = User.get_all()
    print(people)
    
    return render_template("read.html", people=people)




@app.route('/add', methods=['POST'])
def add_user():
    user_id = User.create(request.form)
    return redirect(f'/show_user/{user_id}')



@app.route('/create')
def result_form():
    return render_template("create.html")

@app.route('/show_user/<int:id>')
def show_user(id):
    user = User.get_one(id)
    return render_template('show_user.html', user=user)


@app.route('/edit_user/<int:id>')
def edit_user(id):
    # print(id)
    User.get_one(id)
    return render_template('edit_user.html', user=User.get_one(id))


@app.route('/save_user', methods=['POST'])
def save_user():
    User.save(request.form)
    return redirect('/')


@app.route('/delete_user/<int:id>')
def delete(id):
    
    User.delete(id)
    
    return redirect('/')












@app.route('/reset_session')
def reset():
    session.clear()
    return redirect('/')
