from flask import Flask, render_template
app = Flask(__name__)


# home route
@app.route("/")
def home():
    return render_template("home.html")

# Register route
@app.route("/register")
def register():
    return render_template("register.html")



if __name__=="__main__":
    app.run(debug=True)
