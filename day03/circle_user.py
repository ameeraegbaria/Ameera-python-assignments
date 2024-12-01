# circle.py

import math
import argparse

# Set up the argument parser
parser = argparse.ArgumentParser(description="Calculate the area and circumference of a circle.")
parser.add_argument("radius", type=float, help="The radius of the circle")

# Parse the arguments
args = parser.parse_args()

# Retrieve the radius
radius = args.radius

# Calculate the area
area = math.pi * radius ** 2

# Calculate the circumference
circumference = 2 * math.pi * radius

# Print out the results
print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)
print("Done")
