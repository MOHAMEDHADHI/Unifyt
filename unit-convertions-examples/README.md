# Industry-Specific Unit Conversion Examples

This directory contains real-world unit conversion examples tailored for specific industries. Each file demonstrates the most commonly used conversions that professionals encounter in their daily work.

## Available Industry Examples

### 1. **Aerospace Engineering** (`aerospace_engineering.py`)
Real-world conversions for aircraft, rockets, and spacecraft operations.

**Topics Covered:**
- Aircraft Performance (airspeed, altitude, climb rate, fuel consumption)
- Rocket Propulsion (thrust, specific impulse, chamber pressure)
- Orbital Mechanics (orbital velocity, altitude, delta-v)
- Aerodynamics (dynamic pressure, Mach number, Reynolds number)
- Structural Loads (load factors, stress, strain)
- Propulsion Efficiency (TSFC, efficiencies)
- Atmospheric Conditions (pressure, temperature, density at various altitudes)
- Range and Endurance calculations

**Key Units:** knot, foot, nautical_mile, pound_force, psi, mach

---

### 2. **Oil & Gas Industry** (`oil_and_gas.py`)
Petroleum engineering, drilling, production, and refining conversions.

**Topics Covered:**
- Drilling Operations (well depth, ROP, mud weight, downhole pressure)
- Production Rates (oil/gas production, barrels per day, MMSCFD)
- Reservoir Properties (pressure, temperature, permeability, porosity)
- Pipeline Transportation (diameter, flow rate, pressure)
- Refining Operations (capacity, distillation temperatures, API gravity)
- Storage and Handling (tank capacity, vapor pressure)
- Well Testing (flow rates, productivity index)
- Enhanced Oil Recovery (steam injection, CO2 injection)

**Key Units:** barrel, psi, MMSCFD, darcy, API gravity, ppg (pounds per gallon)

---

### 3. **Civil Engineering** (`civil_engineering.py`)
Structural design, construction, and infrastructure projects.

**Topics Covered:**
- Structural Loads (dead load, live load, wind load, snow load)
- Concrete Properties (compressive strength, modulus of elasticity)
- Steel Properties (yield strength, ultimate strength)
- Foundation Design (bearing capacity, settlement, pile capacity)
- Earthwork and Excavation (volume, soil density, compaction)
- Pavement Design (thickness, traffic load, tire pressure)
- Hydraulics and Drainage (flow rate, pipe diameter, rainfall)
- Bridge Design (span length, design loads, deflection)
- Building Dimensions (height, floor area, wall thickness)
- Construction Materials (concrete volume, rebar weight, cement)

**Key Units:** megapascal, kilonewton, cubic_meter, cubic_yard, pound/foot^2

---

### 4. **Electrical Power Engineering** (`electrical_power.py`)
Power generation, transmission, distribution, and electrical systems.

**Topics Covered:**
- Power Generation (generator capacity, voltage, current, efficiency)
- Transmission Lines (HV/EHV/UHV levels, line length, power loss)
- Transformers (rating, voltage transformation, losses)
- Distribution Systems (voltage levels, feeder capacity, cable size)
- Power Factor and Reactive Power (active, reactive, apparent power)
- Circuit Protection (breaking capacity, fault current, trip time)
- Energy Consumption (industrial loads, monthly consumption, costs)
- Renewable Energy (solar panels, wind turbines, battery storage)

**Key Units:** megawatt, kilovolt, ampere, kilowatt_hour, kVA, kVAR

---

### 5. **HVAC & Mechanical Engineering** (`hvac_mechanical.py`)
Heating, ventilation, air conditioning, and mechanical systems.

**Topics Covered:**
- Cooling Capacity (tons of refrigeration, BTU/hr, chiller capacity)
- Air Flow Rates (CFM, duct velocity, duct dimensions)
- Heating Capacity (boiler capacity, heating load, fuel consumption)
- Temperature Control (room temperature, supply air, design conditions)
- Pressure and Static (static pressure, fan pressure, pressure drop)
- Humidity Control (relative humidity, dew point, moisture removal)
- Energy Efficiency (COP, EER, SEER, annual energy use)
- Ventilation Requirements (fresh air, air changes per hour)
- Refrigeration Cycle (evaporator/condenser temps and pressures)
- Thermal Loads (sensible/latent heat, heat gain from occupants)

**Key Units:** ton (refrigeration), CFM, BTU/hr, inches water column, COP

---

### 6. **Universal Volume Converter** (`volume_to_cubic_meter.py`) ⭐ NEW
Convert any volume unit to cubic meters with interactive and batch modes.

**Features:**
- Interactive conversion mode
- Command-line direct conversion
- Batch conversion for multiple values
- Practical application examples
- Real-world scenarios (construction, logistics, water management, HVAC)

**Supported Units:** liter, gallon, milliliter, quart, pint, cup, fluid_ounce, cubic_meter

**Usage:**
```bash
# Interactive mode
python volume_to_cubic_meter.py

# Direct conversion
python volume_to_cubic_meter.py 100 liter

# See demonstrations
python volume_to_cubic_meter.py --demo

# See applications
python volume_to_cubic_meter.py --apps
```

**See:** `VOLUME_CONVERTER_README.md` for detailed documentation

---

### 7. **Cubic Meter to Meter Converter** (`cubic_meter_to_meter.py`) ⭐ NEW
Calculate cube side length from volume - visualize volumes as dimensions.

**Features:**
- Calculate equivalent cube dimensions from volume
- Interactive and command-line modes
- Batch conversion for multiple volumes
- Additional calculations (surface area, edge length)
- Real-world visualization examples
- Quick reference table

**Formula:** `side_length = ∛(volume)`

**Usage:**
```bash
# Interactive mode
python cubic_meter_to_meter.py

# Direct conversion
python cubic_meter_to_meter.py 8
# Output: 2.0000 m (a 2m × 2m × 2m cube)

# See demonstrations
python cubic_meter_to_meter.py --demo

# See applications
python cubic_meter_to_meter.py --apps

# Show reference table
python cubic_meter_to_meter.py --table
```

**Applications:**
- Room design and space visualization
- Warehouse storage planning
- Water tank sizing
- Concrete volume estimation
- HVAC system sizing

**See:** `CUBIC_METER_CONVERTER_README.md` for detailed documentation

---

### 8. **Wire Gauge Converter** (`wire_gauge_converter.py`) ⭐ NEW v0.2.1
Convert between wire gauge standards (AWG, SWG, BWG) and physical diameters.

**Features:**
- AWG (American Wire Gauge) - 0000 to 44
- SWG (Standard Wire Gauge) - 0 to 50
- BWG (Birmingham Wire Gauge) - 0 to 36
- Bidirectional conversions (gauge ↔ diameter)
- Interactive mode with comparison tables
- Practical applications (electrical, jewelry, industrial)

**Usage:**
```bash
# Interactive mode
python wire_gauge_converter.py --interactive

# Run all demonstrations
python wire_gauge_converter.py
```

**Key Units:** AWG, SWG, BWG, millimeter, inch

---

### 9. **Torque Converter** (`torque_converter.py`) ⭐ NEW v0.2.1
Convert between torque units for automotive, industrial, and mechanical applications.

**Features:**
- Newton-meter (Nm) - SI standard
- Foot-pound (ft-lb) - Imperial standard
- Inch-pound (in-lb) - Small fasteners
- Kilonewton-meter (kNm) - Large applications
- Automotive specifications (engine, wheel, fastener torques)
- Interactive mode with practical examples

**Usage:**
```bash
# Interactive mode
python torque_converter.py --interactive

# Run all demonstrations
python torque_converter.py
```

**Key Units:** newton_meter, foot_pound, inch_pound, kilonewton_meter

---

### 10. **Flow Rate Converter** (`flow_rate_converter.py`) ⭐ NEW v0.2.1
Convert between mass and volumetric flow rates for HVAC, pumps, and industrial processes.

**Features:**
- Mass flow: kg/s, kg/min, kg/hr, tph, lb/s, lb/min, lb/hr
- Volumetric flow: m³/s, m³/min, m³/hr, L/s, lpm, L/hr, cfm, cfs, gpm
- HVAC applications (air handlers, chillers, cooling towers)
- Pump specifications
- Industrial process flows
- Interactive mode

**Usage:**
```bash
# Interactive mode
python flow_rate_converter.py --interactive

# Run all demonstrations
python flow_rate_converter.py
```

**Key Units:** kilogram_per_hour, liter_per_minute, cubic_meter_per_hour, cfm

---

### 11. **Angular Velocity Converter** (`angular_velocity_converter.py`) ⭐ NEW v0.2.1
Convert between rotational speed units for motors, machinery, and rotational mechanics.

**Features:**
- RPM (revolutions per minute) - Common motor speed
- RPS (revolutions per second)
- rad/s (radians per second) - SI standard
- deg/s (degrees per second)
- Motor specifications and applications
- Rotational mechanics calculations (linear velocity, centripetal acceleration)
- Power calculations from torque and speed
- RPM vs revolution_per_minute clarification

**Usage:**
```bash
# Interactive mode
python angular_velocity_converter.py --interactive

# Run all demonstrations
python angular_velocity_converter.py
```

**Key Units:** revolution_per_minute, radian_per_second, degree_per_second

**Important Note:** Unifyt has two RPM units:
- `'rpm'` - Frequency (Hz) for cycles per minute
- `'revolution_per_minute'` - Angular velocity (rad/s) for rotational speed

---

### 12. **Paper Weight (GSM) Converter** (`paper_weight_converter.py`) ⭐ NEW v0.2.1
Convert paper and fabric weights using GSM (grams per square meter).

**Features:**
- GSM to kg/m², lb/ft², oz/yd²
- Common paper types (copy paper, cardstock, newsprint)
- Fabric weights (cotton, denim, canvas)
- Printing industry specifications
- Paper ream weight calculations
- Cost and environmental impact analysis
- Interactive mode

**Usage:**
```bash
# Interactive mode
python paper_weight_converter.py --interactive

# Run all demonstrations
python paper_weight_converter.py
```

**Key Units:** gsm (grams per square meter), kilogram_per_meter^2

**Applications:**
- Printing and publishing
- Textile industry
- Packaging design
- Office supplies
- Environmental impact assessment

---

## How to Use These Examples

### Running Individual Files

Each file can be run independently:

```bash
# Aerospace engineering examples
python unit-convertions-examples/aerospace_engineering.py

# Oil & gas examples
python unit-convertions-examples/oil_and_gas.py

# Civil engineering examples
python unit-convertions-examples/civil_engineering.py

# Electrical power examples
python unit-convertions-examples/electrical_power.py

# HVAC examples
python unit-convertions-examples/hvac_mechanical.py
```

### Using in Your Code

You can also import and use specific functions:

```python
from unit_convertions_examples.aerospace_engineering import aircraft_performance
from unit_convertions_examples.oil_and_gas import drilling_operations

# Run specific examples
aircraft_performance()
drilling_operations()
```

### Adapting for Your Needs

Each example is structured to be easily modified:

```python
from unifyt import Quantity

# Modify values for your specific case
my_pressure = Quantity(5000, 'psi')
print(f"Pressure: {my_pressure.to('megapascal')}")
```

## Industry-Specific Notes

### Aerospace
- Uses both metric and imperial units (knots, feet, nautical miles)
- Critical for flight safety and performance calculations
- Includes orbital mechanics for space missions

### Oil & Gas
- Heavy use of industry-specific units (barrels, MMSCFD, API gravity)
- Pressure conversions are critical for safety
- Includes both upstream (drilling/production) and downstream (refining)

### Civil Engineering
- Primarily uses metric (SI) units with imperial conversions
- Stress/strength in MPa or psi
- Volume often in cubic meters or cubic yards

### Electrical Power
- Uses kW, MW, GW for power
- Voltage in kV for transmission
- Energy in kWh or MWh

### HVAC
- Unique units like "tons of refrigeration" and CFM
- Temperature in both Celsius and Fahrenheit
- Pressure in pascals or inches of water column

## Common Conversion Patterns

### Energy Conversions
```python
# Electrical energy
energy_kwh = Quantity(1000, 'kilowatt_hour')
energy_joules = energy_kwh.to('joule')
energy_mwh = energy_kwh.to('megawatt_hour')

# Thermal energy
energy_btu = 1000000  # BTU
energy_kj = energy_btu * 1.05506  # Convert to kJ
```

### Flow Rate Conversions
```python
# Volumetric flow
flow_cfm = 10000  # CFM
flow_m3_s = flow_cfm * 0.000471947  # to m³/s
flow_lps = flow_m3_s * 1000  # to L/s

# Mass flow
flow_kg_s = Quantity(100, 'kilogram/second')
flow_lb_hr = flow_kg_s.to('pound/hour')
```

### Pressure Conversions
```python
# Pressure
pressure_psi = Quantity(1000, 'psi')
pressure_mpa = pressure_psi.to('megapascal')
pressure_bar = pressure_psi.to('bar')
pressure_atm = pressure_psi.to('atmosphere')
```

## Best Practices

1. **Always specify units explicitly** - Don't assume default units
2. **Convert early** - Convert to your working units at the start
3. **Check dimensionality** - Unifyt will catch incompatible conversions
4. **Use constants** - Leverage built-in physical constants
5. **Document assumptions** - Note any conversion factors or assumptions

## Contributing

To add a new industry example:

1. Create a new file: `industry_name.py`
2. Follow the existing structure with sections and subsections
3. Include real-world values and scenarios
4. Add comprehensive comments
5. Update this README with the new industry

## Additional Resources

- **Main Documentation**: See `../docs/` for complete API reference
- **Basic Examples**: See `../examples/` for introductory examples
- **Comprehensive Examples**: See `unit_conversions_comprehensive.py` for extensive coverage
- **Units Catalog**: See `../final documents/UNITS_CATALOG.md` for all available units

## Support

For questions or issues:
- Check the main README.md
- Review the documentation in `../docs/`
- See examples in `../examples/`
- Refer to the units catalog for available units

---

**Note**: All examples use real-world values and industry-standard practices. Values are representative and should be verified for specific applications.
