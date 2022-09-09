import argparse     # import argparse library to Parse the Arguments for calculating the Volume of a Cylinder
import math         # import math library 

# create the parser

parser = argparse.ArgumentParser(Description = "Calculate the volume of a Cylinder")    #
parser.add_argument("-r", "--radius", type=int, help="Radius of the Cylinder")          #
parser.add_argument("-H", "--height", type=int, help="Height of the Cylinder")          #
args = parser.parse_args()              # create args object and getting parser object info


# Creating the function to calculate the volume of the cylinder
def cylinder_volume(radius, height):
    vol = (math.pi) * (radius ** 2) * (height)
    return vol