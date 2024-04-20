# Information of the math for this assignment
# https://byui-cse.github.io/cse111-course/lesson01/approx_tire_vol.html 

import math

# Get the user input
width = float(input("Enter the width of the tire in mm (ex 205): "))
aspectRatio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# Math goes here
volume = (math.pi * width * aspectRatio (width * aspectRatio + 2540 * diameter))/ 10000000000

# Output the results
print(f"The approximate volume is {volume} liters.")
