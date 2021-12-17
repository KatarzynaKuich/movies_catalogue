from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    movies = ['tytul filmu1','tytul filmu2','tytul filmu3','tytul filmu4','tytul filmu5']
    return render_template("homepage.html", movies=movies)


if __name__ == '__main__':
    app.run(debug=True)
