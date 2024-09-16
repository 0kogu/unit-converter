from flask_wtf import FlaskForm
from wtforms import FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired

class UnitConverterForm(FlaskForm):
    category = SelectField('Category', choices=[('length', 'Length'), ('temperature', 'Temperature'), ('weight', 'Weight')], validators=[DataRequired()])
    value = FloatField('Value', validators=[DataRequired()])
    from_unit = SelectField('From Unit', choices=[('meters', 'Meters'), ('feet','Feet')], validators=[DataRequired()])
    to_unit = SelectField('To Unit', choices=[('meters', 'Meters'), ('feet','Feet'), ('celsius', 'Celsius'), ('fahrenheit', 'Fahrenheit'), ('kilograms', 'Kilograms'), ('pounds', 'Pounds')], validators=[DataRequired()])
    submit = SubmitField('Convert')


