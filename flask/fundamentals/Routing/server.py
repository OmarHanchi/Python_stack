from flask import Flask , render_template
app= Flask(__name__)
@app.errorhandler(404)
def not_found():
    return render_template("error.html")
@app.route ("/")
def index () : 
    return ("Hello World !")
@app.route ("/Dojo")
def dojo ():
    return ("Dojo!")
@app.route ("/hi/<name>")
def hi_name (name):
    return f"Hi {name.capitalize()} !"
@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ''
    for i in range(0,num):
        output += f"<p>{word}</p>"
    return output
if __name__ == "__main__":
    app.run(debug=True)


