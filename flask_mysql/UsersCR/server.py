from flask import Flask, render_template, request, redirect

from users import User

app=Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    return render_template("users.html",users=User.get_all())


@app.route('/user/new')
def new():
    return render_template("new_user.html")

@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    result = User.save(request.form)
    if result is not None:
        # User was successfully saved
        return redirect('/users')
    else:
        # User creation failed, maybe due to a duplicate email
        # You can add a flash message or handle the error as needed
        return redirect('/user/new')  # Redirect to the new user creation page with an error message
@app.route ("/user/delete/<int:id>")
def destroy (id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect ('/users')
@app.route('/user/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')
@app.route('/user/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit_user.html",user=User.get_by_id(data))

@app.route('/user/show/<int:id>')
def show(id):
    data = {"id": id}
    user = User.get_by_id(data)
    return render_template("show_user.html", user=user)

if __name__=="__main__":
    app.run(debug=True)