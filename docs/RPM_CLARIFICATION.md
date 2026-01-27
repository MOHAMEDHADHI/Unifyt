# RPM Clarification - Frequency vs Angular Velocity

## The RPM Ambiguity

The abbreviation **RPM** (revolutions per minute) can mean two different things:

### 1. Frequency (Cycles per Minute)
- **Dimension**: 1/time (Hz)
- **Use case**: Oscillations, vibrations, cycles
- **Unifyt unit**: `'rpm'`
- **Conversion**: 1 rpm = 1/60 Hz

### 2. Angular Velocity (Radians per Second)
- **Dimension**: angle/time (rad/s)
- **Use case**: Rotational speed, motor speed, spinning objects
- **Unifyt unit**: `'revolution_per_minute'` or `'rev_min'`
- **Conversion**: 1 rev/min = 2π/60 rad/s ≈ 0.1047 rad/s

## Why This Matters

These are **dimensionally different** but often confused:

```python
from unifyt import Quantity

# FREQUENCY (Hz)
freq = Quantity(1800, 'rpm')  # Treats as frequency
print(freq.to('hertz'))  # 30 Hz ✅
print(freq.to('radian_per_second'))  # 30 rad/s (WRONG for rotation!)

# ANGULAR VELOCITY (rad/s)
omega = Quantity(1800, 'revolution_per_minute')  # Treats as angular velocity
print(omega.to('radian_per_second'))  # 188.5 rad/s ✅
print(omega.to('hertz'))  # 30 Hz (cycles, not radians!)
```

## When to Use Which

### Use `'rpm'` (Frequency) for:
- Vibration frequency
- Oscillation rate
- Cycle counting
- When you want Hz

```python
# Engine vibration
vibration = Quantity(3000, 'rpm')
print(vibration.to('hertz'))  # 50 Hz
```

### Use `'revolution_per_minute'` (Angular Velocity) for:
- Motor speed
- Wheel rotation
- Shaft speed
- When you want rad/s

```python
# Motor speed
motor_speed = Quantity(1800, 'revolution_per_minute')
print(motor_speed.to('radian_per_second'))  # 188.5 rad/s

# Calculate linear velocity
radius = Quantity(0.5, 'meter')
linear_vel = motor_speed.to('radian_per_second').magnitude * radius.magnitude
print(Quantity(linear_vel, 'meter/second'))  # 94.2 m/s
```

## Quick Reference

| Quantity | Value | Unit String | Converts To |
|----------|-------|-------------|-------------|
| Frequency | 1800 | `'rpm'` | 30 Hz |
| Angular Velocity | 1800 | `'revolution_per_minute'` | 188.5 rad/s |
| Angular Velocity | 1800 | `'rev_min'` | 188.5 rad/s |

## Conversion Formulas

### Frequency (rpm → Hz)
```
Hz = rpm / 60
```

### Angular Velocity (rev/min → rad/s)
```
rad/s = rev/min × (2π / 60) = rev/min × 0.10472
```

### Relationship
```
1 revolution = 2π radians
1 minute = 60 seconds

Therefore:
1 rev/min = 2π/60 rad/s ≈ 0.10472 rad/s
```

## Best Practice

**Always use the full unit name for clarity:**

```python
# ✅ CLEAR - Angular velocity
motor = Quantity(1800, 'revolution_per_minute')

# ⚠️ AMBIGUOUS - Could be frequency or angular velocity
motor = Quantity(1800, 'rpm')

# ✅ CLEAR - Frequency
vibration = Quantity(1800, 'rpm')  # When you explicitly want Hz
```

## Summary

- **`'rpm'`** = Frequency (Hz) - for cycles, oscillations
- **`'revolution_per_minute'`** or **`'rev_min'`** = Angular velocity (rad/s) - for rotation
- When in doubt, use the full name to avoid confusion
- Both are valid, but they convert differently!

---

**Note**: This is a common source of confusion in engineering. Unifyt handles both correctly, but you must choose the right unit string for your use case.
