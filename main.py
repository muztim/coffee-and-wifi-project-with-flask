from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from cafe_form import CafeFrom
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
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


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    render_template('cafes.html', cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
