"""
Flow Rate Conversion Examples
==============================

This module demonstrates flow rate conversions for both mass and volumetric flow.

Units Covered:
Mass Flow:
- kg/s, kg/min, kg/hr, ton/hr (tph)
- lb/s, lb/min, lb/hr

Volumetric Flow:
- m³/s, m³/min, m³/hr
- L/s, L/min (lpm), L/hr
- cfm (cubic feet per minute), cfs
- gpm (gallons per minute)

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


def mass_flow_conversions():
    """Demonstrate mass flow rate conversions."""
    print_header("Mass Flow Rate Conversions")
    
    print("\n--- Common Mass Flow Values (kg/hr to other units) ---")
    
    kg_hr_values = [100, 500, 1000, 2000, 5000, 10000, 20000, 50000]
    
    print(f"\n{'kg/hr':<12} {'kg/s':<12} {'kg/min':<12} {'tph':<12} {'lb/hr':<12}")
    print("-" * 70)
    
    for kg_hr in kg_hr_values:
        flow = Quantity(kg_hr, 'kg_hr')
        kg_s = flow.to('kilogram_per_second')
        kg_min = flow.to('kilogram_per_minute')
        tph = flow.to('ton_per_hour')
        lb_hr = flow.to('pound_per_hour')
        
        print(f"{kg_hr:<12.0f} {kg_s.magnitude:<12.3f} {kg_min.magnitude:<12.1f} "
              f"{tph.magnitude:<12.2f} {lb_hr.magnitude:<12.0f}")


def volumetric_flow_conversions():
    """Demonstrate volumetric flow rate conversions."""
    print_header("Volumetric Flow Rate Conversions")
    
    print("\n--- Common Volumetric Flow Values (L/min to other units) ---")
    
    lpm_values = [10, 50, 100, 200, 500, 1000, 2000, 5000]
    
    print(f"\n{'L/min':<12} {'L/s':<12} {'m³/hr':<12} {'gpm':<12} {'cfm':<12}")
    print("-" * 70)
    
    for lpm in lpm_values:
        flow = Quantity(lpm, 'liter_per_minute')
        l_s = flow.to('liter_per_second')
        m3_hr = flow.to('cubic_meter_per_hour')
        gpm = flow.to('gallon_per_minute')
        cfm = flow.to('cubic_foot_per_minute')
        
        print(f"{lpm:<12.0f} {l_s.magnitude:<12.2f} {m3_hr.magnitude:<12.2f} "
              f"{gpm.magnitude:<12.2f} {cfm.magnitude:<12.2f}")


def hvac_applications():
    """HVAC and air flow applications."""
    print_header("HVAC & Air Flow Applications")
    
    print("\n--- Common HVAC Air Flow Rates (CFM) ---")
    
    hvac_specs = [
        ("Bathroom exhaust fan", 50, "cfm"),
        ("Kitchen range hood", 300, "cfm"),
        ("Whole house fan", 1000, "cfm"),
        ("Small AC unit (1 ton)", 400, "cfm"),
        ("Medium AC unit (3 ton)", 1200, "cfm"),
        ("Large AC unit (5 ton)", 2000, "cfm"),
        ("Commercial HVAC", 5000, "cfm"),
        ("Industrial ventilation", 10000, "cfm"),
    ]
    
    print(f"\n{'Application':<30} {'CFM':<12} {'m³/hr':<12} {'L/s':<12}")
    print("-" * 70)
    
    for app, value, unit in hvac_specs:
        flow = Quantity(value, unit)
        cfm = flow.to('cfm').magnitude
        m3_hr = flow.to('cubic_meter_per_hour').magnitude
        l_s = flow.to('liter_per_second').magnitude
        
        print(f"{app:<30} {cfm:<12.0f} {m3_hr:<12.1f} {l_s:<12.1f}")


def pump_applications():
    """Pump flow rate applications."""
    print_header("Pump Flow Rate Applications")
    
    print("\n--- Common Pump Flow Rates (GPM) ---")
    
    pump_specs = [
        ("Sump pump", 30, "gpm"),
        ("Pool pump (small)", 50, "gpm"),
        ("Pool pump (large)", 100, "gpm"),
        ("Irrigation pump", 150, "gpm"),
        ("Fire pump (residential)", 250, "gpm"),
        ("Industrial pump", 500, "gpm"),
        ("Municipal water", 1000, "gpm"),
        ("Large industrial", 5000, "gpm"),
    ]
    
    print(f"\n{'Application':<30} {'GPM':<12} {'L/min':<12} {'m³/hr':<12}")
    print("-" * 70)
    
    for app, value, unit in pump_specs:
        flow = Quantity(value, unit)
        gpm = flow.to('gpm').magnitude
        lpm = flow.to('liter_per_minute').magnitude
        m3_hr = flow.to('cubic_meter_per_hour').magnitude
        
        print(f"{app:<30} {gpm:<12.0f} {lpm:<12.1f} {m3_hr:<12.2f}")


def industrial_process_flow():
    """Industrial process flow rates."""
    print_header("Industrial Process Flow Rates")
    
    print("\n--- Mass Flow in Industrial Processes ---")
    
    processes = [
        ("Chemical reactor feed", 500, "kg_hr"),
        ("Polymer extrusion", 1000, "kg_hr"),
        ("Food processing", 2000, "kg_hr"),
        ("Cement production", 50, "tph"),
        ("Coal conveyor", 100, "tph"),
        ("Mining operation", 500, "tph"),
        ("Steel mill", 1000, "tph"),
    ]
    
    print(f"\n{'Process':<30} {'Input':<15} {'kg/s':<12} {'lb/hr':<12}")
    print("-" * 75)
    
    for process, value, unit in processes:
        flow = Quantity(value, unit)
        kg_s = flow.to('kilogram_per_second').magnitude
        lb_hr = flow.to('pound_per_hour').magnitude
        
        print(f"{process:<30} {value:>8.0f} {unit:<6} {kg_s:<12.2f} {lb_hr:<12.0f}")


def water_flow_calculations():
    """Water flow calculations and conversions."""
    print_header("Water Flow Calculations")
    
    print("\n--- Converting Between Mass and Volumetric Flow (Water) ---")
    print("Assumption: Water density = 1000 kg/m³ at 4°C")
    
    # Mass flow to volumetric flow
    print("\nMass Flow → Volumetric Flow:")
    mass_flows = [100, 500, 1000, 5000, 10000]  # kg/hr
    
    print(f"\n{'Mass Flow':<20} {'Volumetric Flow':<30}")
    print("-" * 55)
    
    for mass_flow_value in mass_flows:
        mass_flow = Quantity(mass_flow_value, 'kg_hr')
        # For water: 1 kg/hr = 1 L/hr (approximately)
        vol_flow_lhr = mass_flow_value  # L/hr
        vol_flow = Quantity(vol_flow_lhr, 'liter_per_hour')
        
        print(f"{mass_flow_value:>8.0f} kg/hr        = {vol_flow.to('liter_per_minute').magnitude:>8.2f} L/min "
              f"= {vol_flow.to('gallon_per_minute').magnitude:>6.2f} gpm")
    
    # Volumetric flow to mass flow
    print("\nVolumetric Flow → Mass Flow:")
    vol_flows = [10, 50, 100, 500, 1000]  # L/min
    
    print(f"\n{'Volumetric Flow':<20} {'Mass Flow (Water)':<30}")
    print("-" * 55)
    
    for vol_flow_value in vol_flows:
        vol_flow = Quantity(vol_flow_value, 'liter_per_minute')
        # For water: 1 L/min ≈ 1 kg/min
        mass_flow_kgmin = vol_flow_value
        mass_flow = Quantity(mass_flow_kgmin, 'kilogram_per_minute')
        
        print(f"{vol_flow_value:>8.0f} L/min        = {mass_flow.to('kilogram_per_hour').magnitude:>8.0f} kg/hr "
              f"= {mass_flow.to('ton_per_hour').magnitude:>6.3f} tph")


def pipe_sizing_flow_rates():
    """Flow rates for pipe sizing."""
    print_header("Pipe Sizing Flow Rates")
    
    print("\n--- Typical Flow Velocities in Pipes ---")
    print("Common pipe sizes with typical flow rates")
    
    pipe_data = [
        ("1/2 inch", 5, "gpm", "Residential water"),
        ("3/4 inch", 10, "gpm", "Residential water"),
        ("1 inch", 20, "gpm", "Residential/small commercial"),
        ("2 inch", 80, "gpm", "Commercial water"),
        ("3 inch", 180, "gpm", "Commercial/industrial"),
        ("4 inch", 320, "gpm", "Industrial water"),
        ("6 inch", 720, "gpm", "Large industrial"),
        ("8 inch", 1280, "gpm", "Municipal water"),
    ]
    
    print(f"\n{'Pipe Size':<15} {'Flow (GPM)':<12} {'L/min':<12} {'m³/hr':<12} {'Application'}")
    print("-" * 80)
    
    for pipe_size, flow_value, unit, application in pipe_data:
        flow = Quantity(flow_value, unit)
        gpm = flow.to('gpm').magnitude
        lpm = flow.to('liter_per_minute').magnitude
        m3_hr = flow.to('cubic_meter_per_hour').magnitude
        
        print(f"{pipe_size:<15} {gpm:<12.0f} {lpm:<12.1f} {m3_hr:<12.2f} {application}")


def conveyor_belt_flow():
    """Conveyor belt material flow rates."""
    print_header("Conveyor Belt Material Flow")
    
    print("\n--- Material Handling Flow Rates ---")
    
    materials = [
        ("Sand/gravel", 50, "tph", "Small operation"),
        ("Coal", 100, "tph", "Medium mine"),
        ("Iron ore", 500, "tph", "Large mine"),
        ("Grain", 20, "tph", "Grain elevator"),
        ("Cement", 80, "tph", "Cement plant"),
        ("Aggregate", 200, "tph", "Quarry"),
    ]
    
    print(f"\n{'Material':<15} {'tph':<10} {'kg/s':<12} {'kg/hr':<12} {'Application'}")
    print("-" * 75)
    
    for material, value, unit, application in materials:
        flow = Quantity(value, unit)
        tph = flow.to('tph').magnitude
        kg_s = flow.to('kilogram_per_second').magnitude
        kg_hr = flow.to('kilogram_per_hour').magnitude
        
        print(f"{material:<15} {tph:<10.0f} {kg_s:<12.2f} {kg_hr:<12.0f} {application}")


def conversion_formulas():
    """Display conversion formulas."""
    print_header("Flow Rate Conversion Formulas")
    
    print("\n--- Mass Flow Conversions ---")
    print("1 kg/s = 60 kg/min = 3600 kg/hr")
    print("1 tph = 1000 kg/hr = 0.2778 kg/s")
    print("1 kg/hr = 2.205 lb/hr")
    
    print("\n--- Volumetric Flow Conversions ---")
    print("1 m³/s = 60 m³/min = 3600 m³/hr")
    print("1 L/min = 0.01667 L/s = 60 L/hr")
    print("1 cfm = 0.4719 L/s = 28.32 L/min")
    print("1 gpm = 3.785 L/min = 0.06309 L/s")
    print("1 m³/hr = 16.67 L/min = 4.403 gpm")
    
    print("\n--- Water Flow (Mass ↔ Volume) ---")
    print("For water at 4°C (density = 1000 kg/m³):")
    print("1 kg/s = 1 L/s = 60 L/min")
    print("1 kg/hr = 1 L/hr = 0.01667 L/min")
    print("1 tph = 1000 L/hr = 16.67 L/min")


def interactive_converter():
    """Interactive flow rate converter."""
    print_header("Interactive Flow Rate Converter")
    
    print("\nSelect flow type:")
    print("  1. Mass Flow")
    print("  2. Volumetric Flow")
    
    try:
        flow_type = input("\nEnter choice (1-2): ").strip()
        
        if flow_type == '1':
            # Mass flow
            units = {
                '1': ('kg/s', 'kilogram_per_second'),
                '2': ('kg/min', 'kilogram_per_minute'),
                '3': ('kg/hr', 'kilogram_per_hour'),
                '4': ('tph', 'ton_per_hour'),
                '5': ('lb/hr', 'pound_per_hour'),
            }
            
            print("\nSelect input unit:")
            print("  1. kg/s")
            print("  2. kg/min")
            print("  3. kg/hr")
            print("  4. tph (ton per hour)")
            print("  5. lb/hr")
            
            choice = input("\nEnter choice (1-5): ").strip()
            
            if choice in units:
                value = float(input(f"Enter flow rate in {units[choice][0]}: "))
                flow = Quantity(value, units[choice][1])
                
                print(f"\n{value} {units[choice][0]} equals:")
                print(f"  {flow.to('kilogram_per_second').magnitude:.4f} kg/s")
                print(f"  {flow.to('kilogram_per_minute').magnitude:.2f} kg/min")
                print(f"  {flow.to('kilogram_per_hour').magnitude:.1f} kg/hr")
                print(f"  {flow.to('ton_per_hour').magnitude:.4f} tph")
                print(f"  {flow.to('pound_per_hour').magnitude:.1f} lb/hr")
        
        elif flow_type == '2':
            # Volumetric flow
            units = {
                '1': ('L/min', 'liter_per_minute'),
                '2': ('L/s', 'liter_per_second'),
                '3': ('m³/hr', 'cubic_meter_per_hour'),
                '4': ('gpm', 'gallon_per_minute'),
                '5': ('cfm', 'cubic_foot_per_minute'),
            }
            
            print("\nSelect input unit:")
            print("  1. L/min")
            print("  2. L/s")
            print("  3. m³/hr")
            print("  4. gpm (gallons per minute)")
            print("  5. cfm (cubic feet per minute)")
            
            choice = input("\nEnter choice (1-5): ").strip()
            
            if choice in units:
                value = float(input(f"Enter flow rate in {units[choice][0]}: "))
                flow = Quantity(value, units[choice][1])
                
                print(f"\n{value} {units[choice][0]} equals:")
                print(f"  {flow.to('liter_per_second').magnitude:.2f} L/s")
                print(f"  {flow.to('liter_per_minute').magnitude:.2f} L/min")
                print(f"  {flow.to('cubic_meter_per_hour').magnitude:.2f} m³/hr")
                print(f"  {flow.to('gallon_per_minute').magnitude:.2f} gpm")
                print(f"  {flow.to('cubic_foot_per_minute').magnitude:.2f} cfm")
    
    except Exception as e:
        print(f"\nError: {e}")


def main():
    """Main function to run all examples."""
    print("\n" + "=" * 80)
    print("  FLOW RATE CONVERSION EXAMPLES")
    print("  Unifyt Library - Mass & Volumetric Flow Support")
    print("=" * 80)
    
    if len(sys.argv) > 1 and sys.argv[1] == '--interactive':
        interactive_converter()
    else:
        mass_flow_conversions()
        volumetric_flow_conversions()
        hvac_applications()
        pump_applications()
        industrial_process_flow()
        water_flow_calculations()
        pipe_sizing_flow_rates()
        conveyor_belt_flow()
        conversion_formulas()
        
        print("\n" + "=" * 80)
        print("  TIP: Run with --interactive flag for interactive converter")
        print("  Example: python flow_rate_converter.py --interactive")
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
