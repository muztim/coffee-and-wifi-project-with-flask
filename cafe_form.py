from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
from flask_wtf import FlaskForm


class CafeFrom(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired(message='Cafe name required')])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open = StringField('Opening time e.g. 8AM', validators=[DataRequired()])
    close = StringField('Closing time e.g. 9PM', validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
                                validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Strength Rating", choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
                              validators=[DataRequired()])
    power_rating = SelectField('Power Socket Availability', choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌",
                                                                     "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('submit')