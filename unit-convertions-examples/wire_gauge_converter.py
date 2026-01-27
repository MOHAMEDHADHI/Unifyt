"""
Wire Gauge Conversion Examples
===============================

This module demonstrates wire gauge conversions between AWG, SWG, BWG standards
and physical diameter measurements.

Standards Covered:
- AWG (American Wire Gauge) - North American electrical standard
- SWG (Standard Wire Gauge) - British Imperial standard
- BWG (Birmingham Wire Gauge) - Steel wire and tubing standard

Author: Unifyt Team
Date: 2025-01-27
"""

from unifyt import Quantity, wire_gauge
import sys


def print_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)


def print_conversion(label, value, conversions):
    """Print a value with multiple conversions."""
    print(f"\n{label}: {value}")
    for unit, desc in conversions:
        converted = value.to(unit) if isinstance(value, Quantity) else value
        print(f"  → {desc}: {converted}")


def awg_conversions():
    """Demonstrate AWG (American Wire Gauge) conversions."""
    print_header("AWG (American Wire Gauge) Conversions")
    
    print("\n--- Common AWG Wire Sizes ---")
    common_gauges = [10, 12, 14, 16, 18, 20, 22, 24]
    
    print(f"\n{'Gauge':<8} {'Diameter (mm)':<15} {'Diameter (inch)':<15} {'Application'}")
    print("-" * 70)
    
    applications = {
        10: "Heavy appliances, AC units",
        12: "Kitchen appliances, outlets",
        14: "Lighting circuits, outlets",
        16: "Extension cords, doorbells",
        18: "Low-voltage lighting",
        20: "Thermostat wiring",
        22: "Alarm systems, intercoms",
        24: "Phone lines, data cables"
    }
    
    for gauge in common_gauges:
        dia_mm = wire_gauge.awg_to_diameter(gauge)
        dia_in = wire_gauge.awg_to_diameter(gauge, 'inch')
        app = applications.get(gauge, "General purpose")
        print(f"AWG {gauge:<4} {dia_mm.magnitude:<15.3f} {dia_in.magnitude:<15.4f} {app}")
    
    print("\n--- Special AWG Gauges ---")
    special_gauges = ['0000', '000', '00', '0']
    
    for gauge in special_gauges:
        dia_mm = wire_gauge.awg_to_diameter(gauge)
        dia_in = wire_gauge.awg_to_diameter(gauge, 'inch')
        print(f"AWG {gauge:<4} = {dia_mm} = {dia_in}")
    
    print("\n--- Reverse Lookup: Diameter to AWG ---")
    test_diameters = [
        Quantity(1.0, 'mm'),
        Quantity(1.5, 'mm'),
        Quantity(2.0, 'mm'),
        Quantity(0.05, 'inch'),
        Quantity(0.1, 'inch'),
    ]
    
    for diameter in test_diameters:
        gauge = wire_gauge.diameter_to_awg(diameter)
        actual_dia = wire_gauge.awg_to_diameter(gauge)
        print(f"{diameter} → Closest: AWG {gauge} (actual: {actual_dia})")


def swg_conversions():
    """Demonstrate SWG (Standard Wire Gauge) conversions."""
    print_header("SWG (Standard Wire Gauge) Conversions")
    
    print("\n--- Common SWG Wire Sizes ---")
    common_gauges = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    
    print(f"\n{'Gauge':<8} {'Diameter (mm)':<15} {'Diameter (inch)':<15}")
    print("-" * 50)
    
    for gauge in common_gauges:
        dia_mm = wire_gauge.swg_to_diameter(gauge)
        dia_in = wire_gauge.swg_to_diameter(gauge, 'inch')
        print(f"SWG {gauge:<4} {dia_mm.magnitude:<15.3f} {dia_in.magnitude:<15.4f}")
    
    print("\n--- Fine Wire Gauges (SWG) ---")
    fine_gauges = [32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
    
    print(f"\n{'Gauge':<8} {'Diameter (mm)':<15} {'Diameter (μm)':<15}")
    print("-" * 50)
    
    for gauge in fine_gauges:
        dia_mm = wire_gauge.swg_to_diameter(gauge)
        dia_um = wire_gauge.swg_to_diameter(gauge, 'micrometer')
        print(f"SWG {gauge:<4} {dia_mm.magnitude:<15.3f} {dia_um.magnitude:<15.1f}")


def bwg_conversions():
    """Demonstrate BWG (Birmingham Wire Gauge) conversions."""
    print_header("BWG (Birmingham Wire Gauge) Conversions")
    
    print("\n--- Common BWG Sizes (Tubing & Needles) ---")
    common_gauges = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
    
    print(f"\n{'Gauge':<8} {'Diameter (mm)':<15} {'Diameter (inch)':<15} {'Application'}")
    print("-" * 70)
    
    applications = {
        10: "Heavy tubing",
        12: "Industrial tubing",
        14: "Standard tubing",
        16: "Light tubing",
        18: "Thin tubing",
        20: "Medical tubing",
        22: "Hypodermic needles",
        24: "Fine needles",
        26: "Very fine needles",
        28: "Ultra-fine needles",
        30: "Micro needles"
    }
    
    for gauge in common_gauges:
        dia_mm = wire_gauge.bwg_to_diameter(gauge)
        dia_in = wire_gauge.bwg_to_diameter(gauge, 'inch')
        app = applications.get(gauge, "General purpose")
        print(f"BWG {gauge:<4} {dia_mm.magnitude:<15.3f} {dia_in.magnitude:<15.4f} {app}")


def compare_standards():
    """Compare the same gauge number across different standards."""
    print_header("Comparison: Same Gauge Number, Different Standards")
    
    print("\nNote: The same gauge number means different diameters in different standards!")
    
    test_gauges = [10, 12, 14, 16, 18, 20, 22, 24]
    
    print(f"\n{'Gauge':<8} {'AWG (mm)':<12} {'SWG (mm)':<12} {'BWG (mm)':<12} {'Difference'}")
    print("-" * 70)
    
    for gauge in test_gauges:
        awg_dia = wire_gauge.awg_to_diameter(gauge).magnitude
        swg_dia = wire_gauge.swg_to_diameter(gauge).magnitude
        bwg_dia = wire_gauge.bwg_to_diameter(gauge).magnitude
        
        max_dia = max(awg_dia, swg_dia, bwg_dia)
        min_dia = min(awg_dia, swg_dia, bwg_dia)
        diff_percent = ((max_dia - min_dia) / min_dia) * 100
        
        print(f"{gauge:<8} {awg_dia:<12.3f} {swg_dia:<12.3f} {bwg_dia:<12.3f} {diff_percent:>6.1f}%")


def practical_examples():
    """Practical wire gauge conversion examples."""
    print_header("Practical Wire Gauge Examples")
    
    print("\n--- Example 1: Selecting Wire for 15A Circuit ---")
    print("Requirement: Wire for 15 ampere circuit (residential)")
    print("Recommended: AWG 14 or larger")
    
    awg_14 = wire_gauge.awg_to_diameter(14)
    awg_12 = wire_gauge.awg_to_diameter(12)
    
    print(f"\nAWG 14: {awg_14} = {awg_14.to('inch')}")
    print(f"AWG 12: {awg_12} = {awg_12.to('inch')} (safer, lower resistance)")
    
    print("\n--- Example 2: Replacing British Wire with American ---")
    print("Have: SWG 16 wire")
    print("Need: Equivalent AWG gauge")
    
    swg_16_dia = wire_gauge.swg_to_diameter(16)
    awg_equiv = wire_gauge.diameter_to_awg(swg_16_dia)
    awg_dia = wire_gauge.awg_to_diameter(awg_equiv)
    
    print(f"\nSWG 16 diameter: {swg_16_dia}")
    print(f"Closest AWG: {awg_equiv}")
    print(f"AWG {awg_equiv} diameter: {awg_dia}")
    print(f"Difference: {abs(swg_16_dia.magnitude - awg_dia.magnitude):.3f} mm")
    
    print("\n--- Example 3: Medical Needle Selection ---")
    print("Common hypodermic needle gauges (BWG):")
    
    needle_gauges = {
        18: "Blood donation, IV",
        20: "Blood transfusion",
        22: "Intramuscular injection",
        25: "Subcutaneous injection",
        27: "Insulin injection",
        30: "Intradermal injection"
    }
    
    for gauge, use in needle_gauges.items():
        dia = wire_gauge.bwg_to_diameter(gauge)
        print(f"  {gauge}G: {dia} - {use}")
    
    print("\n--- Example 4: Wire Cross-Sectional Area ---")
    print("Calculate cross-sectional area for current capacity:")
    
    gauge = 12
    diameter = wire_gauge.awg_to_diameter(gauge)
    radius = diameter / 2
    
    # Area = π × r²
    import math
    area_mm2 = math.pi * (radius.magnitude ** 2)
    area_circular_mils = (diameter.to('inch').magnitude * 1000) ** 2
    
    print(f"\nAWG {gauge}:")
    print(f"  Diameter: {diameter}")
    print(f"  Radius: {radius}")
    print(f"  Cross-sectional area: {area_mm2:.3f} mm²")
    print(f"  Cross-sectional area: {area_circular_mils:.0f} circular mils")


def interactive_mode():
    """Interactive wire gauge converter."""
    print_header("Interactive Wire Gauge Converter")
    
    while True:
        print("\nOptions:")
        print("  1. AWG to diameter")
        print("  2. SWG to diameter")
        print("  3. BWG to diameter")
        print("  4. Diameter to AWG")
        print("  5. Diameter to SWG")
        print("  6. Diameter to BWG")
        print("  7. Compare all standards")
        print("  0. Exit")
        
        try:
            choice = input("\nEnter choice (0-7): ").strip()
            
            if choice == '0':
                print("\nGoodbye!")
                break
            
            elif choice in ['1', '2', '3']:
                gauge_input = input("Enter gauge number: ").strip()
                
                # Handle special AWG gauges
                if choice == '1' and gauge_input in ['0000', '000', '00', '0']:
                    gauge = gauge_input
                else:
                    gauge = int(gauge_input)
                
                unit = input("Output unit (mm/inch/um) [mm]: ").strip() or 'millimeter'
                unit_map = {'mm': 'millimeter', 'inch': 'inch', 'in': 'inch', 'um': 'micrometer'}
                unit = unit_map.get(unit, unit)
                
                if choice == '1':
                    dia = wire_gauge.awg_to_diameter(gauge, unit)
                    print(f"\nAWG {gauge} = {dia}")
                elif choice == '2':
                    dia = wire_gauge.swg_to_diameter(gauge, unit)
                    print(f"\nSWG {gauge} = {dia}")
                else:
                    dia = wire_gauge.bwg_to_diameter(gauge, unit)
                    print(f"\nBWG {gauge} = {dia}")
            
            elif choice in ['4', '5', '6']:
                value = float(input("Enter diameter value: "))
                unit = input("Unit (mm/inch/um) [mm]: ").strip() or 'millimeter'
                unit_map = {'mm': 'millimeter', 'inch': 'inch', 'in': 'inch', 'um': 'micrometer'}
                unit = unit_map.get(unit, unit)
                
                diameter = Quantity(value, unit)
                
                if choice == '4':
                    gauge = wire_gauge.diameter_to_awg(diameter)
                    actual = wire_gauge.awg_to_diameter(gauge)
                    print(f"\n{diameter} → AWG {gauge}")
                    print(f"Actual AWG {gauge} diameter: {actual}")
                elif choice == '5':
                    gauge = wire_gauge.diameter_to_swg(diameter)
                    actual = wire_gauge.swg_to_diameter(gauge)
                    print(f"\n{diameter} → SWG {gauge}")
                    print(f"Actual SWG {gauge} diameter: {actual}")
                else:
                    gauge = wire_gauge.diameter_to_bwg(diameter)
                    actual = wire_gauge.bwg_to_diameter(gauge)
                    print(f"\n{diameter} → BWG {gauge}")
                    print(f"Actual BWG {gauge} diameter: {actual}")
            
            elif choice == '7':
                gauge = int(input("Enter gauge number: "))
                
                try:
                    awg = wire_gauge.awg_to_diameter(gauge)
                    print(f"\nAWG {gauge}: {awg} = {awg.to('inch')}")
                except:
                    print(f"\nAWG {gauge}: Not available")
                
                try:
                    swg = wire_gauge.swg_to_diameter(gauge)
                    print(f"SWG {gauge}: {swg} = {swg.to('inch')}")
                except:
                    print(f"SWG {gauge}: Not available")
                
                try:
                    bwg = wire_gauge.bwg_to_diameter(gauge)
                    print(f"BWG {gauge}: {bwg} = {bwg.to('inch')}")
                except:
                    print(f"BWG {gauge}: Not available")
            
            else:
                print("Invalid choice!")
        
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {e}")


def main():
    """Main function to run all examples."""
    print("\n" + "=" * 80)
    print("  WIRE GAUGE CONVERSION EXAMPLES")
    print("  Unifyt Library - Complete Wire Gauge Support")
    print("=" * 80)
    
    if len(sys.argv) > 1 and sys.argv[1] == '--interactive':
        interactive_mode()
    else:
        awg_conversions()
        swg_conversions()
        bwg_conversions()
        compare_standards()
        practical_examples()
        
        print("\n" + "=" * 80)
        print("  TIP: Run with --interactive flag for interactive converter")
        print("  Example: python wire_gauge_converter.py --interactive")
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
