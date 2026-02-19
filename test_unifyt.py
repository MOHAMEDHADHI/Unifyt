from unifyt import Quantity

# Create measurements (value first, then unit)
distance = Quantity(100, 'meter')

# Convert it
distance_in_feet = distance.to('feet')

print(f"100 meters = {distance_in_feet.value} feet")

# Do some math
weight1 = Quantity(5, 'kilogram')
weight2 = Quantity(2000, 'gram')
total = weight1 + weight2

print(f"Total weight: {total}")
