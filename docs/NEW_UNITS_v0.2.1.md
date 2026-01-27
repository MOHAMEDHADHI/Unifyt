# New Units Added to Unifyt v0.2.1

## Overview

This document describes all the new units and features added to Unifyt library to support industrial and engineering applications.

## Summary of Additions

- **Wire Gauge Systems**: 3 complete standards (AWG, SWG, BWG)
- **Torque Units**: 8 new unit definitions
- **Flow Rate Units**: 15+ new mass and volumetric flow units
- **Angular Velocity**: 8 new units
- **Paper/Fabric Weight**: GSM support
- **Specialized Units**: 15+ additional industrial units

**Total New Units**: 50+ unit definitions added

---

## 1. Wire Gauge Conversions

### New Module: `unifyt.wire_gauge`

Complete support for three wire gauge standards with bidirectional conversions.

#### American Wire Gauge (AWG)
- **Range**: 0000, 000, 00, 0 through 44
- **Usage**: North American electrical wire standard
- **Conversion**: Non-linear lookup table to diameter

```python
from unifyt import wire_gauge, Quantity

# Convert gauge to diameter
diameter = wire_gauge.awg_to_diameter(14)
print(diameter)  # 1.628 millimeter

# Convert to inches
diameter_in = wire_gauge.awg_to_diameter(14, 'inch')
print(diameter_in)  # 0.0641 inch

# Find gauge from diameter
wire_dia = Quantity(1.6, 'millimeter')
gauge = wire_gauge.diameter_to_awg(wire_dia)
print(gauge)  # 14
```

#### Standard Wire Gauge (SWG)
- **Range**: 0 through 50
- **Usage**: British Imperial wire standard
- **Application**: UK electrical and mechanical wire

```python
# SWG conversions
diameter = wire_gauge.swg_to_diameter(14)
print(diameter)  # 2.032 millimeter

gauge = wire_gauge.diameter_to_swg(Quantity(2.0, 'mm'))
print(gauge)  # 14
```

#### Birmingham Wire Gauge (BWG)
- **Range**: 0 through 36
- **Usage**: Steel wire, tubing, and needles
- **Application**: Medical, industrial tubing

```python
# BWG conversions
diameter = wire_gauge.bwg_to_diameter(14)
print(diameter)  # 2.108 millimeter

gauge = wire_gauge.diameter_to_bwg(Quantity(2.1, 'mm'))
print(gauge)  # 14
```

#### API Reference

**Functions:**
- `awg_to_diameter(gauge, unit='millimeter')` → Quantity
- `swg_to_diameter(gauge, unit='millimeter')` → Quantity
- `bwg_to_diameter(gauge, unit='millimeter')` → Quantity
- `diameter_to_awg(diameter)` → int
- `diameter_to_swg(diameter)` → int
- `diameter_to_bwg(diameter)` → int

**Class:**
- `WireGaugeConverter` - Class-based interface for all conversions

---

## 2. Torque Units

### New Unit Definitions

Torque units are dimensionally equivalent to energy (force × distance) but contextually different.

#### SI Torque Units
```python
from unifyt import Quantity

# Newton-meter (primary SI unit)
torque = Quantity(100, 'newton_meter')  # Full name
torque = Quantity(100, 'Nm')            # Shorthand
torque = Quantity(100, 'N_m')           # Alternative

# Kilonewton-meter (large applications)
torque = Quantity(5, 'kilonewton_meter')  # or 'kNm'
```

#### Imperial Torque Units
```python
# Foot-pound
torque = Quantity(75, 'foot_pound')   # Full name
torque = Quantity(75, 'ft_lb')        # Shorthand
torque = Quantity(75, 'pound_foot')   # Alternative
torque = Quantity(75, 'lb_ft')        # Alternative

# Inch-pound (small fasteners)
torque = Quantity(120, 'inch_pound')  # Full name
torque = Quantity(120, 'in_lb')       # Shorthand
```

#### Conversions
```python
# Convert between systems
torque_nm = Quantity(100, 'Nm')
torque_ftlb = torque_nm.to('foot_pound')
print(torque_ftlb)  # 73.76 foot_pound

# Practical example
bolt_torque = Quantity(85, 'ft_lb')
print(bolt_torque.to('Nm'))  # 115.24 newton_meter
```

**Conversion Factors:**
- 1 Nm = 0.7376 ft-lb
- 1 ft-lb = 1.3558 Nm
- 1 in-lb = 0.1130 Nm

---

## 3. Mass Flow Rate Units

### New Unit Definitions

Support for industrial process flow measurements.

#### SI Mass Flow Units
```python
# Kilogram per second (base unit)
flow = Quantity(10, 'kilogram_per_second')  # or 'kg_s'

# Kilogram per minute
flow = Quantity(600, 'kilogram_per_minute')  # or 'kg_min'

# Kilogram per hour
flow = Quantity(1000, 'kilogram_per_hour')  # or 'kg_hr', 'kg_h'

# Ton per hour (industrial)
flow = Quantity(5, 'ton_per_hour')  # or 'tph', 't_h'
```

#### Imperial Mass Flow Units
```python
# Pound per second
flow = Quantity(22, 'pound_per_second')  # or 'lb_s'

# Pound per minute
flow = Quantity(1320, 'pound_per_minute')  # or 'lb_min'

# Pound per hour
flow = Quantity(79200, 'pound_per_hour')  # or 'lb_hr'
```

#### Conversions
```python
# Convert between units
flow_kg_hr = Quantity(1000, 'kg_hr')
flow_kg_s = flow_kg_hr.to('kilogram_per_second')
print(flow_kg_s)  # 0.2778 kilogram_per_second

flow_tph = Quantity(5, 'tph')
print(flow_tph.to('kg_hr'))  # 5000 kilogram_per_hour
```

---

## 4. Volumetric Flow Rate Units

### New Unit Definitions

Additional volumetric flow units for HVAC, pumps, and process engineering.

#### SI Volumetric Flow
```python
# Cubic meter per minute
flow = Quantity(10, 'cubic_meter_per_minute')  # or 'm3_min'

# Cubic meter per hour
flow = Quantity(600, 'cubic_meter_per_hour')  # or 'm3_hr', 'm3_h'
```

#### Imperial Volumetric Flow
```python
# Cubic foot per minute (HVAC standard)
flow = Quantity(500, 'cubic_foot_per_minute')  # or 'cfm', 'ft3_min'

# Cubic foot per second
flow = Quantity(8.33, 'cubic_foot_per_second')  # or 'cfs', 'ft3_s'
```

#### Conversions
```python
# HVAC example
air_flow = Quantity(500, 'cfm')
print(air_flow.to('cubic_meter_per_hour'))  # 849.5 m³/h
print(air_flow.to('liter_per_second'))      # 236.0 L/s

# Pump example
pump_flow = Quantity(100, 'liter_per_minute')
print(pump_flow.to('cubic_meter_per_hour'))  # 6.0 m³/h
print(pump_flow.to('gallon_per_minute'))     # 26.4 gpm
```

---

## 5. Angular Velocity Units

### New Unit Definitions

Support for rotational speed measurements.

#### SI Angular Velocity
```python
# Radian per second (base unit)
omega = Quantity(10, 'radian_per_second')  # or 'rad_s'

# Degree per second
omega = Quantity(573, 'degree_per_second')  # or 'deg_s'
```

#### Rotational Speed
```python
# Revolution per minute (alternative to rpm)
speed = Quantity(1800, 'revolution_per_minute')  # or 'rev_min'

# Revolution per second
speed = Quantity(30, 'revolution_per_second')  # or 'rev_s'
```

#### Conversions
```python
# Motor speed
motor_rpm = Quantity(1800, 'rpm')
omega = motor_rpm.to('radian_per_second')
print(omega)  # 188.5 radian_per_second

# Calculate linear velocity
radius = Quantity(0.5, 'meter')
linear_vel = omega.magnitude * radius.magnitude
print(Quantity(linear_vel, 'meter/second'))  # 94.2 m/s
```

**Conversion Factors:**
- 1 rpm = 0.1047 rad/s
- 1 rev/s = 6.283 rad/s
- 1 deg/s = 0.01745 rad/s

---

## 6. Paper and Fabric Weight

### GSM (Grams per Square Meter)

Standard unit for paper and fabric weight.

```python
# Paper weights
copy_paper = Quantity(80, 'gsm')
cardstock = Quantity(200, 'gsm')
newspaper = Quantity(45, 'gsm')

# Convert to kg/m²
print(copy_paper.to('kilogram/meter^2'))  # 0.08 kg/m²

# Calculate total weight
a4_area = Quantity(0.0625, 'meter^2')  # 210mm × 297mm
sheets = 500
total_weight = copy_paper.magnitude * a4_area.magnitude * sheets
print(Quantity(total_weight, 'kilogram'))  # 2.5 kg
```

**Common Paper Weights:**
- Newspaper: 45-50 GSM
- Copy paper: 70-80 GSM
- Brochure: 115-130 GSM
- Cardstock: 200-300 GSM

---

## 7. Additional Specialized Units

### Specific Energy (Energy per Mass)
```python
# Joule per kilogram
specific_energy = Quantity(1000, 'joule_per_kilogram')  # or 'J_kg'

# Kilojoule per kilogram
specific_energy = Quantity(5, 'kilojoule_per_kilogram')  # or 'kJ_kg'

# Calorie per gram
specific_energy = Quantity(4, 'calorie_per_gram')  # or 'cal_g'
```

### Specific Volume (Volume per Mass)
```python
# Cubic meter per kilogram
specific_vol = Quantity(0.001, 'cubic_meter_per_kilogram')  # or 'm3_kg'

# Liter per kilogram
specific_vol = Quantity(1, 'liter_per_kilogram')  # or 'L_kg'
```

### Surface Tension
```python
# Newton per meter
surface_tension = Quantity(0.072, 'newton_per_meter')  # or 'N_m'

# Dyne per centimeter
surface_tension = Quantity(72, 'dyne_per_centimeter')  # or 'dyn_cm'
```

### Moment of Inertia
```python
# Kilogram meter squared
inertia = Quantity(10, 'kilogram_meter_squared')  # or 'kg_m2'

# Gram centimeter squared
inertia = Quantity(1000, 'gram_centimeter_squared')  # or 'g_cm2'
```

### Thermal Properties
```python
# Calorie per gram celsius
specific_heat = Quantity(1, 'calorie_per_gram_celsius')  # or 'cal_g_C'

# BTU per pound fahrenheit
specific_heat = Quantity(1, 'btu_per_pound_fahrenheit')  # or 'BTU_lb_F'
```

---

## Complete Unit List

### Torque (8 units)
- newton_meter, Nm, N_m
- kilonewton_meter, kNm
- foot_pound, ft_lb, foot_lb
- pound_foot, lb_ft
- inch_pound, in_lb, inch_lb

### Mass Flow Rate (13 units)
- kilogram_per_second, kg_s
- kilogram_per_minute, kg_min
- kilogram_per_hour, kg_hr, kg_h
- ton_per_hour, tph, t_h
- pound_per_second, lb_s
- pound_per_minute, lb_min
- pound_per_hour, lb_hr

### Volumetric Flow Rate (8 units)
- cubic_meter_per_minute, m3_min
- cubic_meter_per_hour, m3_hr, m3_h
- cubic_foot_per_minute, cfm, ft3_min
- cubic_foot_per_second, cfs, ft3_s

### Angular Velocity (8 units)
- radian_per_second, rad_s
- degree_per_second, deg_s
- revolution_per_minute, rev_min
- revolution_per_second, rev_s

### Paper/Fabric (2 units)
- gsm
- grams_per_square_meter

### Specific Energy (7 units)
- joule_per_kilogram, J_kg
- kilojoule_per_kilogram, kJ_kg
- megajoule_per_kilogram, MJ_kg
- calorie_per_gram, cal_g

### Specific Volume (2 units)
- cubic_meter_per_kilogram, m3_kg
- liter_per_kilogram, L_kg

### Surface Tension (2 units)
- newton_per_meter, N_m
- dyne_per_centimeter, dyn_cm

### Moment of Inertia (2 units)
- kilogram_meter_squared, kg_m2
- gram_centimeter_squared, g_cm2

### Thermal Properties (2 units)
- calorie_per_gram_celsius, cal_g_C
- btu_per_pound_fahrenheit, BTU_lb_F

---

## Testing

All new units have been tested with:
- Unit conversion accuracy
- Dimensional consistency
- Array operations
- Edge cases

Run tests:
```bash
pytest tests/test_wire_gauge.py -v
```

---

## Examples

See `examples/new_units_demo.py` for comprehensive demonstrations of all new units.

Run the demo:
```bash
python examples/new_units_demo.py
```

---

## Backward Compatibility

All new units are **fully backward compatible**. Existing code will continue to work without any changes.

---

## Future Enhancements

Potential additions for future versions:
- pH scale support (logarithmic)
- Decibel support (logarithmic)
- Additional wire gauge standards (IEC, JIS)
- More specialized industrial units

---

## Documentation Updates

- README.md - Updated with new unit examples
- CHANGELOG.md - Complete list of additions
- API documentation - Wire gauge module documented
- Test coverage - Full test suite for new units

---

**Version**: 0.2.1 (Unreleased)  
**Date**: 2025-01-27  
**Total New Units**: 50+ definitions  
**New Module**: wire_gauge  
**Backward Compatible**: Yes ✅
