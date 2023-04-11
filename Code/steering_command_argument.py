# steering_command_argument.py
# Author: George Gorospe
 
# Learning how to use python to control the JetRacer
# This implementation includes an input argument parser

# Importing required libraries
# note "jetracer.nvidia_racecar" library is only on robot
from jetracer.nvidia_racecar import NvidiaRacecar
import argparse

# Instantiate the racecar module as an object for Object Oriented Programming (OOP)
car = NvidiaRacecar()

# Instantiate the parser
parser = argparse.ArgumentParser()

#Adding an argument to the parser
parser.add_argument('--value', type=float, required=True)# Parser for servo command

# Parse the command line arguments
args = parser.parse_args()

# Modify the steering parameter to automatically change steering angle on the JetRacer
car.steering = args.value

# formerly: car.steering= 0.3 or whatever, but now a dynamic args.value contains the 
# value fed from the data stream
print = ("The command servo value is: ", args.value )

#example of a command line argument (CLA) two parts:flag (1 or 2 dashes), value
#  python3 steering_command_argument.py --value 0.3
