# Learning how to python to control the jetracer
# This script features a command line parser

#Import the agparse library to manage command line arguments
import argparse

#Create the parser
parser = argparse.ArgumentParser()
parser.add_argument('--value', type=float, required=True) # Parser for servo copmmand
args = parser.parse.args()

#Importing required libraries
# from jetracer.nvidia_racercar Import NividiaRacecar

# Instantiate the object for Object Oriented Programming (OOP)
#car=NividiaRacecar()

#car.steering = 0.3
print = ("The commanded servo value is: ", args.value)