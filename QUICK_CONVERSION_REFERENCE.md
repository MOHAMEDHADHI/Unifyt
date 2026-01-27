# Quick Conversion Reference Card

## One-Page Cheat Sheet for Unifyt Library

### Basic Syntax
```python
from unifyt import Quantity

# Create quantity
value = Quantity(100, 'meter')

# Convert
result = value.to('foot')
```

---

## Most Common Conversions

### Length
```python
Quantity(1, 'meter').to('foot')          # 3.281 ft
Quantity(1, 'kilometer').to('mile')      # 0.621 mi
Quantity(1, 'inch').to('centimeter')     # 2.54 cm
Quantity(1, 'foot').to('meter')          # 0.305 m
```

### Mass
```python
Quantity(1, 'kilogram').to('pound')      # 2.205 lb
Quantity(1, 'pound').to('kilogram')      # 0.454 kg
Quantity(1, 'ton').to('kilogram')        # 1000 kg
```

### Temperature
```python
Quantity(0, 'celsius').to('fahrenheit')  # 32 °F
Quantity(100, 'celsius').to('fahrenheit') # 212 °F
Quantity(25, 'celsius').to('kelvin')     # 298.15 K
```

### Pressure
```python
Quantity(1, 'bar').to('psi')             # 14.504 psi
Quantity(1, 'psi').to('kilopascal')      # 6.895 kPa
Quantity(1, 'atmosphere').to('pascal')   # 101,325 Pa
```

### Volume
```python
Quantity(1, 'liter').to('gallon')        # 0.264 gal
Quantity(1, 'gallon').to('liter')        # 3.785 L
Quantity(1, 'cubic_meter').to('liter')   # 1000 L
```

### Speed
```python
Quantity(100, 'kilometer/hour').to('mile/hour')  # 62.137 mph
Quantity(60, 'mile/hour').to('meter/second')     # 26.822 m/s
```

---

## New Units (v0.2.1)

### Wire Gauge
```python
from unifyt import wire_gauge

wire_gauge.awg_to_diameter(14)           # 1.628 mm
wire_gauge.diameter_to_awg(1.6, 'mm')    # 14
wire_gauge.swg_to_diameter(14)           # 2.032 mm
wire_gauge.bwg_to_diameter(14)           # 2.108 mm
```

### Torque
```python
Quantity(100, 'newton_meter').to('foot_pound')   # 73.76 ft-lb
Quantity(75, 'foot_pound').to('newton_meter')    # 101.69 Nm
Quantity(120, 'inch_pound').to('newton_meter')   # 13.56 Nm
```

### Flow Rate
```python
# Mass flow
Quantity(1000, 'kilogram_per_hour').to('kilogram_per_second')  # 0.278 kg/s
Quantity(1000, 'kilogram_per_hour').to('ton_per_hour')         # 1.0 tph

# Volumetric flow
Quantity(100, 'liter_per_minute').to('cubic_meter_per_hour')   # 6.0 m³/hr
Quantity(1000, 'cubic_foot_per_minute').to('liter_per_minute') # 28,317 lpm
```

### Angular Velocity
```python
Quantity(1800, 'revolution_per_minute').to('radian_per_second')  # 188.5 rad/s
Quantity(1800, 'revolution_per_minute').to('degree_per_second')  # 10,800 deg/s

# Frequency vs Angular Velocity
Quantity(1800, 'rpm').to('hertz')                                # 30 Hz (frequency)
Quantity(1800, 'revolution_per_minute').to('radian_per_second')  # 188.5 rad/s (angular)
```

### Paper Weight (GSM)
```python
# Direct calculation (GSM is simple unit)
gsm = 80
kg_m2 = gsm * 0.001                      # 0.080 kg/m²
lb_ft2 = kg_m2 * 0.2048                  # 0.0164 lb/ft²
oz_yd2 = gsm * 0.0295                    # 2.36 oz/yd²
```

---

## Unit Shortcuts

### Length
- `'m'` = meter
- `'cm'` = centimeter
- `'mm'` = millimeter
- `'km'` = kilometer
- `'in'` = inch
- `'ft'` = foot
- `'yd'` = yard
- `'mi'` = mile

### Mass
- `'g'` = gram
- `'kg'` = kilogram
- `'mg'` = milligram
- `'t'` = ton
- `'lb'` = pound
- `'oz'` = ounce

### Time
- `'s'` = second
- `'min'` = minute
- `'hr'` = hour
- `'d'` = day

### Pressure
- `'Pa'` = pascal
- `'kPa'` = kilopascal
- `'MPa'` = megapascal
- `'bar'` = bar
- `'psi'` = pound per square inch
- `'atm'` = atmosphere

### Energy/Power
- `'J'` = joule
- `'kJ'` = kilojoule
- `'MJ'` = megajoule
- `'W'` = watt
- `'kW'` = kilowatt
- `'MW'` = megawatt
- `'hp'` = horsepower

---

## Quick Formulas

### Compound Units
```python
# Velocity
v = Quantity(100, 'meter') / Quantity(10, 'second')  # 10 m/s

# Acceleration
a = Quantity(10, 'meter/second^2')

# Force
F = Quantity(10, 'kilogram') * a  # 100 N

# Pressure
P = F / Quantity(0.01, 'meter^2')  # 10,000 Pa

# Energy
E = F * Quantity(10, 'meter')  # 1000 J

# Power
P = E / Quantity(5, 'second')  # 200 W
```

---

## Interactive Converters

```bash
# Run interactive mode
python unit-convertions-examples/wire_gauge_converter.py --interactive
python unit-convertions-examples/torque_converter.py --interactive
python unit-convertions-examples/flow_rate_converter.py --interactive
python unit-convertions-examples/angular_velocity_converter.py --interactive
python unit-convertions-examples/paper_weight_converter.py --interactive
```

---

## Common Patterns

### Pattern 1: Simple Conversion
```python
result = Quantity(value, 'from_unit').to('to_unit')
```

### Pattern 2: Arithmetic
```python
total = Quantity(10, 'meter') + Quantity(5, 'meter')  # 15 m
diff = Quantity(10, 'meter') - Quantity(5, 'meter')   # 5 m
area = Quantity(10, 'meter') * Quantity(5, 'meter')   # 50 m²
ratio = Quantity(10, 'meter') / Quantity(5, 'meter')  # 2.0
```

### Pattern 3: Comparison
```python
Quantity(1, 'kilometer') == Quantity(1000, 'meter')   # True
Quantity(1, 'kilometer') > Quantity(500, 'meter')     # True
```

---

## Conversion Factors (Quick Reference)

### Length
- 1 m = 100 cm = 1000 mm
- 1 km = 1000 m
- 1 in = 2.54 cm
- 1 ft = 0.3048 m = 12 in
- 1 yd = 0.9144 m = 3 ft
- 1 mi = 1.609 km = 5280 ft

### Mass
- 1 kg = 1000 g = 1,000,000 mg
- 1 t = 1000 kg
- 1 lb = 0.4536 kg = 16 oz
- 1 oz = 28.35 g

### Volume
- 1 L = 1000 mL = 0.001 m³
- 1 gal = 3.785 L
- 1 m³ = 1000 L

### Pressure
- 1 bar = 100,000 Pa = 100 kPa
- 1 psi = 6.895 kPa
- 1 atm = 101.325 kPa = 1.013 bar

### Temperature
- °F = (°C × 9/5) + 32
- °C = (°F - 32) × 5/9
- K = °C + 273.15

### Energy
- 1 kJ = 1000 J
- 1 kWh = 3.6 MJ
- 1 BTU = 1.055 kJ

### Power
- 1 kW = 1000 W
- 1 hp = 745.7 W = 0.746 kW

---

## Troubleshooting

| Error | Solution |
|-------|----------|
| "incompatible dimensions" | Check units are compatible (e.g., can't convert m to s) |
| "Unknown unit" | Use lowercase, check spelling |
| GSM not converting | Use direct calculation: `gsm * 0.001 = kg/m²` |
| RPM confusion | Use 'rpm' for Hz, 'revolution_per_minute' for rad/s |

---

## Resources

- **Full Guide**: `final documents/CONVERSION_GUIDE.md`
- **API Docs**: `docs/api_reference.md`
- **Examples**: `examples/` directory
- **Converters**: `unit-convertions-examples/` directory
- **Units Catalog**: `final documents/UNITS_CATALOG.md`

---

**Print this page for quick reference!**

*Unifyt v0.2.1 - 300+ units supported*
