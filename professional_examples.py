"""
Professional Examples for Unifyt
Demonstrates correct abbreviation usage for industry professionals
"""

from unifyt import Quantity

print("=" * 80)
print("UNIFYT - PROFESSIONAL EXAMPLES")
print("=" * 80)
print()

# ============================================================================
# TIME CONVERSIONS - CORRECT ABBREVIATIONS
# ============================================================================
print("TIME CONVERSIONS")
print("-" * 80)
print("✓ CORRECT: Use 's' for second, 'min' for minute, 'h' or 'hr' for hour")
print()

# Correct examples
print("Seconds to minutes:")
print(f"  60 s → min     = {Quantity('60 s', 'min')}")
print(f"  120 sec → min  = {Quantity('120 sec', 'min')}")
print()

print("Minutes to seconds:")
print(f"  5 min → s      = {Quantity('5 min', 's')}")
print(f"  10 minute → s  = {Quantity('10 minute', 's')}")
print()

print("Hours to minutes:")
print(f"  2 h → min      = {Quantity('2 h', 'min')}")
print(f"  1.5 hr → min   = {Quantity('1.5 hr', 'min')}")
print()

print("❌ COMMON MISTAKE: Using 'm' for minute")
print("  'm' means METER (length), not minute!")
print("  Use 'min' for minute")
print()

# ============================================================================
# AEROSPACE ENGINEERING
# ============================================================================
print("=" * 80)
print("AEROSPACE ENGINEERING")
print("-" * 80)

print("Speed conversions:")
print(f"  500 knot → km/hr = {Quantity('500 knot', 'km/hr')}")
print(f"  100 km/hr → m/s  = {Quantity('100 km/hr', 'm/s')}")
print(f"  60 mi/hr → km/hr = {Quantity('60 mi/hr', 'km/hr')}")
print()

print("Altitude/Distance:")
print(f"  35000 ft → m     = {Quantity('35000 ft', 'm')}")
print(f"  10 km → ft       = {Quantity('10 km', 'ft')}")
print()

print("Pressure (cabin pressure, etc.):")
print(f"  14.7 psi → bar   = {Quantity('14.7 psi', 'bar')}")
print(f"  1 atm → Pa       = {Quantity('1 atm', 'Pa')}")
print()

# ============================================================================
# HVAC/MECHANICAL ENGINEERING
# ============================================================================
print("=" * 80)
print("HVAC/MECHANICAL ENGINEERING")
print("-" * 80)

print("Flow rates:")
print(f"  100 cfm → m3_min = {Quantity('100 cfm', 'm3_min')}")
print(f"  50 L_min → gpm   = {Quantity('50 L_min', 'gpm')}")
print()

print("Pressure:")
print(f"  2 bar → psi      = {Quantity('2 bar', 'psi')}")
print(f"  100 kPa → psi    = {Quantity('100 kPa', 'psi')}")
print()

print("Power:")
print(f"  5 kW → hp        = {Quantity('5 kW', 'hp')}")
print(f"  10 hp → kW       = {Quantity('10 hp', 'kW')}")
print()

# ============================================================================
# ELECTRICAL ENGINEERING
# ============================================================================
print("=" * 80)
print("ELECTRICAL ENGINEERING")
print("-" * 80)

print("Power:")
print(f"  5 kW → W         = {Quantity('5 kW', 'W')}")
print(f"  1000 W → kW      = {Quantity('1000 W', 'kW')}")
print(f"  1 hp → W         = {Quantity('1 hp', 'W')}")
print()

print("Voltage:")
print(f"  230 V → kV       = {Quantity('230 V', 'kV')}")
print(f"  11 kV → V        = {Quantity('11 kV', 'V')}")
print()

print("Energy:")
print(f"  1 kWh → J        = {Quantity('1 kWh', 'J')}")
print(f"  3600 kJ → kWh    = {Quantity('3600 kJ', 'kWh')}")
print()

# ============================================================================
# OIL & GAS INDUSTRY
# ============================================================================
print("=" * 80)
print("OIL & GAS INDUSTRY")
print("-" * 80)

print("Pressure:")
print(f"  1000 psi → bar   = {Quantity('1000 psi', 'bar')}")
print(f"  50 bar → MPa     = {Quantity('50 bar', 'MPa')}")
print(f"  5000 psi → MPa   = {Quantity('5000 psi', 'MPa')}")
print()

print("Flow rate:")
print(f"  100 gpm → L_min  = {Quantity('100 gpm', 'L_min')}")
print(f"  500 L_min → gpm  = {Quantity('500 L_min', 'gpm')}")
print()

print("Volume:")
print(f"  1000 gal → L     = {Quantity('1000 gallon', 'liter')}")
print(f"  100 L → gal      = {Quantity('100 liter', 'gallon')}")
print()

# ============================================================================
# CIVIL ENGINEERING
# ============================================================================
print("=" * 80)
print("CIVIL ENGINEERING")
print("-" * 80)

print("Length/Distance:")
print(f"  100 m → ft       = {Quantity('100 m', 'ft')}")
print(f"  1 km → mi        = {Quantity('1 km', 'mi')}")
print(f"  50 ft → m        = {Quantity('50 ft', 'm')}")
print()

print("Force:")
print(f"  1000 N → kN      = {Quantity('1000 N', 'kN')}")
print(f"  100 lbf → N      = {Quantity('100 lbf', 'N')}")
print()

print("Pressure/Stress:")
print(f"  1 MPa → psi      = {Quantity('1 MPa', 'psi')}")
print(f"  5000 psi → MPa   = {Quantity('5000 psi', 'MPa')}")
print()

# ============================================================================
# AUTOMOTIVE ENGINEERING
# ============================================================================
print("=" * 80)
print("AUTOMOTIVE ENGINEERING")
print("-" * 80)

print("Speed:")
print(f"  100 km/hr → mi/hr = {Quantity('100 km/hr', 'mi/hr')}")
print(f"  60 mi/hr → m/s    = {Quantity('60 mi/hr', 'm/s')}")
print()

print("Torque:")
print(f"  100 Nm → ft_lb    = {Quantity('100 Nm', 'ft_lb')}")
print(f"  50 ft_lb → Nm     = {Quantity('50 ft_lb', 'Nm')}")
print()

print("Engine RPM to rad/s:")
print(f"  3000 rpm → rad_s  = {Quantity('3000 revolution_per_minute', 'radian_per_second')}")
print(f"  6000 rpm → rad_s  = {Quantity('6000 revolution_per_minute', 'radian_per_second')}")
print()

print("Tire Pressure:")
print(f"  32 psi → bar      = {Quantity('32 psi', 'bar')}")
print(f"  2.2 bar → psi     = {Quantity('2.2 bar', 'psi')}")
print()

# ============================================================================
# SUMMARY
# ============================================================================
print("=" * 80)
print("KEY TAKEAWAYS")
print("=" * 80)
print()
print("✓ Time units:")
print("  - second: 's' or 'sec'")
print("  - minute: 'min' (NOT 'm'!)")
print("  - hour: 'h' or 'hr'")
print()
print("✓ Length units:")
print("  - meter: 'm'")
print("  - kilometer: 'km'")
print("  - centimeter: 'cm'")
print()
print("✓ Always check dimensions:")
print("  - Time units convert to time units")
print("  - Length units convert to length units")
print("  - Cannot mix dimensions!")
print()
print("✓ Use standard abbreviations:")
print("  - Refer to ABBREVIATION_GUIDE.md")
print("  - When in doubt, use full names")
print()
print("=" * 80)
