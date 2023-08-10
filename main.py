from flask import Flask, render_template, url_for
from jinja2 import Template

# шаблон

# name = "Света"
# tm = Template("Hi, {{name}}")
# msg = tm.render(name=name)
# print(msg)

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html')
    # return "Home page"


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "User: " + name + " - " + str(id)


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
