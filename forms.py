from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, EmailField
from wtforms.validators import DataRequired


class CodeForm(FlaskForm):
    checkbox = BooleanField('Decode')
    text = StringField('Text', validators=[DataRequired(),], render_kw={"style": "margin-bottom: 10px;"})
    submit = SubmitField('Submit', render_kw={"style": "margin-bottom: 40px;float-right"})
    Output: TextAreaField = TextAreaField('Output')