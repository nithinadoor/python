import math

def area_of_circle(radius):
    area=radius**2*math.pi
    return area
radius=float(input("enter radius of circle"))
print("area is",area_of_circle(radius))