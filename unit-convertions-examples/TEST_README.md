# Comprehensive Test File for Unifyt

## Overview

The `test.py` file contains comprehensive tests for ALL unit conversions used across all example files in this directory.

## What's Tested

### 1. Time Conversions (8 tests)
- Seconds ↔ Minutes
- Hours ↔ Minutes/Seconds
- Days ↔ Hours
- Weeks ↔ Days
- Years ↔ Days

### 2. Length Conversions (9 tests)
- Centimeters ↔ Meters
- Meters ↔ Kilometers
- Inches ↔ Centimeters
- Feet ↔ Meters
- Miles ↔ Kilometers
- Nautical miles ↔ Kilometers
- Yards ↔ Meters

### 3. Mass Conversions (6 tests)
- Pounds ↔ Kilograms
- Kilograms ↔ Grams
- Ounces ↔ Pounds
- Tons ↔ Kilograms

### 4. Pressure Conversions (8 tests)
- Bar ↔ Pascals
- PSI ↔ Bar
- Atmospheres ↔ Pascals
- Torr ↔ Atmospheres
- Kilopascals ↔ Pascals
- Megapascals ↔ Bar

### 5. Temperature Conversions (7 tests)
- Celsius ↔ Fahrenheit
- Celsius ↔ Kelvin
- Fahrenheit ↔ Kelvin

### 6. Energy Conversions (5 tests)
- Kilowatt-hours ↔ Joules
- Joules ↔ Kilojoules
- Calories ↔ Joules
- BTU ↔ Joules
- Kilocalories ↔ Joules

### 7. Power Conversions (5 tests)
- Kilowatts ↔ Watts
- Horsepower ↔ Watts
- Kilowatts ↔ Horsepower

### 8. Speed/Velocity Conversions (6 tests)
- km/h ↔ m/s
- mph ↔ km/h
- Knots ↔ km/h
- Knots ↔ m/s

### 9. Force Conversions (4 tests)
- Newtons ↔ Kilonewtons
- Pound-force ↔ Newtons
- Newtons ↔ Meganewtons

### 10. Torque Conversions (3 tests)
- Newton-meters ↔ Foot-pounds

### 11. Angular Velocity Conversions (3 tests)
- RPM ↔ rad/s
- rad/s ↔ deg/s

### 12. Voltage Conversions (3 tests)
- Kilovolts ↔ Volts

### 13. Volume Conversions (4 tests)
- Liters ↔ Cubic meters
- Gallons ↔ Liters

### 14. Flow Rate Conversions (3 tests)
- CFM ↔ m³/min
- L/min ↔ GPM

### 15. Area Conversions (3 tests)
- Square meters ↔ Square feet
- Hectares ↔ Square meters

### 16. Industry-Specific Conversions

#### Aerospace Engineering (6 tests)
- Altitude conversions (feet to meters)
- Orbital velocities
- Fuel flow rates
- Engine thrust

#### HVAC/Mechanical (2 tests)
- Pressure conversions for systems

#### Electrical Engineering (3 tests)
- Power conversions
- Energy conversions

#### Oil & Gas (4 tests)
- High-pressure conversions
- Volume conversions

#### Civil Engineering (5 tests)
- Length conversions
- Stress/pressure conversions

#### Automotive (3 tests)
- Speed conversions
- Tire pressure

### 17. Compound Units (2 tests)
- Density (kg/m³)
- Acceleration (m/s²)

## Total Tests: 100+ conversions

## How to Run

### Method 1: Direct Execution
```bash
cd unit-convertions-examples
python test.py
```

### Method 2: From Root Directory
```bash
python unit-convertions-examples/test.py
```

### Method 3: After pip install
```bash
pip install unifyt
python unit-convertions-examples/test.py
```

## Expected Output

```
================================================================================
UNIFYT COMPREHENSIVE TEST SUITE
Testing all conversions from example files
================================================================================

================================================================================
TIME CONVERSIONS
================================================================================
✓ 10 seconds to minutes                              = 0.16666666666666666 min
✓ 60 seconds to minutes                              = 1.0 min
...

================================================================================
TEST SUITE COMPLETE
================================================================================

All conversions tested successfully!
```

## Understanding Results

- **✓** = Test passed successfully
- **✗** = Test failed (shows error message)

All tests should show ✓ marks. If you see any ✗ marks, there's an issue with that specific conversion.

## What This Tests

This test file validates:
1. All abbreviations work correctly
2. All conversions produce results
3. The package is installed correctly
4. All example files will work

## Coverage

This test file covers conversions from:
- `aerospace_engineering.py`
- `angular_velocity_converter.py`
- `civil_engineering.py`
- `electrical_power.py`
- `flow_rate_converter.py`
- `hvac_mechanical.py`
- `oil_and_gas.py`
- `pressure_converter.py`
- `speed_converter.py`
- `temperature_converter.py`
- `torque_converter.py`
- `volume_to_cubic_meter.py`

## Key Abbreviations Used

### Time
- `s`, `sec` = second
- `min` = minute (NOT `m`!)
- `h`, `hr` = hour
- `d` = day

### Length
- `m` = meter
- `km` = kilometer
- `cm` = centimeter
- `ft` = foot
- `in` = inch
- `mi` = mile

### Mass
- `kg` = kilogram
- `g` = gram
- `lb` = pound
- `oz` = ounce

### Pressure
- `Pa` = pascal
- `kPa` = kilopascal
- `MPa` = megapascal
- `bar` = bar
- `psi` = pounds per square inch
- `atm` = atmosphere

### Power
- `W` = watt
- `kW` = kilowatt
- `hp` = horsepower

### Speed
- `m/s` = meters per second
- `km/hr` = kilometers per hour
- `mi/hr` = miles per hour
- `knot` = nautical miles per hour

## Troubleshooting

### If tests fail:

1. **Check installation:**
   ```bash
   pip install --upgrade unifyt
   ```

2. **Verify Python version:**
   ```bash
   python --version
   ```
   (Should be Python 3.7+)

3. **Check for typos:**
   - Use `min` for minute, not `m`
   - Use correct abbreviations from list above

4. **Run individual test:**
   ```python
   from unifyt import Quantity
   print(Quantity('10 s', 'min'))
   ```

## Adding Your Own Tests

To add more tests, use this format:

```python
def test_my_conversions():
    print_section("MY CUSTOM CONVERSIONS")
    
    test_conversion("Description", value, "from_unit", "to_unit")
    test_conversion("100 meters to feet", 100, "m", "ft")
    test_conversion("50 kg to pounds", 50, "kg", "lb")
```

Then add to `main()`:
```python
def main():
    # ... existing tests ...
    test_my_conversions()
```

## Success Criteria

✓ All tests show ✓ marks
✓ No error messages
✓ Exit code: 0
✓ "All conversions tested successfully!" message appears

## Notes

- This test file uses the CORRECT abbreviations
- `min` is used for minute (NOT `m`)
- `m` is used for meter
- All industry-standard abbreviations are tested
- Covers 100+ real-world conversion scenarios

## Related Files

- `../test_abbreviations.py` - Basic abbreviation tests
- `../run_excel_tests.py` - Excel-based test suite
- `../ABBREVIATION_GUIDE.md` - Complete abbreviation reference
- `../TESTING_GUIDE.md` - Testing documentation

## Summary

This comprehensive test file validates that ALL conversions from ALL example files work correctly with the unifyt package. Run it after installation to ensure everything is working properly!
