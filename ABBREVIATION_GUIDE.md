# Unifyt Abbreviation Guide for Professionals

## Important: Correct Abbreviations

### Time Units
| Full Name | Correct Abbreviation | ❌ Common Mistake |
|-----------|---------------------|-------------------|
| second    | `s` or `sec`        | -                 |
| minute    | `min`               | ❌ `m` (this is meter!) |
| hour      | `h`, `hr`           | -                 |
| day       | `d`                 | -                 |

### Length Units
| Full Name | Abbreviation |
|-----------|-------------|
| meter     | `m`         |
| kilometer | `km`        |
| centimeter| `cm`        |
| millimeter| `mm`        |
| inch      | `in`        |
| foot      | `ft`        |
| mile      | `mi`        |

### Mass Units
| Full Name | Abbreviation |
|-----------|-------------|
| kilogram  | `kg`        |
| gram      | `g`         |
| pound     | `lb`        |
| ounce     | `oz`        |

### Pressure Units
| Full Name | Abbreviation |
|-----------|-------------|
| pascal    | `Pa`        |
| kilopascal| `kPa`       |
| bar       | `bar`       |
| psi       | `psi`, `PSI`|
| atmosphere| `atm`       |
| torr      | `torr`      |

### Temperature Units
| Full Name | Abbreviation | Note |
|-----------|-------------|------|
| celsius   | `celsius`, `degC` | ⚠️ Use full name for conversions |
| fahrenheit| `fahrenheit`, `degF` | ⚠️ Use full name for conversions |
| kelvin    | `kelvin`, `K` | ⚠️ Use full name for conversions |

### Energy Units
| Full Name | Abbreviation |
|-----------|-------------|
| joule     | `J`         |
| kilojoule | `kJ`        |
| calorie   | `cal`       |
| kilocalorie| `kcal`     |
| BTU       | `BTU`, `btu`|
| kilowatt_hour | `kWh`   |

### Power Units
| Full Name | Abbreviation |
|-----------|-------------|
| watt      | `W`         |
| kilowatt  | `kW`        |
| megawatt  | `MW`        |
| horsepower| `hp`        |

## Common Mistakes and Solutions

### ❌ Wrong: Converting seconds to 'm' (meter)
```python
# This will FAIL - incompatible dimensions
Quantity('10 s', 'm')  # ERROR: Cannot convert time to length
```

### ✅ Correct: Converting seconds to 'min' (minute)
```python
# Use 'min' for minute, not 'm'
Quantity('10 s', 'min')  # ✓ Works: 0.1667 min
Quantity('60 second', 'minute')  # ✓ Works: 1.0 minute
```

### ✅ Correct: Converting meters to kilometers
```python
# 'm' is for meter (length)
Quantity('1000 m', 'km')  # ✓ Works: 1.0 km
```

## Quick Reference for Industry Professionals

### Aerospace/Mechanical Engineering
```python
# Speed
Quantity('100 km/hr', 'm/s')  # ✓ 27.78 m/s
Quantity('500 knot', 'km/hr')  # ✓ 926.0 km/hr

# Pressure
Quantity('14.7 psi', 'bar')  # ✓ 1.01 bar
Quantity('1 atm', 'Pa')  # ✓ 101325.0 Pa

# Force
Quantity('1000 N', 'kN')  # ✓ 1.0 kN
```

### HVAC/Mechanical
```python
# Flow rate
Quantity('100 cfm', 'm3_min')  # Cubic feet per minute to cubic meters per minute
Quantity('50 L_min', 'gpm')  # Liters per minute to gallons per minute

# Pressure
Quantity('2 bar', 'psi')  # ✓ 29.0 psi
```

### Electrical Engineering
```python
# Power
Quantity('5 kW', 'W')  # ✓ 5000.0 W
Quantity('1 hp', 'kW')  # ✓ 0.746 kW

# Voltage
Quantity('230 V', 'kV')  # ✓ 0.23 kV
```

### Oil & Gas
```python
# Pressure
Quantity('1000 psi', 'bar')  # ✓ 68.95 bar
Quantity('50 bar', 'MPa')  # ✓ 5.0 MPa

# Flow rate
Quantity('100 gpm', 'L_min')  # Gallons per minute to liters per minute
```

## Best Practices

1. **Always use standard abbreviations**: Use `min` for minute, not `m`
2. **Be explicit when needed**: Use full names like `'second'`, `'minute'` if unsure
3. **Check dimensions**: Time units can't convert to length units
4. **Use compound units correctly**: `'km/hr'`, `'m/s'`, `'kg/m3'`
5. **Temperature conversions**: Use full names (`'celsius'`, `'fahrenheit'`, `'kelvin'`)

## Testing Your Conversions

Run the test suite to verify all conversions work:
```bash
python test_abbreviations.py
```

This will test all common abbreviations and conversions used in industry.
