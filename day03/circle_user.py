# circle.py

#circle_user.py

# Run the script from the terminal: pass python file_name.py (for example, python circle_user.py) 

import math
import argparse

# Set up the argument parser
parser = argparse.ArgumentParser(description="Calculate the area and circumference of a circle.")
parser.add_argument("--radius", type=float, help="The radius of the circle")

# Parse the arguments
args = parser.parse_args()

# Prompt the user for radius if not provided as an argument
if args.radius is None:
    radius = float(input("Please enter the radius of the circle: "))
else:
    radius = args.radius

# Calculate the area
area = math.pi * radius ** 2

# Calculate the circumference
circumference = 2 * math.pi * radius

# Print out the results
print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)
print("Done")
