from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class CafeFrom(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired(message='Cafe name required')])
    submit = SubmitField('submit')