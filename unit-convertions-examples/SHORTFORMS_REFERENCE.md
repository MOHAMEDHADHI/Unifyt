# Short Forms Reference for Unifyt

## Quick Copy-Paste Examples

Copy these lines directly into your test.py file to test any conversion:

## TIME
```python
print(Quantity('10 s', 'min'))          # seconds to minutes
print(Quantity('5 min', 's'))           # minutes to seconds
print(Quantity('2 h', 'min'))           # hours to minutes
print(Quantity('1 d', 'h'))             # days to hours
print(Quantity('1 week', 'd'))          # weeks to days
```

## LENGTH
```python
print(Quantity('5 cm', 'm'))            # centimeters to meters
print(Quantity('100 m', 'km'))          # meters to kilometers
print(Quantity('12 in', 'cm'))          # inches to centimeters
print(Quantity('3 ft', 'm'))            # feet to meters
print(Quantity('1 mi', 'km'))           # miles to kilometers
print(Quantity('1 yd', 'm'))            # yards to meters
print(Quantity('1 nautical_mile', 'km')) # nautical miles to km
```

## MASS
```python
print(Quantity('100 lb', 'kg'))         # pounds to kilograms
print(Quantity('1 kg', 'g'))            # kilograms to grams
print(Quantity('16 oz', 'lb'))          # ounces to pounds
print(Quantity('1 ton', 'kg'))          # tons to kilograms
```

## PRESSURE
```python
print(Quantity('1 bar', 'Pa'))          # bar to pascals
print(Quantity('100 psi', 'bar'))       # psi to bar
print(Quantity('1 atm', 'Pa'))          # atmosphere to pascals
print(Quantity('1 kPa', 'Pa'))          # kilopascals to pascals
print(Quantity('1 MPa', 'bar'))         # megapascals to bar
print(Quantity('760 torr', 'atm'))      # torr to atmosphere
```

## TEMPERATURE
```python
print(Quantity('0 celsius', 'fahrenheit'))    # C to F
print(Quantity('100 celsius', 'kelvin'))      # C to K
print(Quantity('32 fahrenheit', 'celsius'))   # F to C
print(Quantity('273.15 kelvin', 'celsius'))   # K to C
```

## ENERGY
```python
print(Quantity('1 kWh', 'J'))           # kilowatt-hours to joules
print(Quantity('1000 J', 'kJ'))         # joules to kilojoules
print(Quantity('1 cal', 'J'))           # calories to joules
print(Quantity('1 BTU', 'J'))           # BTU to joules
```

## POWER
```python
print(Quantity('1 kW', 'W'))            # kilowatts to watts
print(Quantity('1 hp', 'W'))            # horsepower to watts
print(Quantity('5 kW', 'hp'))           # kilowatts to horsepower
print(Quantity('1000 W', 'kW'))         # watts to kilowatts
```

## SPEED
```python
print(Quantity('100 km/hr', 'm/s'))     # km/h to m/s
print(Quantity('60 mi/hr', 'km/hr'))    # mph to km/h
print(Quantity('450 knot', 'km/hr'))    # knots to km/h
print(Quantity('10 m/s', 'km/hr'))      # m/s to km/h
```

## FORCE
```python
print(Quantity('1000 N', 'kN'))         # newtons to kilonewtons
print(Quantity('100 lbf', 'N'))         # pound-force to newtons
print(Quantity('1 MN', 'N'))            # meganewtons to newtons
```

## TORQUE
```python
print(Quantity('100 Nm', 'ft_lb'))      # newton-meters to foot-pounds
print(Quantity('50 ft_lb', 'Nm'))       # foot-pounds to newton-meters
```

## VOLTAGE
```python
print(Quantity('1 kV', 'V'))            # kilovolts to volts
print(Quantity('230 V', 'kV'))          # volts to kilovolts
print(Quantity('11 kV', 'V'))           # kilovolts to volts
```

## VOLUME
```python
print(Quantity('1 L', 'm3'))            # liters to cubic meters
print(Quantity('1 gallon', 'liter'))    # gallons to liters
print(Quantity('1000 L', 'm3'))         # liters to cubic meters
print(Quantity('1 m3', 'L'))            # cubic meters to liters
```

## FLOW RATE
```python
print(Quantity('100 cfm', 'm3_min'))    # CFM to m³/min
print(Quantity('50 L_min', 'gpm'))      # L/min to GPM
print(Quantity('100 gpm', 'L_min'))     # GPM to L/min
```

## ANGULAR VELOCITY
```python
print(Quantity('60 revolution_per_minute', 'radian_per_second'))   # RPM to rad/s
print(Quantity('3000 revolution_per_minute', 'radian_per_second')) # RPM to rad/s
print(Quantity('1 radian_per_second', 'degree_per_second'))        # rad/s to deg/s
```

## AREA
```python
print(Quantity('1 meter^2', 'foot^2'))  # square meters to square feet
print(Quantity('100 foot^2', 'meter^2')) # square feet to square meters
```

## COMPOUND UNITS
```python
print(Quantity('1.225 kg/m^3', 'kg/m^3'))  # density
print(Quantity('9.8 m/s^2', 'm/s^2'))      # acceleration
```

---

## All Available Short Forms

### Time
- `s`, `sec` = second
- `min` = minute
- `h`, `hr` = hour
- `d` = day
- `week` = week
- `year`, `yr` = year

### Length
- `m` = meter
- `km` = kilometer
- `cm` = centimeter
- `mm` = millimeter
- `ft` = foot
- `in` = inch
- `mi` = mile
- `yd` = yard
- `nautical_mile`, `nmi` = nautical mile

### Mass
- `kg` = kilogram
- `g` = gram
- `lb` = pound
- `oz` = ounce
- `ton` = ton

### Pressure
- `Pa` = pascal
- `kPa` = kilopascal
- `MPa` = megapascal
- `bar` = bar
- `psi`, `PSI` = pounds per square inch
- `atm` = atmosphere
- `torr` = torr

### Temperature
- `celsius`, `degC` = Celsius
- `fahrenheit`, `degF` = Fahrenheit
- `kelvin`, `K` = Kelvin

### Energy
- `J` = joule
- `kJ` = kilojoule
- `kWh` = kilowatt-hour
- `cal` = calorie
- `kcal` = kilocalorie
- `BTU`, `btu` = British thermal unit

### Power
- `W` = watt
- `kW` = kilowatt
- `MW` = megawatt
- `hp` = horsepower

### Speed
- `m/s` = meters per second
- `km/hr` = kilometers per hour
- `mi/hr` = miles per hour
- `knot` = knot
- `ft/s` = feet per second

### Force
- `N` = newton
- `kN` = kilonewton
- `MN` = meganewton
- `lbf` = pound-force

### Torque
- `Nm`, `N_m` = newton-meter
- `ft_lb`, `foot_pound` = foot-pound

### Voltage
- `V` = volt
- `kV` = kilovolt
- `mV` = millivolt

### Volume
- `L` = liter
- `m3`, `m^3` = cubic meter
- `gallon`, `gal` = gallon
- `liter` = liter

### Flow Rate
- `cfm` = cubic feet per minute
- `m3_min` = cubic meters per minute
- `L_min` = liters per minute
- `gpm` = gallons per minute

### Angular Velocity
- `revolution_per_minute` = RPM
- `radian_per_second` = rad/s
- `degree_per_second` = deg/s
- `rad_s` = rad/s
- `deg_s` = deg/s

---

## Usage Pattern

```python
from unifyt import Quantity

# Basic pattern:
print(Quantity('VALUE UNIT', 'TARGET_UNIT'))

# Examples:
print(Quantity('10 s', 'min'))
print(Quantity('100 psi', 'bar'))
print(Quantity('60 mi/hr', 'km/hr'))
```

## Important Notes

1. **Use `min` for minute, NOT `m`** - `m` means meter!
2. **Temperature**: Use full names (`celsius`, `fahrenheit`, `kelvin`)
3. **Compound units**: Use `/` for division, `^` for powers
4. **Spaces**: Can use spaces between value and unit

## Quick Test Template

```python
from unifyt import Quantity

# Copy any line from above and paste here to test
print(Quantity('YOUR_VALUE YOUR_UNIT', 'TARGET_UNIT'))
```
