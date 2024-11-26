# circle_user.py

import argparse

# Set up the argument parser
parser = argparse.ArgumentParser(description="Calculate the area and circumference of a rectangle.")

# Add arguments for width and length
parser.add_argument("--width", type=float, required=True, help="The width of the rectangle")
parser.add_argument("--length", type=float, required=True, help="The length of the rectangle")

# Parse the command-line arguments
args = parser.parse_args()

# Get the width and length from the parsed arguments
width = args.width
length = args.length

# Calculate the area
area = width * length

# Calculate the circumference
circumference = 2 * (width + length)

# Print out the results
print("The area of the rectangle is:", area)
print("The circumference of the rectangle is:", circumference)
