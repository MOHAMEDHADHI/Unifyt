from unifyt import Quantity

# TIME CONVERSIONS
print(Quantity('10 s', 'min'))
print(Quantity('5 min', 's'))
print(Quantity('2 h', 'min'))
print(Quantity('1 d', 'h'))

# LENGTH CONVERSIONS
print(Quantity('5 cm', 'm'))
print(Quantity('100 m', 'km'))
print(Quantity('12 in', 'cm'))
print(Quantity('3 ft', 'm'))
print(Quantity('1 mi', 'km'))

# MASS CONVERSIONS
print(Quantity('100 lb', 'kg'))
print(Quantity('1 kg', 'g'))
print(Quantity('16 oz', 'lb'))

# PRESSURE CONVERSIONS
print(Quantity('1 bar', 'Pa'))
print(Quantity('100 psi', 'bar'))
print(Quantity('1 atm', 'Pa'))
print(Quantity('1 kPa', 'Pa'))

# TEMPERATURE CONVERSIONS
print(Quantity('0 celsius', 'fahrenheit'))
print(Quantity('100 celsius', 'kelvin'))
print(Quantity('32 fahrenheit', 'celsius'))

# ENERGY CONVERSIONS
print(Quantity('1 kWh', 'J'))
print(Quantity('1000 J', 'kJ'))
print(Quantity('1 cal', 'J'))

# POWER CONVERSIONS
print(Quantity('1 kW', 'W'))
print(Quantity('1 hp', 'W'))
print(Quantity('5 kW', 'hp'))

# SPEED CONVERSIONS
print(Quantity('100 km/hr', 'm/s'))
print(Quantity('60 mi/hr', 'km/hr'))
print(Quantity('450 knot', 'km/hr'))

# FORCE CONVERSIONS
print(Quantity('1000 N', 'kN'))
print(Quantity('100 lbf', 'N'))

# TORQUE CONVERSIONS
print(Quantity('100 Nm', 'ft_lb'))
print(Quantity('50 ft_lb', 'Nm'))

# VOLTAGE CONVERSIONS
print(Quantity('1 kV', 'V'))
print(Quantity('230 V', 'kV'))

# VOLUME CONVERSIONS (LITERS AND GALLONS)
print(Quantity('1 L', 'gallon'))
print(Quantity('1 gallon', 'liter'))
print(Quantity('100 L', 'gallon'))

# FLOW RATE CONVERSIONS
print(Quantity('100 cfm', 'm3_min'))
print(Quantity('50 L_min', 'gpm'))

# ANGULAR VELOCITY CONVERSIONS
print(Quantity('60 revolution_per_minute', 'radian_per_second'))
print(Quantity('3000 revolution_per_minute', 'radian_per_second'))

# CUBIC METER CONVERSIONS (m3 and cubic_meter)
print(Quantity('1 m3', 'L'))
print(Quantity('1 cubic_meter', 'liter'))
print(Quantity('1000 L', 'm3'))
print(Quantity('1 m3', 'gallon'))
print(Quantity('5 cubic_meter', 'liter'))
print(Quantity('10 m3', 'gallon'))
print(Quantity('500 gallon', 'm3'))
print(Quantity('10 cubic_meter', 'gallon'))
