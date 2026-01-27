# New Unit Converters - Version 0.2.1

This document provides a comprehensive overview of the new unit converters added in Unifyt v0.2.1.

## Overview

Version 0.2.1 introduces five new specialized converters that demonstrate the newly added units:

1. **Wire Gauge Converter** - AWG, SWG, BWG standards
2. **Torque Converter** - Nm, ft-lb, in-lb, kNm
3. **Flow Rate Converter** - Mass and volumetric flow
4. **Angular Velocity Converter** - RPM, rad/s, deg/s, RPS
5. **Paper Weight Converter** - GSM and fabric weights

Each converter follows a consistent structure with:
- Comprehensive conversion tables
- Real-world applications and examples
- Interactive mode for user input
- Practical calculations and specifications

---

## 1. Wire Gauge Converter

**File:** `wire_gauge_converter.py`

### Standards Supported

- **AWG (American Wire Gauge)** - Gauges 0000 to 44
  - North American electrical standard
  - Used for electrical wiring, cables
  
- **SWG (Standard Wire Gauge)** - Gauges 0 to 50
  - British Imperial standard
  - Used in UK and Commonwealth countries
  
- **BWG (Birmingham Wire Gauge)** - Gauges 0 to 36
  - Steel wire and tubing standard
  - Used for steel wire, hypodermic needles

### Key Features

```python
from unifyt import wire_gauge

# Convert gauge to diameter
diameter = wire_gauge.awg_to_diameter(14)  # Returns Quantity in mm
print(diameter)  # 1.628 millimeter

# Convert diameter to gauge
gauge = wire_gauge.diameter_to_awg(1.6, 'mm')
print(gauge)  # 14 (closest gauge)

# Compare standards
awg_14 = wire_gauge.awg_to_diameter(14)  # 1.628 mm
swg_14 = wire_gauge.swg_to_diameter(14)  # 2.032 mm
bwg_14 = wire_gauge.bwg_to_diameter(14)  # 2.108 mm
```

### Applications

- **Electrical Wiring** - House wiring, appliances, circuits
- **Jewelry Making** - Wire wrapping, chain making
- **Industrial** - Steel wire, springs, fasteners
- **Medical** - Hypodermic needles (BWG)

### Usage

```bash
# Interactive mode
python wire_gauge_converter.py --interactive

# Run all demonstrations
python wire_gauge_converter.py
```

---

## 2. Torque Converter

**File:** `torque_converter.py`

### Units Supported

- **newton_meter (Nm)** - SI standard torque unit
- **kilonewton_meter (kNm)** - Large applications
- **foot_pound (ft-lb)** - Imperial standard
- **inch_pound (in-lb)** - Small fasteners

### Key Features

```python
from unifyt import Quantity

# Engine torque
engine_torque = Quantity(200, 'newton_meter')
print(engine_torque.to('foot_pound'))  # 147.51 foot_pound

# Bolt torque
bolt_torque = Quantity(75, 'foot_pound')
print(bolt_torque.to('newton_meter'))  # 101.69 newton_meter

# Small fastener
fastener = Quantity(120, 'inch_pound')
print(fastener.to('newton_meter'))  # 13.56 newton_meter
```

### Applications

- **Automotive** - Engine specs, wheel lug nuts, spark plugs
- **Bicycle** - Crank bolts, stem bolts, brake calipers
- **Industrial** - Machinery assembly, equipment maintenance
- **Construction** - Structural bolts, anchor bolts

### Practical Examples

| Application | Torque (Nm) | Torque (ft-lb) |
|-------------|-------------|----------------|
| Spark plug | 20-30 | 15-22 |
| Wheel lug nut | 100-120 | 74-89 |
| Cylinder head bolt | 80-100 | 59-74 |
| Engine mount | 50-70 | 37-52 |

### Usage

```bash
# Interactive mode
python torque_converter.py --interactive

# Run all demonstrations
python torque_converter.py
```

---

## 3. Flow Rate Converter

**File:** `flow_rate_converter.py`

### Units Supported

**Mass Flow:**
- kilogram_per_second (kg/s)
- kilogram_per_minute (kg/min)
- kilogram_per_hour (kg/hr)
- ton_per_hour (tph)
- pound_per_second (lb/s)
- pound_per_minute (lb/min)
- pound_per_hour (lb/hr)

**Volumetric Flow:**
- cubic_meter_per_second (m³/s)
- cubic_meter_per_minute (m³/min)
- cubic_meter_per_hour (m³/hr)
- liter_per_second (L/s)
- liter_per_minute (lpm)
- liter_per_hour (L/hr)
- cubic_foot_per_minute (cfm)
- cubic_foot_per_second (cfs)
- gallon_per_minute (gpm)

### Key Features

```python
from unifyt import Quantity

# Mass flow
mass_flow = Quantity(1000, 'kilogram_per_hour')
print(mass_flow.to('kilogram_per_second'))  # 0.2778 kg/s
print(mass_flow.to('ton_per_hour'))  # 1.0 tph

# Volumetric flow
vol_flow = Quantity(100, 'liter_per_minute')
print(vol_flow.to('cubic_meter_per_hour'))  # 6.0 m³/hr
print(vol_flow.to('gallon_per_minute'))  # 26.42 gpm
```

### Applications

- **HVAC** - Air handlers, chillers, cooling towers
- **Pumps** - Water pumps, chemical pumps, fuel pumps
- **Industrial** - Process flows, material handling
- **Water Treatment** - Treatment plants, distribution systems

### Practical Examples

| Application | Flow Rate | Equivalent |
|-------------|-----------|------------|
| Residential AC | 400 cfm | 679 m³/hr |
| Chiller | 500 gpm | 1893 lpm |
| Cooling tower | 1000 gpm | 3785 lpm |
| Process pump | 5000 kg/hr | 1.39 kg/s |

### Usage

```bash
# Interactive mode
python flow_rate_converter.py --interactive

# Run all demonstrations
python flow_rate_converter.py
```

---

## 4. Angular Velocity Converter

**File:** `angular_velocity_converter.py`

### Units Supported

- **revolution_per_minute** - Common motor speed (RPM)
- **revolution_per_second** - RPS
- **radian_per_second** - SI standard (rad/s)
- **degree_per_second** - deg/s

### Important: RPM Disambiguation

Unifyt has **two different RPM units**:

1. **`'rpm'`** - Frequency unit (cycles per minute)
   - Dimension: 1/time (Hz)
   - Use for: Rotation frequency, cycles, oscillations
   - Converts to: Hz, kHz

2. **`'revolution_per_minute'`** - Angular velocity unit
   - Dimension: angle/time (rad/s)
   - Use for: Rotational speed, angular motion
   - Converts to: rad/s, deg/s, revolution_per_second

### Key Features

```python
from unifyt import Quantity

# Motor speed (angular velocity)
motor_speed = Quantity(1800, 'revolution_per_minute')
print(motor_speed.to('radian_per_second'))  # 188.50 rad/s
print(motor_speed.to('degree_per_second'))  # 10800 deg/s

# Frequency
freq = Quantity(1800, 'rpm')
print(freq.to('hertz'))  # 30.0 Hz
```

### Applications

- **Motors** - AC motors, DC motors, servo motors
- **Machinery** - Pumps, fans, compressors, grinders
- **Rotational Mechanics** - Linear velocity calculations, power calculations
- **Automotive** - Engine RPM, wheel speed

### Rotational Calculations

```python
# Linear velocity from angular velocity
# v = ω × r
rpm = 300
radius = Quantity(0.5, 'meter')
angular_vel = Quantity(rpm, 'revolution_per_minute')
omega = angular_vel.to('radian_per_second')  # 31.42 rad/s

linear_vel = omega.magnitude * radius.magnitude  # 15.71 m/s

# Power from torque and speed
# P = τ × ω
torque = Quantity(100, 'newton_meter')
power_watts = torque.magnitude * omega.magnitude  # 3142 W
```

### Usage

```bash
# Interactive mode
python angular_velocity_converter.py --interactive

# Run all demonstrations
python angular_velocity_converter.py
```

---

## 5. Paper Weight (GSM) Converter

**File:** `paper_weight_converter.py`

### Units Supported

- **gsm** - Grams per square meter (g/m²)
- **kilogram_per_meter^2** - kg/m²
- **pound_per_foot^2** - lb/ft²
- **ounce_per_yard^2** - oz/yd² (fabric weight)

### Key Features

```python
from unifyt import Quantity

# Paper weight
copy_paper = Quantity(80, 'gsm')
print(copy_paper.to('kilogram_per_meter^2'))  # 0.080 kg/m²

cardstock = Quantity(200, 'gsm')
print(cardstock.to('pound_per_foot^2'))  # 0.041 lb/ft²

# Calculate ream weight
a4_area = 0.210 * 0.297  # m²
sheets = 500
weight_per_sheet = copy_paper.magnitude * a4_area  # kg
total_weight = weight_per_sheet * sheets  # 2.50 kg
```

### Applications

- **Printing** - Copy paper, brochures, business cards
- **Publishing** - Books, magazines, newspapers
- **Packaging** - Boxes, cartons, labels
- **Textiles** - Fabric weight, clothing
- **Environmental** - Paper consumption, CO2 impact

### Common Paper Types

| Paper Type | GSM Range | Application |
|------------|-----------|-------------|
| Tissue paper | 10-20 | Gift wrap, facial tissue |
| Newsprint | 40-50 | Newspapers |
| Copy paper | 70-80 | Office printing |
| Brochure | 90-120 | Marketing materials |
| Cardstock | 180-300 | Business cards, invitations |
| Poster board | 300-400 | Posters, displays |

### Fabric Weights

| Fabric Type | GSM Range | Application |
|-------------|-----------|-------------|
| Sheer chiffon | 30-50 | Scarves, overlays |
| Light cotton | 80-120 | Summer shirts |
| Medium cotton | 130-180 | T-shirts |
| Denim (light) | 200-280 | Light jeans |
| Denim (heavy) | 450-600 | Heavy-duty jeans |
| Canvas | 400-600 | Tents, bags |

### Usage

```bash
# Interactive mode
python paper_weight_converter.py --interactive

# Run all demonstrations
python paper_weight_converter.py
```

---

## Common Usage Patterns

### Interactive Mode

All converters support interactive mode:

```bash
python <converter_name>.py --interactive
```

This provides:
- User-friendly prompts
- Input validation
- Multiple conversion options
- Practical examples

### Programmatic Usage

Import and use in your code:

```python
from unifyt import Quantity, wire_gauge

# Wire gauge
diameter = wire_gauge.awg_to_diameter(14)

# Torque
torque = Quantity(100, 'newton_meter')
ft_lb = torque.to('foot_pound')

# Flow rate
flow = Quantity(1000, 'kilogram_per_hour')
kg_s = flow.to('kilogram_per_second')

# Angular velocity
speed = Quantity(1800, 'revolution_per_minute')
rad_s = speed.to('radian_per_second')

# Paper weight
paper = Quantity(80, 'gsm')
kg_m2 = paper.to('kilogram_per_meter^2')
```

---

## Integration with Existing Converters

These new converters complement the existing industry-specific converters:

- **Aerospace Engineering** - Can now use torque for fasteners
- **Oil & Gas** - Can use flow rates for pipelines
- **Civil Engineering** - Can use torque for structural bolts
- **Electrical Power** - Can use wire gauges for cables
- **HVAC** - Can use flow rates and angular velocity for fans/pumps

---

## Best Practices

1. **Use Interactive Mode** for learning and exploration
2. **Use Programmatic Mode** for automation and integration
3. **Check Units** - Always verify input/output units
4. **Read Documentation** - Each converter has detailed comments
5. **Understand Context** - Use appropriate units for your application

---

## Testing the Converters

Run each converter to see demonstrations:

```bash
# Wire gauge
python unit-convertions-examples/wire_gauge_converter.py

# Torque
python unit-convertions-examples/torque_converter.py

# Flow rate
python unit-convertions-examples/flow_rate_converter.py

# Angular velocity
python unit-convertions-examples/angular_velocity_converter.py

# Paper weight
python unit-convertions-examples/paper_weight_converter.py
```

---

## Related Documentation

- **Main README**: `../README.md`
- **New Units Documentation**: `../docs/NEW_UNITS_v0.2.1.md`
- **RPM Clarification**: `../docs/RPM_CLARIFICATION.md`
- **Quick Start**: `../QUICK_START_NEW_UNITS.md`
- **Implementation Details**: `../IMPLEMENTATION_COMPLETE.md`

---

## Support

For questions or issues:
- Check the main documentation
- Review the examples
- See the units catalog
- Test with interactive mode

---

**Version:** 0.2.1  
**Date:** 2025-01-27  
**Author:** Unifyt Team
