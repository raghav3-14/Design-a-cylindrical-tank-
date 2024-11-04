import math

def tank_design(volume, diameter):
    """
    Calculate the height and surface area of a cylindrical water tank.

    Parameters:
    volume (float): Volume of the tank in cubic meters.
    diameter (float): Diameter of the tank in meters.

    Returns:
    tuple: Height of the tank in meters, surface area in square meters.
    """
    # Calculate the radius of the tank
    radius = diameter / 2
    
    # Calculate the height of the tank
    height = volume / (math.pi * radius ** 2)
    
    # Calculate the surface area of the tank (2πrh + 2πr²)
    surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2
    
    return height, surface_area

# Manual input from the user
try:
    volume = float(input("Enter the volume of the tank (in cubic meters): "))
    diameter = float(input("Enter the diameter of the tank (in meters): "))
    
    height, surface_area = tank_design(volume, diameter)
    print(f"The height of the tank is: {round(height, 2)} meters")
    print(f"The surface area of the tank is: {round(surface_area, 2)} square meters")
except ValueError:
    print("Please enter valid numerical values.")
