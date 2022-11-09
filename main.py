from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from cafe_form import CafeFrom
import csv

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add')
def add_cafe():
    form = CafeFrom()
    if form.validate_on_submit():
        print("True")
    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
