# app.py

from flask import Flask, render_template,redirect ,session, request

app = Flask(__name__)

@app.route("/")
def index():
  """This function renders the index.html template and displays the number of times the client has visited this site."""

  # Get the number of times the client has visited this site.
  count = session.get("count", 0)

  # Return the template.
  return render_template("index.html", count=count)

@app.route("/increment", methods=["POST"])
def increment():
  """This function increments the counter by the specified amount and redirects to the root route."""

  # Get the increment amount from the form.
  increment = int(request.form["increment"])

  # Get the number of times the client has visited this site.
  count = session.get("count", 0)

  # Increment the counter.
  count += increment

  # Store the counter in the session.
  session["count"] = count

  # Redirect to the root route.
  return redirect("/")
@app.route("/destroy_session")
def destroy_session():
  """This function clears the session and redirects to the root route."""

  # Clear the session.
  session.clear()

  # Redirect to the root route.
  return redirect("/")
if __name__ == "__main__":
  app.secret_key = "my_secret_key"
  app.run(debug=True)
