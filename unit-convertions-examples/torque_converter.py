"""
Torque Conversion Examples
===========================

This module demonstrates torque unit conversions between SI and Imperial systems.

Units Covered:
- Newton-meter (Nm) - SI standard
- Foot-pound (ft-lb) - Imperial standard
- Inch-pound (in-lb) - Small fasteners
- Kilonewton-meter (kNm) - Large applications

Author: Unifyt Team
Date: 2025-01-27
"""

from unifyt import Quantity
import sys


def print_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)


def print_conversion_table(values, from_unit, to_units):
    """Print a conversion table."""
    print(f"\n{'Value':<15} " + " ".join([f"{u:<15}" for u in to_units]))
    print("-" * (15 + 15 * len(to_units)))
    
    for value in values:
        torque = Quantity(value, from_unit)
        row = f"{value:<15.1f} "
        for to_unit in to_units:
            converted = torque.to(to_unit)
            row += f"{converted.magnitude:<15.2f} "
        print(row)


def nm_to_imperial():
    """Convert Newton-meters to Imperial units."""
    print_header("Newton-Meter (Nm) to Imperial Conversions")
    
    print("\n--- Common Torque Values (Nm to ft-lb and in-lb) ---")
    
    nm_values = [5, 10, 20, 30, 50, 75, 100, 150, 200, 250, 300, 500, 1000]
    
    print(f"\n{'Nm':<12} {'ft-lb':<12} {'in-lb':<12} {'Application'}")
    print("-" * 70)
    
    applications = {
        5: "Small electronics screws",
        10: "Bicycle components",
        20: "Automotive sensors",
        30: "Motorcycle bolts",
        50: "Car wheel lugs (small)",
        75: "Car wheel lugs (medium)",
        100: "Car wheel lugs (large)",
        150: "Cylinder head bolts",
        200: "Crankshaft bolts",
        250: "Heavy machinery",
        300: "Industrial equipment",
        500: "Large machinery",
        1000: "Heavy industrial"
    }
    
    for nm in nm_values:
        torque_nm = Quantity(nm, 'Nm')
        torque_ftlb = torque_nm.to('foot_pound')
        torque_inlb = torque_nm.to('inch_pound')
        app = applications.get(nm, "")
        
        print(f"{nm:<12.0f} {torque_ftlb.magnitude:<12.1f} {torque_inlb.magnitude:<12.0f} {app}")


def ftlb_to_metric():
    """Convert Foot-pounds to Metric units."""
    print_header("Foot-Pound (ft-lb) to Metric Conversions")
    
    print("\n--- Common Torque Values (ft-lb to Nm) ---")
    
    ftlb_values = [5, 10, 15, 20, 25, 30, 40, 50, 75, 100, 150, 200, 300]
    
    print(f"\n{'ft-lb':<12} {'Nm':<12} {'kNm':<12} {'Application'}")
    print("-" * 70)
    
    applications = {
        5: "Small fasteners",
        10: "Spark plugs",
        15: "Oil drain plugs",
        20: "Brake calipers",
        25: "Suspension components",
        30: "Engine mounts",
        40: "Transmission bolts",
        50: "Axle nuts",
        75: "Wheel lugs (cars)",
        100: "Wheel lugs (trucks)",
        150: "Driveshaft bolts",
        200: "Heavy equipment",
        300: "Industrial machinery"
    }
    
    for ftlb in ftlb_values:
        torque_ftlb = Quantity(ftlb, 'ft_lb')
        torque_nm = torque_ftlb.to('Nm')
        torque_knm = torque_ftlb.to('kilonewton_meter')
        app = applications.get(ftlb, "")
        
        print(f"{ftlb:<12.0f} {torque_nm.magnitude:<12.1f} {torque_knm.magnitude:<12.4f} {app}")


def inlb_conversions():
    """Convert Inch-pounds to other units."""
    print_header("Inch-Pound (in-lb) Conversions")
    
    print("\n--- Small Fastener Torque Values (in-lb) ---")
    
    inlb_values = [5, 10, 15, 20, 30, 40, 50, 75, 100, 120, 150, 200]
    
    print(f"\n{'in-lb':<12} {'Nm':<12} {'ft-lb':<12} {'Application'}")
    print("-" * 70)
    
    applications = {
        5: "Tiny electronics",
        10: "Small electronics",
        15: "Circuit boards",
        20: "Computer components",
        30: "Instrument panels",
        40: "Light switches",
        50: "Electrical boxes",
        75: "Small brackets",
        100: "Medium brackets",
        120: "Thermostat screws",
        150: "Light fixtures",
        200: "Heavy brackets"
    }
    
    for inlb in inlb_values:
        torque_inlb = Quantity(inlb, 'in_lb')
        torque_nm = torque_inlb.to('Nm')
        torque_ftlb = torque_inlb.to('ft_lb')
        app = applications.get(inlb, "")
        
        print(f"{inlb:<12.0f} {torque_nm.magnitude:<12.2f} {torque_ftlb.magnitude:<12.2f} {app}")


def automotive_torque_specs():
    """Common automotive torque specifications."""
    print_header("Automotive Torque Specifications")
    
    print("\n--- Common Car Components (Typical Values) ---")
    
    specs = [
        ("Spark plugs", 20, "Nm"),
        ("Oil drain plug", 25, "Nm"),
        ("Oil filter", 15, "Nm"),
        ("Wheel lug nuts (small car)", 100, "Nm"),
        ("Wheel lug nuts (SUV/truck)", 140, "Nm"),
        ("Brake caliper bolts", 35, "Nm"),
        ("Suspension bolts", 80, "Nm"),
        ("Engine mount bolts", 50, "Nm"),
        ("Cylinder head bolts", 90, "Nm"),
        ("Connecting rod bolts", 45, "Nm"),
        ("Crankshaft bolt", 200, "Nm"),
    ]
    
    print(f"\n{'Component':<30} {'Nm':<12} {'ft-lb':<12} {'in-lb':<12}")
    print("-" * 75)
    
    for component, value, unit in specs:
        torque = Quantity(value, unit)
        nm = torque.to('Nm').magnitude
        ftlb = torque.to('ft_lb').magnitude
        inlb = torque.to('in_lb').magnitude
        
        print(f"{component:<30} {nm:<12.0f} {ftlb:<12.1f} {inlb:<12.0f}")


def bicycle_torque_specs():
    """Common bicycle torque specifications."""
    print_header("Bicycle Torque Specifications")
    
    print("\n--- Bicycle Components (Typical Values) ---")
    
    specs = [
        ("Handlebar clamp", 5, "Nm"),
        ("Stem bolts", 6, "Nm"),
        ("Brake lever clamp", 5, "Nm"),
        ("Brake caliper bolts", 8, "Nm"),
        ("Disc brake rotor", 6, "Nm"),
        ("Seat post clamp", 5, "Nm"),
        ("Seat rail clamp", 15, "Nm"),
        ("Pedals", 35, "Nm"),
        ("Crank arm bolts", 40, "Nm"),
        ("Bottom bracket", 50, "Nm"),
        ("Cassette lockring", 40, "Nm"),
        ("Thru-axle", 12, "Nm"),
    ]
    
    print(f"\n{'Component':<25} {'Nm':<10} {'ft-lb':<10} {'in-lb':<10}")
    print("-" * 60)
    
    for component, value, unit in specs:
        torque = Quantity(value, unit)
        nm = torque.to('Nm').magnitude
        ftlb = torque.to('ft_lb').magnitude
        inlb = torque.to('in_lb').magnitude
        
        print(f"{component:<25} {nm:<10.1f} {ftlb:<10.1f} {inlb:<10.0f}")


def industrial_torque():
    """Industrial and heavy machinery torque values."""
    print_header("Industrial & Heavy Machinery Torque")
    
    print("\n--- Large Torque Values (kNm) ---")
    
    values_knm = [0.5, 1, 2, 5, 10, 20, 50, 100]
    
    print(f"\n{'kNm':<12} {'Nm':<12} {'ft-lb':<12} {'Application'}")
    print("-" * 70)
    
    applications = {
        0.5: "Medium industrial bolts",
        1: "Large industrial bolts",
        2: "Heavy machinery",
        5: "Wind turbine bolts",
        10: "Ship propeller nuts",
        20: "Large crane bolts",
        50: "Mining equipment",
        100: "Massive industrial"
    }
    
    for knm in values_knm:
        torque_knm = Quantity(knm, 'kNm')
        torque_nm = torque_knm.to('Nm')
        torque_ftlb = torque_knm.to('ft_lb')
        app = applications.get(knm, "")
        
        print(f"{knm:<12.1f} {torque_nm.magnitude:<12.0f} {torque_ftlb.magnitude:<12.0f} {app}")


def torque_wrench_settings():
    """Torque wrench setting conversions."""
    print_header("Torque Wrench Setting Conversions")
    
    print("\n--- Converting Between Wrench Scales ---")
    print("Scenario: You have a torque spec in Nm but your wrench shows ft-lb")
    
    target_specs = [
        ("Wheel lug nuts", 110, "Nm"),
        ("Cylinder head", 85, "Nm"),
        ("Oil drain plug", 25, "Nm"),
        ("Spark plug", 20, "Nm"),
    ]
    
    print(f"\n{'Component':<20} {'Spec (Nm)':<15} {'Set Wrench To':<20}")
    print("-" * 60)
    
    for component, value, unit in target_specs:
        torque = Quantity(value, unit)
        ftlb = torque.to('ft_lb')
        print(f"{component:<20} {value:<15.0f} {ftlb.magnitude:.1f} ft-lb")
    
    print("\n--- Precision Torque (in-lb scale) ---")
    
    precision_specs = [
        ("Electronics", 8, "in_lb"),
        ("Instrument panel", 15, "in_lb"),
        ("Thermostat", 20, "in_lb"),
    ]
    
    print(f"\n{'Component':<20} {'Spec (in-lb)':<15} {'Equivalent (Nm)':<20}")
    print("-" * 60)
    
    for component, value, unit in precision_specs:
        torque = Quantity(value, unit)
        nm = torque.to('Nm')
        print(f"{component:<20} {value:<15.0f} {nm.magnitude:.2f} Nm")


def conversion_formulas():
    """Display conversion formulas and factors."""
    print_header("Torque Conversion Formulas & Factors")
    
    print("\n--- Conversion Factors ---")
    print("1 Nm = 0.7376 ft-lb")
    print("1 Nm = 8.851 in-lb")
    print("1 ft-lb = 1.3558 Nm")
    print("1 ft-lb = 12 in-lb")
    print("1 in-lb = 0.1130 Nm")
    print("1 kNm = 1000 Nm")
    
    print("\n--- Quick Conversion Examples ---")
    
    examples = [
        (50, "Nm", ["ft_lb", "in_lb"]),
        (100, "ft_lb", ["Nm", "in_lb"]),
        (200, "in_lb", ["Nm", "ft_lb"]),
        (5, "kNm", ["Nm", "ft_lb"]),
    ]
    
    for value, from_unit, to_units in examples:
        torque = Quantity(value, from_unit)
        print(f"\n{value} {from_unit}:")
        for to_unit in to_units:
            converted = torque.to(to_unit)
            print(f"  = {converted.magnitude:.2f} {to_unit}")


def interactive_converter():
    """Interactive torque converter."""
    print_header("Interactive Torque Converter")
    
    units = {
        '1': ('Nm', 'newton_meter'),
        '2': ('ft-lb', 'foot_pound'),
        '3': ('in-lb', 'inch_pound'),
        '4': ('kNm', 'kilonewton_meter'),
    }
    
    while True:
        print("\nSelect input unit:")
        print("  1. Newton-meter (Nm)")
        print("  2. Foot-pound (ft-lb)")
        print("  3. Inch-pound (in-lb)")
        print("  4. Kilonewton-meter (kNm)")
        print("  0. Exit")
        
        try:
            choice = input("\nEnter choice (0-4): ").strip()
            
            if choice == '0':
                print("\nGoodbye!")
                break
            
            if choice not in units:
                print("Invalid choice!")
                continue
            
            value = float(input(f"Enter torque value in {units[choice][0]}: "))
            torque = Quantity(value, units[choice][1])
            
            print(f"\n{value} {units[choice][0]} equals:")
            print(f"  {torque.to('Nm').magnitude:.2f} Nm")
            print(f"  {torque.to('foot_pound').magnitude:.2f} ft-lb")
            print(f"  {torque.to('inch_pound').magnitude:.2f} in-lb")
            print(f"  {torque.to('kilonewton_meter').magnitude:.4f} kNm")
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")


def main():
    """Main function to run all examples."""
    print("\n" + "=" * 80)
    print("  TORQUE CONVERSION EXAMPLES")
    print("  Unifyt Library - Complete Torque Unit Support")
    print("=" * 80)
    
    if len(sys.argv) > 1 and sys.argv[1] == '--interactive':
        interactive_converter()
    else:
        nm_to_imperial()
        ftlb_to_metric()
        inlb_conversions()
        automotive_torque_specs()
        bicycle_torque_specs()
        industrial_torque()
        torque_wrench_settings()
        conversion_formulas()
        
        print("\n" + "=" * 80)
        print("  TIP: Run with --interactive flag for interactive converter")
        print("  Example: python torque_converter.py --interactive")
        print("=" * 80)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
