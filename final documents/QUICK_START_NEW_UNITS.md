# Quick Start - New Units in Unifyt

## 🚀 5-Minute Guide to New Features

### 1. Wire Gauges (AWG, SWG, BWG)

```python
from unifyt import wire_gauge, Quantity

# Convert gauge to diameter
diameter = wire_gauge.awg_to_diameter(14)
print(diameter)  # 1.628 millimeter

# Convert to inches
diameter_in = wire_gauge.awg_to_diameter(14, 'inch')
print(diameter_in)  # 0.0641 inch

# Find gauge from diameter
gauge = wire_gauge.diameter_to_awg(Quantity(1.6, 'mm'))
print(gauge)  # 14

# Other standards
swg_dia = wire_gauge.swg_to_diameter(14)  # 2.032 mm
bwg_dia = wire_gauge.bwg_to_diameter(14)  # 2.108 mm
```

### 2. Torque Units

```python
from unifyt import Quantity

# Newton-meter (SI)
torque = Quantity(100, 'Nm')  # or 'newton_meter'
print(torque.to('foot_pound'))  # 73.76 ft-lb

# Foot-pound (Imperial)
bolt_torque = Quantity(75, 'ft_lb')  # or 'foot_pound'
print(bolt_torque.to('Nm'))  # 101.69 Nm

# Inch-pound (small fasteners)
screw_torque = Quantity(120, 'in_lb')  # or 'inch_pound'
print(screw_torque.to('Nm'))  # 13.56 Nm
```

### 3. Mass Flow Rates

```python
# Kilogram per hour
flow = Quantity(1000, 'kg_hr')  # or 'kilogram_per_hour'
print(flow.to('kilogram_per_second'))  # 0.278 kg/s

# Ton per hour (industrial)
material_flow = Quantity(5, 'tph')  # or 'ton_per_hour'
print(material_flow.to('kg_hr'))  # 5000 kg/hr
```

### 4. Volumetric Flow Rates

```python
# Cubic feet per minute (HVAC)
air_flow = Quantity(500, 'cfm')  # or 'cubic_foot_per_minute'
print(air_flow.to('cubic_meter_per_hour'))  # 849.5 m³/h

# Liters per minute
pump_flow = Quantity(100, 'lpm')  # or 'liter_per_minute'
print(pump_flow.to('gallon_per_minute'))  # 26.4 gpm
```

### 5. Angular Velocity

```python
# Revolution per minute (rotational speed)
motor_speed = Quantity(1800, 'revolution_per_minute')  # or 'rev_min'
print(motor_speed.to('radian_per_second'))  # 188.5 rad/s

# Note: Use 'rpm' for frequency (Hz), not angular velocity!
# For rotation, use 'revolution_per_minute'
```

### 6. Paper Weight (GSM)

```python
# Grams per square meter
paper = Quantity(80, 'gsm')  # or 'grams_per_square_meter'
print(paper.to('kilogram/meter^2'))  # 0.08 kg/m²
```

---

## 📋 Common Conversions

### Length
```python
Quantity(100, 'mm').to('inch')  # 3.94 in
Quantity(10, 'ft').to('meter')  # 3.05 m
```

### Pressure
```python
Quantity(5, 'bar').to('psi')  # 72.5 psi
Quantity(100, 'kPa').to('bar')  # 1.0 bar
```

### Torque
```python
Quantity(100, 'Nm').to('ft_lb')  # 73.76 ft-lb
Quantity(50, 'ft_lb').to('Nm')  # 67.79 Nm
```

### Flow Rates
```python
Quantity(1000, 'kg_hr').to('kg_s')  # 0.278 kg/s
Quantity(500, 'cfm').to('m3_h')  # 849.5 m³/h
Quantity(100, 'lpm').to('gpm')  # 26.4 gpm
```

### Angular Velocity
```python
Quantity(1800, 'revolution_per_minute').to('radian_per_second')  # 188.5 rad/s
Quantity(30, 'revolution_per_second').to('rpm')  # 1800 rpm (frequency)
```

---

## ⚠️ Important Notes

### 1. Use Lowercase
```python
# ✅ Correct
Quantity(100, 'mm')
Quantity(5, 'bar')

# ❌ Wrong
Quantity(100, 'MM')  # Won't work!
```

### 2. RPM Ambiguity
```python
# For rotational speed (rad/s)
Quantity(1800, 'revolution_per_minute')  # ✅ Correct

# For frequency (Hz)
Quantity(1800, 'rpm')  # ✅ Also correct, but different!
```

### 3. Gauge Pressure
```python
# Gauge pressure: add atmospheric offset in your code
gauge = Quantity(2, 'bar')  # 2 bar gauge
atmospheric = Quantity(1.01325, 'bar')
absolute = gauge + atmospheric  # 3.01 bar absolute
```

### 4. Wire Gauges
```python
# Use wire_gauge module, not unit strings
from unifyt import wire_gauge

# ✅ Correct
diameter = wire_gauge.awg_to_diameter(14)

# ❌ Wrong
# diameter = Quantity(14, 'AWG')  # No such unit!
```

---

## 🎯 Your Unit Mapping

```python
def map_your_units(unit_str):
    """Quick mapping for your industrial units."""
    mapping = {
        'MM': 'mm', 'CM': 'cm', 'IN': 'in', 'FT': 'ft',
        'BAR': 'bar', 'PSI': 'psi', 'KPA': 'kilopascal',
        'V': 'volt', 'A': 'ampere', 'HZ': 'hertz',
        'W': 'watt', 'KW': 'kilowatt', 'HP': 'horsepower',
        'LPM': 'liter_per_minute', 'CFM': 'cfm',
        'KG/HR': 'kg_hr', 'TPH': 'tph',
        'NM': 'Nm', 'RPM': 'revolution_per_minute',
    }
    return mapping.get(unit_str, unit_str.lower())

# Usage
from unifyt import Quantity
q = Quantity(100, map_your_units('MM'))
print(q)  # 100 millimeter
```

---

## 📚 More Information

- **Complete Guide**: `docs/NEW_UNITS_v0.2.1.md`
- **Your Units**: `YOUR_UNITS_COVERAGE.md`
- **Examples**: `python examples/new_units_demo.py`
- **RPM Guide**: `docs/RPM_CLARIFICATION.md`

---

## ✅ Quick Test

```bash
# Test wire gauges
python3 -c "from unifyt import wire_gauge; print(wire_gauge.awg_to_diameter(14))"

# Test torque
python3 -c "from unifyt import Quantity; print(Quantity(100, 'Nm').to('ft_lb'))"

# Test flow
python3 -c "from unifyt import Quantity; print(Quantity(100, 'lpm').to('gpm'))"

# Run full demo
python examples/new_units_demo.py
```

---

**You're ready to use the new units!** 🚀
