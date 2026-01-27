# Complete Conversion Guide - Unifyt Library

## Table of Contents
1. [Quick Start](#quick-start)
2. [Basic Conversions](#basic-conversions)
3. [Industry-Specific Conversions](#industry-specific-conversions)
4. [New Units (v0.2.1)](#new-units-v021)
5. [Interactive Converters](#interactive-converters)
6. [Advanced Usage](#advanced-usage)
7. [Common Patterns](#common-patterns)

---

## Quick Start

### Installation
```bash
pip install unifyt
```

### Basic Usage
```python
from unifyt import Quantity

# Create a quantity
distance = Quantity(100, 'meter')

# Convert to another unit
print(distance.to('kilometer'))  # 0.1 kilometer
print(distance.to('foot'))       # 328.084 foot
```

---

## Basic Conversions

### Length Conversions
```python
from unifyt import Quantity

# Metric
length = Quantity(1, 'meter')
print(length.to('millimeter'))   # 1000 mm
print(length.to('centimeter'))   # 100 cm
print(length.to('kilometer'))    # 0.001 km

# Imperial
print(length.to('inch'))         # 39.37 inch
print(length.to('foot'))         # 3.281 foot
print(length.to('yard'))         # 1.094 yard
print(length.to('mile'))         # 0.000621 mile
```

### Mass Conversions
```python
mass = Quantity(1, 'kilogram')
print(mass.to('gram'))           # 1000 g
print(mass.to('milligram'))      # 1,000,000 mg
print(mass.to('ton'))            # 0.001 ton

# Imperial
print(mass.to('pound'))          # 2.205 lb
print(mass.to('ounce'))          # 35.274 oz
```

### Temperature Conversions
```python
temp = Quantity(25, 'celsius')
print(temp.to('fahrenheit'))     # 77.0 °F
print(temp.to('kelvin'))         # 298.15 K

# Absolute zero
absolute = Quantity(0, 'kelvin')
print(absolute.to('celsius'))    # -273.15 °C
```

### Pressure Conversions
```python
pressure = Quantity(1, 'bar')
print(pressure.to('pascal'))     # 100,000 Pa
print(pressure.to('psi'))        # 14.504 psi
print(pressure.to('atmosphere')) # 0.987 atm
print(pressure.to('kilopascal')) # 100 kPa
print(pressure.to('megapascal')) # 0.1 MPa
```

### Volume Conversions
```python
volume = Quantity(1, 'liter')
print(volume.to('milliliter'))   # 1000 mL
print(volume.to('cubic_meter'))  # 0.001 m³
print(volume.to('gallon'))       # 0.264 gal
print(volume.to('quart'))        # 1.057 qt
print(volume.to('cup'))          # 4.227 cup
```

### Speed Conversions
```python
speed = Quantity(100, 'kilometer/hour')
print(speed.to('meter/second'))  # 27.778 m/s
print(speed.to('mile/hour'))     # 62.137 mph
print(speed.to('knot'))          # 53.996 knot
```

---

## Industry-Specific Conversions

### Aerospace Engineering
```python
# Altitude
altitude = Quantity(35000, 'foot')
print(altitude.to('meter'))      # 10,668 m

# Airspeed
airspeed = Quantity(450, 'knot')
print(airspeed.to('kilometer/hour'))  # 833.4 km/h
print(airspeed.to('meter/second'))    # 231.5 m/s

# Thrust
thrust = Quantity(50000, 'pound_force')
print(thrust.to('newton'))       # 222,411 N
print(thrust.to('kilonewton'))   # 222.4 kN
```

### Oil & Gas Industry
```python
# Volume
oil_volume = Quantity(1000, 'barrel')
print(oil_volume.to('liter'))    # 158,987 L
print(oil_volume.to('cubic_meter'))  # 158.987 m³

# Pressure
well_pressure = Quantity(5000, 'psi')
print(well_pressure.to('bar'))   # 344.74 bar
print(well_pressure.to('megapascal'))  # 34.47 MPa
```

### Civil Engineering
```python
# Stress/Strength
concrete_strength = Quantity(30, 'megapascal')
print(concrete_strength.to('psi'))  # 4,351 psi

# Load
load = Quantity(100, 'kilonewton')
print(load.to('pound_force'))    # 22,481 lbf
print(load.to('ton_force'))      # 10.197 tonf

# Volume (earthwork)
excavation = Quantity(1000, 'cubic_meter')
print(excavation.to('cubic_yard'))  # 1,308 yd³
```

### Electrical Engineering
```python
# Power
power = Quantity(1000, 'watt')
print(power.to('kilowatt'))      # 1 kW
print(power.to('horsepower'))    # 1.341 hp

# Energy
energy = Quantity(100, 'kilowatt_hour')
print(energy.to('joule'))        # 360,000,000 J
print(energy.to('megajoule'))    # 360 MJ

# Voltage
voltage = Quantity(11, 'kilovolt')
print(voltage.to('volt'))        # 11,000 V
```

### HVAC Engineering
```python
# Cooling capacity (tons of refrigeration)
cooling = Quantity(5, 'ton_refrigeration')
print(cooling.to('kilowatt'))    # 17.58 kW
print(cooling.to('btu/hour'))    # 60,000 BTU/hr

# Air flow
airflow = Quantity(1000, 'cubic_foot/minute')
print(airflow.to('cubic_meter/hour'))  # 1,699 m³/hr
print(airflow.to('liter/second'))      # 471.9 L/s
```

---

## New Units (v0.2.1)

### Wire Gauge Conversions
```python
from unifyt import wire_gauge

# AWG to diameter
diameter = wire_gauge.awg_to_diameter(14)
print(diameter)  # 1.628 millimeter
print(diameter.to('inch'))  # 0.0641 inch

# Diameter to AWG
gauge = wire_gauge.diameter_to_awg(1.6, 'mm')
print(f"AWG {gauge}")  # AWG 14

# SWG (Standard Wire Gauge)
swg_diameter = wire_gauge.swg_to_diameter(14)
print(swg_diameter)  # 2.032 millimeter

# BWG (Birmingham Wire Gauge)
bwg_diameter = wire_gauge.bwg_to_diameter(14)
print(bwg_diameter)  # 2.108 millimeter

# Compare standards
print(f"AWG 14: {wire_gauge.awg_to_diameter(14)}")
print(f"SWG 14: {wire_gauge.swg_to_diameter(14)}")
print(f"BWG 14: {wire_gauge.bwg_to_diameter(14)}")
```

### Torque Conversions
```python
# Engine torque
engine_torque = Quantity(200, 'newton_meter')
print(engine_torque.to('foot_pound'))  # 147.51 ft-lb
print(engine_torque.to('kilonewton_meter'))  # 0.2 kNm

# Wheel lug nuts
lug_torque = Quantity(100, 'foot_pound')
print(lug_torque.to('newton_meter'))  # 135.58 Nm

# Small fasteners
fastener = Quantity(120, 'inch_pound')
print(fastener.to('newton_meter'))  # 13.56 Nm
print(fastener.to('foot_pound'))    # 10.0 ft-lb
```

### Flow Rate Conversions
```python
# Mass flow
mass_flow = Quantity(1000, 'kilogram_per_hour')
print(mass_flow.to('kilogram_per_second'))  # 0.278 kg/s
print(mass_flow.to('kilogram_per_minute'))  # 16.67 kg/min
print(mass_flow.to('ton_per_hour'))         # 1.0 tph
print(mass_flow.to('pound_per_hour'))       # 2,205 lb/hr

# Volumetric flow
vol_flow = Quantity(100, 'liter_per_minute')
print(vol_flow.to('cubic_meter_per_hour'))  # 6.0 m³/hr
print(vol_flow.to('liter_per_second'))      # 1.67 L/s
print(vol_flow.to('gallon_per_minute'))     # 26.42 gpm

# HVAC air flow
airflow = Quantity(1000, 'cubic_foot_per_minute')
print(airflow.to('cubic_meter_per_hour'))   # 1,699 m³/hr
print(airflow.to('liter_per_minute'))       # 28,317 lpm
```

### Angular Velocity Conversions
```python
# Motor speed
motor_speed = Quantity(1800, 'revolution_per_minute')
print(motor_speed.to('radian_per_second'))  # 188.50 rad/s
print(motor_speed.to('degree_per_second'))  # 10,800 deg/s
print(motor_speed.to('revolution_per_second'))  # 30.0 rps

# IMPORTANT: RPM vs revolution_per_minute
# Use 'rpm' for frequency (Hz)
freq = Quantity(1800, 'rpm')
print(freq.to('hertz'))  # 30.0 Hz

# Use 'revolution_per_minute' for angular velocity (rad/s)
ang_vel = Quantity(1800, 'revolution_per_minute')
print(ang_vel.to('radian_per_second'))  # 188.50 rad/s
```

### Paper Weight (GSM) Conversions
```python
# GSM = grams per square meter
# Note: GSM is a simple unit, use direct calculation

# Copy paper
gsm = 80
kg_m2 = gsm * 0.001  # 0.080 kg/m²
lb_ft2 = kg_m2 * 0.2048  # 0.0164 lb/ft²
oz_yd2 = gsm * 0.0295  # 2.36 oz/yd²

print(f"{gsm} GSM = {kg_m2} kg/m²")
print(f"{gsm} GSM = {lb_ft2:.4f} lb/ft²")
print(f"{gsm} GSM = {oz_yd2:.2f} oz/yd²")

# Calculate paper ream weight
a4_area = 0.210 * 0.297  # m²
sheets = 500
weight_per_sheet_kg = (gsm * a4_area) / 1000.0
total_weight_kg = weight_per_sheet_kg * sheets
print(f"500 sheets of {gsm} GSM A4: {total_weight_kg:.2f} kg")
```

---

## Interactive Converters

### Using Interactive Mode
All new converters support interactive mode for easy exploration:

```bash
# Wire gauge converter
python unit-convertions-examples/wire_gauge_converter.py --interactive

# Torque converter
python unit-convertions-examples/torque_converter.py --interactive

# Flow rate converter
python unit-convertions-examples/flow_rate_converter.py --interactive

# Angular velocity converter
python unit-convertions-examples/angular_velocity_converter.py --interactive

# Paper weight converter
python unit-convertions-examples/paper_weight_converter.py --interactive
```

### Running Demonstrations
See comprehensive examples by running without flags:

```bash
python unit-convertions-examples/wire_gauge_converter.py
python unit-convertions-examples/torque_converter.py
python unit-convertions-examples/flow_rate_converter.py
python unit-convertions-examples/angular_velocity_converter.py
python unit-convertions-examples/paper_weight_converter.py
```

---

## Advanced Usage

### Compound Units
```python
# Velocity
velocity = Quantity(10, 'meter') / Quantity(1, 'second')
print(velocity)  # 10.0 meter / second

# Acceleration
accel = Quantity(9.81, 'meter/second^2')
print(accel)  # 9.81 meter/second^2

# Force (mass × acceleration)
mass = Quantity(10, 'kilogram')
force = mass * accel
print(force)  # 98.1 kilogram * meter / second^2.0
print(force.to('newton'))  # 98.1 N

# Pressure (force / area)
area = Quantity(0.01, 'meter^2')
pressure = force / area
print(pressure)  # 9810 kilogram / meter / second^2.0
print(pressure.to('pascal'))  # 9810 Pa
```

### Energy and Power
```python
# Work = Force × Distance
force = Quantity(100, 'newton')
distance = Quantity(10, 'meter')
work = force * distance
print(work.to('joule'))  # 1000 J

# Power = Work / Time
time = Quantity(5, 'second')
power = work / time
print(power.to('watt'))  # 200 W

# Power from torque and angular velocity
torque = Quantity(100, 'newton_meter')
angular_vel = Quantity(1800, 'revolution_per_minute')
omega = angular_vel.to('radian_per_second')
power_watts = torque.magnitude * omega.magnitude
print(f"Power: {power_watts:.1f} W")  # 18,850 W
```

### Density and Specific Gravity
```python
# Density
mass = Quantity(1000, 'kilogram')
volume = Quantity(1, 'cubic_meter')
density = mass / volume
print(density)  # 1000 kg/m³

# Convert to other units
print(density.to('gram/liter'))  # 1000 g/L
print(density.to('pound/cubic_foot'))  # 62.43 lb/ft³
```

### Flow Calculations
```python
# Volumetric flow = velocity × area
velocity = Quantity(2, 'meter/second')
pipe_diameter = Quantity(0.1, 'meter')
pipe_area = 3.14159 * (pipe_diameter.magnitude / 2) ** 2
area = Quantity(pipe_area, 'meter^2')
flow = velocity * area
print(flow.to('liter/second'))  # 15.71 L/s

# Mass flow = density × volumetric flow
water_density = Quantity(1000, 'kilogram/cubic_meter')
mass_flow = water_density * flow
print(mass_flow.to('kilogram/second'))  # 15.71 kg/s
```

---

## Common Patterns

### Pattern 1: Unit Conversion Chain
```python
# Convert through multiple units
distance = Quantity(1, 'mile')
print(distance.to('kilometer'))  # 1.609 km
print(distance.to('meter'))      # 1,609 m
print(distance.to('foot'))       # 5,280 ft
print(distance.to('inch'))       # 63,360 in
```

### Pattern 2: Arithmetic Operations
```python
# Addition (same dimensions)
d1 = Quantity(100, 'meter')
d2 = Quantity(50, 'meter')
total = d1 + d2
print(total)  # 150 meter

# Subtraction
diff = d1 - d2
print(diff)  # 50 meter

# Multiplication
area = d1 * d2
print(area)  # 5000 meter^2

# Division
ratio = d1 / d2
print(ratio)  # 2.0
```

### Pattern 3: Comparison
```python
# Compare quantities
d1 = Quantity(1, 'kilometer')
d2 = Quantity(1000, 'meter')
print(d1 == d2)  # True (same value, compatible units)

d3 = Quantity(1, 'mile')
print(d1 < d3)  # True (1 km < 1 mile)
```

### Pattern 4: Batch Conversions
```python
# Convert multiple values
values = [10, 20, 30, 40, 50]
unit = 'meter'
target = 'foot'

for value in values:
    q = Quantity(value, unit)
    print(f"{value} {unit} = {q.to(target)}")
```

### Pattern 5: Using Constants
```python
from unifyt import constants

# Speed of light
print(constants.c)  # 299,792,458 m/s

# Gravitational constant
print(constants.G)  # 6.674e-11 m³/(kg·s²)

# Planck constant
print(constants.h)  # 6.626e-34 J·s

# Avogadro constant
print(constants.N_A)  # 6.022e23 1/mol
```

---

## Quick Reference Tables

### Length
| Unit | Symbol | Conversion to Meter |
|------|--------|---------------------|
| Millimeter | mm | 0.001 |
| Centimeter | cm | 0.01 |
| Meter | m | 1 |
| Kilometer | km | 1000 |
| Inch | in | 0.0254 |
| Foot | ft | 0.3048 |
| Yard | yd | 0.9144 |
| Mile | mi | 1609.34 |

### Mass
| Unit | Symbol | Conversion to Kilogram |
|------|--------|------------------------|
| Milligram | mg | 0.000001 |
| Gram | g | 0.001 |
| Kilogram | kg | 1 |
| Ton | t | 1000 |
| Ounce | oz | 0.0283495 |
| Pound | lb | 0.453592 |

### Pressure
| Unit | Symbol | Conversion to Pascal |
|------|--------|----------------------|
| Pascal | Pa | 1 |
| Kilopascal | kPa | 1000 |
| Megapascal | MPa | 1,000,000 |
| Bar | bar | 100,000 |
| PSI | psi | 6894.76 |
| Atmosphere | atm | 101,325 |

### Temperature
| Unit | Symbol | Formula |
|------|--------|---------|
| Celsius | °C | Base |
| Fahrenheit | °F | (°C × 9/5) + 32 |
| Kelvin | K | °C + 273.15 |

---

## Tips and Best Practices

### 1. Always Specify Units
```python
# Good
distance = Quantity(100, 'meter')

# Bad - ambiguous
distance = 100  # What unit?
```

### 2. Convert Early
```python
# Convert to working units at the start
input_value = Quantity(100, 'foot')
working_value = input_value.to('meter')
# Now work with meters throughout
```

### 3. Check Dimensionality
```python
# Unifyt will catch incompatible conversions
try:
    distance = Quantity(100, 'meter')
    time = distance.to('second')  # Error!
except ValueError as e:
    print(f"Cannot convert: {e}")
```

### 4. Use Compound Units
```python
# Instead of calculating manually
speed = Quantity(100, 'kilometer/hour')
# Not: speed = 100 / 3.6  # m/s
```

### 5. Leverage Constants
```python
from unifyt import constants

# Use built-in physical constants
gravity = constants.g  # 9.80665 m/s²
```

---

## Troubleshooting

### Common Issues

**Issue: "Cannot convert from X to Y: incompatible dimensions"**
- Solution: Check that units have compatible dimensions
- Example: Can't convert meters to seconds

**Issue: "Unknown unit: xyz"**
- Solution: Check spelling and use lowercase
- Example: Use 'meter' not 'Meter' or 'METER'

**Issue: GSM conversions not working**
- Solution: GSM is a simple unit, use direct calculation
- Example: `kg_m2 = gsm * 0.001`

**Issue: RPM confusion**
- Solution: Use 'rpm' for frequency, 'revolution_per_minute' for angular velocity
- See: `docs/RPM_CLARIFICATION.md`

---

## Additional Resources

### Documentation
- **API Reference**: `docs/api_reference.md`
- **User Guide**: `docs/user_guide.md`
- **New Units**: `docs/NEW_UNITS_v0.2.1.md`
- **Units Catalog**: `final documents/UNITS_CATALOG.md`

### Examples
- **Basic Usage**: `examples/basic_usage.py`
- **Advanced Features**: `examples/advanced_features.py`
- **New Units Demo**: `examples/new_units_demo.py`
- **Industry Examples**: `unit-convertions-examples/`

### Converters
- **Wire Gauge**: `unit-convertions-examples/wire_gauge_converter.py`
- **Torque**: `unit-convertions-examples/torque_converter.py`
- **Flow Rate**: `unit-convertions-examples/flow_rate_converter.py`
- **Angular Velocity**: `unit-convertions-examples/angular_velocity_converter.py`
- **Paper Weight**: `unit-convertions-examples/paper_weight_converter.py`

---

## Support

For questions or issues:
1. Check this guide
2. Review the documentation in `docs/`
3. See examples in `examples/`
4. Try interactive converters
5. Refer to the units catalog

---

**Version:** 0.2.1  
**Last Updated:** 2025-01-27  
**Author:** Unifyt Team

---

*This guide covers all conversions available in Unifyt v0.2.1, including 300+ units across all physical dimensions.*
