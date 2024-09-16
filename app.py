from flask import Flask, render_template, request
from forms import UnitConverterForm
from unit_converter import convert_units

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ea58e702abed259962ce9360603b482c'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UnitConverterForm()
    conversion_result = None  # Initialize conversion result

    if form.validate_on_submit():
        print("Form submitted and validated!")  # Debugging

        category = form.category.data
        value = form.value.data
        from_unit = form.from_unit.data
        to_unit = form.to_unit.data

        print(f"Category: {category}, Value: {value}, From: {from_unit}, To: {to_unit}")  # Debugging

        # Perform the unit conversion
        conversion_result = convert_units(category, value, from_unit, to_unit)
        print(f"Conversion Result: {conversion_result}")  # Debugging
    else:
        print(form.errors)  # This will print validation errors if any

    # Render the template with the form and result
    return render_template('index.html', form=form, conversion_result=conversion_result)


if __name__ == '__main__':
    app.run(debug=True)
