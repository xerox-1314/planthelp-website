from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def welcome():
    return render_template('main_window.html')


@app.route('/define')
def define():
    return render_template('define_window.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)