"""
Angular Velocity Conversion Examples
=====================================

This module demonstrates angular velocity and rotational speed conversions.

Units Covered:
- RPM (revolutions per minute) - Common motor speed
- RPS (revolutions per second)
- rad/s (radians per second) - SI standard
- deg/s (degrees per second)

IMPORTANT NOTE:
- Use 'rpm' for frequency (Hz) - cycles per minute
- Use 'revolution_per_minute' for angular velocity (rad/s) - rotational speed

Author: Unifyt Team
Date: 2025-01-27
"""

from unifyt import Quantity
import sys
import math


def print_header(title):
    """Print a formatted section header."""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)


def rpm_conversions():
    """Demonstrate RPM conversions to other angular velocity units."""
    print_header("RPM (Revolutions Per Minute) Conversions")
    
    print("\n--- Common Motor Speeds (RPM to rad/s, deg/s, RPS) ---")
    
    rpm_values = [60, 120, 300, 600, 900, 1200, 1500, 1800, 3000, 3600, 7200]
    
    print(f"\n{'RPM':<10} {'rad/s':<12} {'deg/s':<12} {'RPS':<12} {'Application'}")
    print("-" * 75)
    
    applications = {
        60: "Slow mixer",
        120: "Ceiling fan low",
        300: "Washing machine",
        600: "Blender low",
        900: "Drill low speed",
        1200: "Fan medium",
        1500: "Pump motor",
        1800: "AC motor (60Hz)",
        3000: "Power tool",
        3600: "High-speed fan",
        7200: "Grinder"
    }
    
    for rpm in rpm_values:
        # Use revolution_per_minute for angular velocity
        angular_vel = Quantity(rpm, 'revolution_per_minute')
        rad_s = angular_vel.to('radian_per_second')
        deg_s = angular_vel.to('degree_per_second')
        rps = angular_vel.to('revolution_per_second')
        
        app = applications.get(rpm, "")
        print(f"{rpm:<10} {rad_s.magnitude:<12.2f} {deg_s.magnitude:<12.1f} {rps.magnitude:<12.2f} {app}")


def motor_specifications():
    """Show typical motor specifications with angular velocity."""
    print_header("Motor Specifications - Angular Velocity Examples")
    
    motors = [
        ("Small DC Motor", 12000, "Hobby projects, toys"),
        ("Ceiling Fan", 300, "Residential cooling"),
        ("Industrial Fan", 1750, "HVAC systems"),
        ("AC Induction Motor (60Hz, 4-pole)", 1800, "General purpose"),
        ("AC Induction Motor (60Hz, 2-pole)", 3600, "High speed applications"),
        ("Servo Motor", 3000, "Robotics, CNC"),
        ("Stepper Motor", 600, "3D printers, positioning"),
        ("Centrifugal Pump", 1450, "Water pumping"),
        ("Compressor Motor", 1200, "Air compression"),
        ("Grinder", 10000, "Metalworking")
    ]
    
    print(f"\n{'Motor Type':<35} {'RPM':<10} {'rad/s':<12} {'Application'}")
    print("-" * 85)
    
    for motor_type, rpm, application in motors:
        angular_vel = Quantity(rpm, 'revolution_per_minute')
        rad_s = angular_vel.to('radian_per_second')
        print(f"{motor_type:<35} {rpm:<10} {rad_s.magnitude:<12.2f} {application}")


def rotational_calculations():
    """Demonstrate rotational mechanics calculations."""
    print_header("Rotational Mechanics Calculations")
    
    print("\n--- Linear Speed from Angular Velocity ---")
    print("Formula: v = ω × r (linear velocity = angular velocity × radius)")
    
    # Example: Wheel rotating at 300 RPM with 0.5m radius
    rpm = 300
    radius = Quantity(0.5, 'meter')
    
    angular_vel = Quantity(rpm, 'revolution_per_minute')
    omega = angular_vel.to('radian_per_second')
    
    # Linear velocity
    linear_vel = omega.magnitude * radius.magnitude  # m/s
    linear_vel_q = Quantity(linear_vel, 'meter_per_second')
    
    print(f"\nWheel rotating at {rpm} RPM with radius {radius}:")
    print(f"  Angular velocity (ω): {omega.magnitude:.2f} rad/s")
    print(f"  Linear velocity (v): {linear_vel_q}")
    print(f"  Linear velocity: {linear_vel_q.to('kilometer_per_hour'):.2f}")
    print(f"  Linear velocity: {linear_vel_q.to('mile_per_hour'):.2f}")
    
    print("\n--- Centripetal Acceleration ---")
    print("Formula: a = ω² × r")
    
    accel = omega.magnitude ** 2 * radius.magnitude  # m/s²
    accel_q = Quantity(accel, 'meter_per_second^2')
    
    print(f"  Centripetal acceleration: {accel_q.magnitude:.2f} m/s²")
    print(f"  In terms of g: {accel_q.magnitude / 9.81:.2f} g")


def frequency_vs_angular_velocity():
    """Clarify the difference between frequency (rpm) and angular velocity (revolution_per_minute)."""
    print_header("RPM: Frequency vs Angular Velocity")
    
    print("\nUNIFYT has TWO different 'RPM' units:")
    print("\n1. 'rpm' - Frequency unit (cycles per minute)")
    print("   - Dimension: 1/time (Hz)")
    print("   - Use for: Rotation frequency, cycles, oscillations")
    print("   - Converts to: Hz, kHz")
    
    print("\n2. 'revolution_per_minute' - Angular velocity unit")
    print("   - Dimension: angle/time (rad/s)")
    print("   - Use for: Rotational speed, angular motion")
    print("   - Converts to: rad/s, deg/s, revolution_per_second")
    
    print("\n--- Example Comparison ---")
    rpm_value = 1800
    
    # Frequency
    freq = Quantity(rpm_value, 'rpm')
    print(f"\nAs FREQUENCY: {rpm_value} rpm")
    print(f"  → {freq.to('hertz'):.1f}")
    print(f"  → {freq.to('kilohertz'):.4f}")
    
    # Angular velocity
    ang_vel = Quantity(rpm_value, 'revolution_per_minute')
    print(f"\nAs ANGULAR VELOCITY: {rpm_value} revolution_per_minute")
    print(f"  → {ang_vel.to('radian_per_second'):.2f}")
    print(f"  → {ang_vel.to('degree_per_second'):.1f}")
    
    print("\n--- When to Use Which ---")
    print("Use 'rpm' (frequency):")
    print("  - Motor nameplate frequency rating")
    print("  - Vibration analysis")
    print("  - Oscillation rates")
    
    print("\nUse 'revolution_per_minute' (angular velocity):")
    print("  - Calculating linear velocity from rotation")
    print("  - Torque and power calculations")
    print("  - Rotational kinematics")


def power_from_torque_speed():
    """Calculate power from torque and rotational speed."""
    print_header("Power Calculation from Torque and Speed")
    
    print("\nFormula: P = τ × ω")
    print("Where:")
    print("  P = Power (Watts)")
    print("  τ = Torque (Newton-meters)")
    print("  ω = Angular velocity (radians/second)")
    
    print("\n--- Example: Motor Power Calculation ---")
    
    examples = [
        (50, 1500, "Small motor"),
        (100, 1800, "Medium motor"),
        (200, 3000, "Large motor"),
        (500, 1200, "Industrial motor")
    ]
    
    print(f"\n{'Torque (Nm)':<15} {'Speed (RPM)':<15} {'Power (W)':<15} {'Power (HP)':<15} {'Application'}")
    print("-" * 85)
    
    for torque_nm, speed_rpm, application in examples:
        torque = Quantity(torque_nm, 'newton_meter')
        angular_vel = Quantity(speed_rpm, 'revolution_per_minute')
        omega = angular_vel.to('radian_per_second')
        
        # Power = Torque × Angular velocity
        power_watts = torque.magnitude * omega.magnitude
        power = Quantity(power_watts, 'watt')
        power_hp = power.to('horsepower')
        
        print(f"{torque_nm:<15} {speed_rpm:<15} {power_watts:<15.1f} {power_hp.magnitude:<15.2f} {application}")


def interactive_mode():
    """Interactive conversion mode."""
    print_header("Interactive Angular Velocity Converter")
    
    print("\nAvailable units:")
    print("  1. revolution_per_minute (RPM)")
    print("  2. revolution_per_second (RPS)")
    print("  3. radian_per_second (rad/s)")
    print("  4. degree_per_second (deg/s)")
    
    unit_map = {
        '1': 'revolution_per_minute',
        '2': 'revolution_per_second',
        '3': 'radian_per_second',
        '4': 'degree_per_second'
    }
    
    try:
        value = float(input("\nEnter value: "))
        print("\nSelect unit:")
        for key, unit in unit_map.items():
            print(f"  {key}. {unit}")
        
        choice = input("Choice (1-4): ").strip()
        
        if choice not in unit_map:
            print("Invalid choice!")
            return
        
        from_unit = unit_map[choice]
        angular_vel = Quantity(value, from_unit)
        
        print(f"\n{value} {from_unit} equals:")
        for unit in unit_map.values():
            if unit != from_unit:
                converted = angular_vel.to(unit)
                print(f"  → {converted}")
        
        # Also show frequency if applicable
        print("\nAs frequency:")
        freq_rpm = value if from_unit == 'revolution_per_minute' else angular_vel.to('revolution_per_minute').magnitude
        freq = Quantity(freq_rpm, 'rpm')
        print(f"  → {freq.to('hertz'):.4f}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nExiting...")


def main():
    """Main function to run all examples."""
    if len(sys.argv) > 1 and sys.argv[1] == '--interactive':
        interactive_mode()
    else:
        print("=" * 80)
        print("  ANGULAR VELOCITY CONVERSION EXAMPLES")
        print("  Using Unifyt Library")
        print("=" * 80)
        
        rpm_conversions()
        motor_specifications()
        rotational_calculations()
        frequency_vs_angular_velocity()
        power_from_torque_speed()
        
        print("\n" + "=" * 80)
        print("  Run with --interactive flag for interactive mode")
        print("=" * 80)


if __name__ == "__main__":
    main()
