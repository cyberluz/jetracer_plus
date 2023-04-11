# steering_command_argument.py
# Author: George Gorospe
 
# Learning how to use python to control the JetRacer
# This implementation includes an input argument parser

import jetracer
from jetracer.nvidia_racecar import NvidiaRacecar

import argparse


car = NvidiaRacecar()

parser = argparse.ArgumentParser()

parser.add_argument('--value', type=float, required=True)

args = parser.parse_args()

car.steering = args.value
