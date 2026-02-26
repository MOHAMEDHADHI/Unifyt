"""
Test file for validating unifyt abbreviations and conversions.
This tests the package after pip install unifyt.
"""

from unifyt import Quantity

def test_time_conversions():
    """Test time unit conversions with various abbreviations."""
    print("=" * 60)
    print("TIME CONVERSIONS")
    print("=" * 60)
    
    # Standard abbreviations (these should work)
    test_cases = [
        ("10 second", "minute"),
        ("10 sec", "min"),
        ("60 s", "min"),  # 's' for second
        ("5 minute", "second"),
        ("5 min", "s"),
        ("1 hour", "minute"),
        ("1 hr", "min"),
        ("1 h", "s"),
        ("1 day", "hour"),
        ("1 d", "hr"),
    ]
    
    for value_unit, target_unit in test_cases:
        try:
            result = Quantity(value_unit, target_unit)
            print(f"✓ {value_unit:20s} → {target_unit:10s} = {result}")
        except Exception as e:
            print(f"✗ {value_unit:20s} → {target_unit:10s} = ERROR: {e}")
    print()

def test_length_conversions():
    """Test length unit conversions."""
    print("=" * 60)
    print("LENGTH CONVERSIONS")
    print("=" * 60)
    
    test_cases = [
        ("5 centimeter", "meter"),
        ("5 cm", "m"),
        ("100 meter", "kilometer"),
        ("100 m", "km"),
        ("1 kilometer", "meter"),
        ("1 km", "m"),
        ("12 inch", "centimeter"),
        ("12 in", "cm"),
        ("3 foot", "meter"),
        ("3 ft", "m"),
        ("1 mile", "kilometer"),
        ("1 mi", "km"),
    ]
    
    for value_unit, target_unit in test_cases:
        try:
            result = Quantity(value_unit, target_unit)
            print(f"✓ {value_unit:20s} → {target_unit:10s} = {result}")
        except Exception as e:
            print(f"✗ {value_unit:20s} → {target_unit:10s} = ERROR: {e}")
    print()

def test_mass_conversions():
    """Test mass unit conversions."""
    print("=" * 60)
    print("MASS CONVERSIONS")
    print("=" * 60)
    
    test_cases = [
        ("100 pound", "kilogram"),
        ("100 lb", "kg"),
        ("1 kilogram", "gram"),
        ("1 kg", "g"),
        ("1000 gram", "kilogram"),
        ("1000 g", "kg"),
        ("16 ounce", "pound"),
        ("16 oz", "lb"),
        ("1 ton", "kilogram"),
    ]
    
    for value_unit, target_unit in test_cases:
        try:
            result = Quantity(value_unit, target_unit)
            print(f"✓ {value_unit:20s} → {target_unit:10s} = {result}")
        except Exception as e:
            print(f"✗ {value_unit:20s} → {target_unit:10s} = ERROR: {e}")
    print()

def test_pressure_conversions():
    """Test pressure unit conversions."""
    print("=" * 60)
    print("PRESSURE CONVERSIONS")
    print("=" * 60)
    
    test_cases = [
        ("1 bar", "pascal"),
        ("1 bar", "Pa"),
        ("100 psi", "bar"),
        ("100 PSI", "bar"),
        ("1 atmosphere", "pascal"),
        ("1 atm", "Pa"),
        ("760 torr", "atm"),
        ("1 kilopascal", "pascal"),
        ("1 kPa", "Pa"),
    ]
    
    for value_unit, target_unit in test_cases:
        try:
            result = Quantity(value_unit, target_unit)
            print(f"✓ {value_unit:20s} → {target_unit:10s} = {result}")
        except Exception as e:
            print(f"✗ {value_unit:20s} → {target_unit:10s} = ERROR: {e}")
    print()

def test_temperature_conversions():
    """Test temperature unit conversions."""
    print("=" * 60)
    print("TEMPERATURE CONVERSIONS")
    print("=" * 60)
    
    test_cases = [
        ("0 celsius", "fahrenheit"),
        ("0 C", "F"),
        ("100 celsius", "kelvin"),
        ("100 C", "K"),
        ("32 fahrenheit", "celsius"),
        ("32 F", "C"),
        ("273.15 kelvin", "celsius"),
        ("273.15 K", "C"),
    ]
    
    for value_unit, target_unit in test_cases:
        try:
            result = Quantity(value_unit, target_unit)
            print(f"✓ {value_unit:20s} → {target_unit:10s} = {result}")
        except Exception as e:
            print(f"✗ {value_unit:20s} → {target_unit:10s} = ERROR: {e}")
    print()

def test_energy_conversions():
    """Test energy unit conversions."""
    print("=" * 60)
    print("ENERGY CONVERSIONS")
    print("=" * 60)
    
    test_cases = [
        ("1 kilowatt_hour", "joule"),
        ("1 kWh", "J"),
        ("1000 joule", "kilojoule"),
        ("1000 J", "kJ"),
        ("1 calorie", "joule"),
        ("1 cal", "J"),
        ("1 BTU", "joule"),
    ]
    
    for value_unit, target_unit in test_cases:
        try:
            result = Quantity(value_unit, target_unit)
            print(f"✓ {value_unit:20s} → {target_unit:10s} = {result}")
        except Exception as e:
            print(f"✗ {value_unit:20s} → {target_unit:10s} = ERROR: {e}")
    print()

def test_power_conversions():
    """Test power unit conversions."""
    print("=" * 60)
    print("POWER CONVERSIONS")
    print("=" * 60)
    
    test_cases = [
        ("1 kilowatt", "watt"),
        ("1 kW", "W"),
        ("1 horsepower", "watt"),
        ("1 hp", "W"),
        ("1000 watt", "kilowatt"),
        ("1000 W", "kW"),
    ]
    
    for value_unit, target_unit in test_cases:
        try:
            result = Quantity(value_unit, target_unit)
            print(f"✓ {value_unit:20s} → {target_unit:10s} = {result}")
        except Exception as e:
            print(f"✗ {value_unit:20s} → {target_unit:10s} = ERROR: {e}")
    print()

def test_speed_conversions():
    """Test speed/velocity unit conversions."""
    print("=" * 60)
    print("SPEED CONVERSIONS")
    print("=" * 60)
    
    test_cases = [
        ("100 kilometer/hour", "meter/second"),
        ("100 km/hr", "m/s"),
        ("60 mile/hour", "kilometer/hour"),
        ("60 mi/hr", "km/hr"),
        ("10 meter/second", "kilometer/hour"),
        ("10 m/s", "km/hr"),
    ]
    
    for value_unit, target_unit in test_cases:
        try:
            result = Quantity(value_unit, target_unit)
            print(f"✓ {value_unit:20s} → {target_unit:10s} = {result}")
        except Exception as e:
            print(f"✗ {value_unit:20s} → {target_unit:10s} = ERROR: {e}")
    print()

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("UNIFYT ABBREVIATION AND CONVERSION TEST SUITE")
    print("=" * 60 + "\n")
    
    test_time_conversions()
    test_length_conversions()
    test_mass_conversions()
    test_pressure_conversions()
    test_temperature_conversions()
    test_energy_conversions()
    test_power_conversions()
    test_speed_conversions()
    
    print("=" * 60)
    print("TEST SUITE COMPLETE")
    print("=" * 60)
