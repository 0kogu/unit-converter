def convert_units(category, value, from_unit, to_unit):
    if category == 'length':
        return convert_length(value, from_unit, to_unit)
    elif category == 'temperature':
        return convert_temperature(value, from_unit, to_unit)
    elif category == 'weight':
        return convert_weight(value, from_unit, to_unit)
    return None

# Length Conversion
def convert_length(value, from_unit, to_unit):
    length_units = {'meters': 1, 'feet': 3.28084}
    return value * length_units[to_unit] / length_units[from_unit]

# Temperature Conversion
def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return value * 9/5 + 32
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (value - 32) * 5/9
    return value

# Weight Conversion
def convert_weight(value, from_unit, to_unit):
    weight_units = {'kg': 1, 'lbs': 2.20462}
    return value * weight_units[to_unit] / weight_units[from_unit]
