from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class CreatePlayerForm(FlaskForm):
    nick1 = StringField('Nick1', validators=[DataRequired(), Length(min=4, max=10)], render_kw={"placeholder": "gracz_nr1"})
    nick2 = StringField('Nick2', validators=[DataRequired(), Length(min=4, max=10)], render_kw={"placeholder": "gracz_nr2"})

    submit = SubmitField('Stwórz graczy')




