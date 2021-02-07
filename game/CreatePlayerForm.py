from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class CreatePlayerForm(FlaskForm):
    nick1 = StringField('Nick1', validators=[DataRequired(), Length(min=4, max=10)])
    nick2 = StringField('Nick2', validators=[DataRequired(), Length(min=4, max=10)])

    submit = SubmitField('Stwórz graczy')




