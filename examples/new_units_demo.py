"""Demonstration of newly added units in Unifyt.

This example showcases:
1. Wire gauge conversions (AWG, SWG, BWG)
2. Torque units
3. GSM (grams per square meter) for paper/fabric
4. Mass flow rates
5. Volumetric flow rates
6. Angular velocity
"""

from unifyt import Quantity, wire_gauge
import numpy as np


print("=" * 70)
print("UNIFYT - NEW UNITS DEMONSTRATION")
print("=" * 70)


# ============================================================================
# 1. WIRE GAUGE CONVERSIONS
# ============================================================================
print("\n" + "=" * 70)
print("1. WIRE GAUGE CONVERSIONS (AWG, SWG, BWG)")
print("=" * 70)

print("\n--- American Wire Gauge (AWG) ---")
# Convert AWG to diameter
awg_14 = wire_gauge.awg_to_diameter(14)
print(f"AWG 14 wire diameter: {awg_14}")
print(f"  → In inches: {awg_14.to('inch'):.4f}")

awg_12 = wire_gauge.awg_to_diameter(12)
print(f"\nAWG 12 wire diameter: {awg_12}")
print(f"  → In inches: {awg_12.to('inch'):.4f}")

# Convert diameter back to AWG
diameter = Quantity(1.6, 'millimeter')
closest_awg = wire_gauge.diameter_to_awg(diameter)
print(f"\nWire with {diameter} diameter is closest to AWG {closest_awg}")

print("\n--- Standard Wire Gauge (SWG) ---")
swg_14 = wire_gauge.swg_to_diameter(14)
print(f"SWG 14 wire diameter: {swg_14}")
print(f"  → In inches: {swg_14.to('inch'):.4f}")

print("\n--- Birmingham Wire Gauge (BWG) ---")
bwg_14 = wire_gauge.bwg_to_diameter(14)
print(f"BWG 14 wire diameter: {bwg_14}")
print(f"  → In inches: {bwg_14.to('inch'):.4f}")

print("\n--- Comparison of Gauge 14 across standards ---")
print(f"AWG 14: {awg_14}")
print(f"SWG 14: {swg_14}")
print(f"BWG 14: {bwg_14}")


# ============================================================================
# 2. TORQUE UNITS
# ============================================================================
print("\n" + "=" * 70)
print("2. TORQUE UNITS")
print("=" * 70)

# Using new torque shortcuts
torque_nm = Quantity(100, 'newton_meter')  # or 'Nm'
print(f"\nEngine torque: {torque_nm}")
print(f"  → In kNm: {torque_nm.to('kilonewton_meter'):.2f}")

# Imperial torque units
torque_ftlb = Quantity(75, 'foot_pound')  # or 'ft_lb'
print(f"\nBolt torque: {torque_ftlb}")
print(f"  → In Nm: {torque_ftlb.to('newton_meter'):.2f}")

torque_inlb = Quantity(120, 'inch_pound')  # or 'in_lb'
print(f"\nSmall fastener torque: {torque_inlb}")
print(f"  → In Nm: {torque_inlb.to('newton_meter'):.2f}")

# Torque calculations
force = Quantity(50, 'newton')
lever_arm = Quantity(2, 'meter')
calculated_torque = force * lever_arm
print(f"\nCalculated torque: {force} × {lever_arm} = {calculated_torque}")


# ============================================================================
# 3. GSM (GRAMS PER SQUARE METER) - Paper/Fabric Weight
# ============================================================================
print("\n" + "=" * 70)
print("3. GSM - PAPER AND FABRIC WEIGHT")
print("=" * 70)

# Paper weights
copy_paper = Quantity(80, 'gsm')  # Standard copy paper
print(f"\nCopy paper: {copy_paper}")
print(f"  → In kg/m²: {copy_paper.to('kilogram/meter^2'):.3f}")

cardstock = Quantity(200, 'gsm')  # Heavy cardstock
print(f"\nCardstock: {cardstock}")
print(f"  → In kg/m²: {cardstock.to('kilogram/meter^2'):.3f}")

# Calculate total weight for a ream (500 sheets of A4)
a4_area = Quantity(0.0625, 'meter^2')  # A4 = 210mm × 297mm
sheets = 500
total_weight = copy_paper * a4_area * sheets
print(f"\nWeight of 500 sheets of 80 GSM A4 paper:")
print(f"  → {total_weight.to('kilogram'):.2f}")


# ============================================================================
# 4. MASS FLOW RATES
# ============================================================================
print("\n" + "=" * 70)
print("4. MASS FLOW RATES")
print("=" * 70)

# Industrial process flow
flow_kg_hr = Quantity(1000, 'kilogram_per_hour')  # or 'kg_hr'
print(f"\nProcess flow rate: {flow_kg_hr}")
print(f"  → In kg/s: {flow_kg_hr.to('kilogram_per_second'):.4f}")
print(f"  → In ton/hr: {flow_kg_hr.to('ton_per_hour'):.2f}")

# Convert to volumetric flow (assuming water density)
# First convert to kg/s, then divide by density
flow_kg_s = flow_kg_hr.to('kilogram_per_second')
water_density = Quantity(1000, 'kilogram/meter^3')
volumetric_flow_m3s = flow_kg_s.magnitude / water_density.magnitude
volumetric_flow = Quantity(volumetric_flow_m3s, 'cubic_meter_per_second')
print(f"  → Volumetric flow (water): {volumetric_flow.to('liter_per_minute'):.2f}")

# Conveyor belt material flow
material_flow = Quantity(5, 'ton_per_hour')  # or 'tph'
print(f"\nConveyor material flow: {material_flow}")
print(f"  → In kg/s: {material_flow.to('kilogram_per_second'):.2f}")


# ============================================================================
# 5. VOLUMETRIC FLOW RATES (Additional)
# ============================================================================
print("\n" + "=" * 70)
print("5. VOLUMETRIC FLOW RATES")
print("=" * 70)

# HVAC air flow
air_flow_cfm = Quantity(500, 'cubic_foot_per_minute')  # or 'cfm'
print(f"\nHVAC air flow: {air_flow_cfm}")
print(f"  → In m³/h: {air_flow_cfm.to('cubic_meter_per_hour'):.2f}")
print(f"  → In L/s: {air_flow_cfm.to('liter_per_second'):.2f}")

# Pump flow rate
pump_flow = Quantity(100, 'liter_per_minute')
print(f"\nPump flow rate: {pump_flow}")
print(f"  → In m³/h: {pump_flow.to('cubic_meter_per_hour'):.2f}")
print(f"  → In gpm: {pump_flow.to('gallon_per_minute'):.2f}")


# ============================================================================
# 6. ANGULAR VELOCITY
# ============================================================================
print("\n" + "=" * 70)
print("6. ANGULAR VELOCITY")
print("=" * 70)

# Motor speed
motor_rpm = Quantity(1800, 'revolution_per_minute')  # Use full name for angular velocity
print(f"\nMotor speed: {motor_rpm}")
print(f"  → In rad/s: {motor_rpm.to('radian_per_second'):.2f}")
print(f"  → In rev/s: {motor_rpm.to('revolution_per_second'):.2f}")

# Angular velocity in rad/s
angular_vel = Quantity(10, 'radian_per_second')
print(f"\nAngular velocity: {angular_vel}")
print(f"  → In rpm (rev/min): {angular_vel.to('revolution_per_minute'):.2f}")
print(f"  → In deg/s: {angular_vel.to('degree_per_second'):.2f}")

# Calculate linear velocity from angular velocity
radius = Quantity(0.5, 'meter')
linear_vel = angular_vel * radius
print(f"\nLinear velocity at radius {radius}:")
print(f"  → {linear_vel.to('meter/second'):.2f}")


# ============================================================================
# 7. COMBINED EXAMPLE - Industrial Application
# ============================================================================
print("\n" + "=" * 70)
print("7. COMBINED EXAMPLE - INDUSTRIAL PUMP SYSTEM")
print("=" * 70)

print("\n--- Pump Specifications ---")
pump_power = Quantity(5, 'kilowatt')
pump_flow = Quantity(200, 'liter_per_minute')
pump_pressure = Quantity(5, 'bar')
motor_speed = Quantity(1450, 'revolution_per_minute')  # Use full name for angular velocity

print(f"Power: {pump_power}")
print(f"Flow rate: {pump_flow}")
print(f"  → {pump_flow.to('cubic_meter_per_hour'):.2f}")
print(f"  → {pump_flow.to('gallon_per_minute'):.2f}")
print(f"Pressure: {pump_pressure}")
print(f"  → {pump_pressure.to('psi'):.2f}")
print(f"Motor speed: {motor_speed}")
print(f"  → {motor_speed.to('radian_per_second'):.2f}")

# Calculate hydraulic power
# Power = Flow × Pressure
# Convert to base units for calculation
flow_m3s = pump_flow.to('cubic_meter_per_second')
pressure_pa = pump_pressure.to('pascal')
hydraulic_power_watts = flow_m3s.magnitude * pressure_pa.magnitude
hydraulic_power = Quantity(hydraulic_power_watts, 'watt')
print(f"\nHydraulic power: {hydraulic_power.to('kilowatt'):.2f}")

# Calculate efficiency
efficiency_ratio = hydraulic_power.magnitude / pump_power.to('watt').magnitude
efficiency = efficiency_ratio * 100
print(f"Pump efficiency: {efficiency:.1f}%")


# ============================================================================
# 8. ARRAY OPERATIONS WITH NEW UNITS
# ============================================================================
print("\n" + "=" * 70)
print("8. ARRAY OPERATIONS WITH NEW UNITS")
print("=" * 70)

# Multiple wire gauges
awg_gauges = [10, 12, 14, 16, 18, 20]
diameters = [wire_gauge.awg_to_diameter(g) for g in awg_gauges]

print("\nAWG wire diameter comparison:")
for gauge, dia in zip(awg_gauges, diameters):
    print(f"  AWG {gauge:2d}: {dia} = {dia.to('inch'):.4f}")

# Flow rate measurements over time
times = np.array([0, 1, 2, 3, 4, 5])  # hours
flows = Quantity(np.array([100, 105, 98, 102, 99, 101]), 'liter_per_minute')

print(f"\nFlow rate measurements:")
print(f"  Mean: {Quantity(np.mean(flows.magnitude), 'liter_per_minute')}")
print(f"  Std dev: {Quantity(np.std(flows.magnitude), 'liter_per_minute'):.2f}")


print("\n" + "=" * 70)
print("DEMONSTRATION COMPLETE")
print("=" * 70)
print("\nNew units successfully integrated into Unifyt!")
print("Total new unit categories added: 6")
print("  - Wire gauges (AWG, SWG, BWG)")
print("  - Torque units (Nm, ft-lb, in-lb)")
print("  - GSM (paper/fabric weight)")
print("  - Mass flow rates (kg/hr, tph, etc.)")
print("  - Volumetric flow rates (cfm, m³/h, etc.)")
print("  - Angular velocity (rpm, rad/s, etc.)")
