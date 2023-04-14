from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL
from user_model import User

app = Flask(__name__)

app.secret_key = "poggers"


@app.route('/')
def form_main():
    
    people = User.get_all()
    print(people)
    
    return render_template("read.html", people=people)




@app.route('/add', methods=['POST'])
def add_user ():
    
    User.create(request.form)
    return redirect('/')


@app.route('/create')
def result_form():
    return render_template("create.html")


@app.route('/reset_session')
def reset():
    session.clear()
    return redirect('/')








if __name__ == "__main__":
    app.run(debug=True)