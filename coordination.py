import math

def distance_between_two_points(x1, y1, x2, y2):
    # The distance between two points is calculated using the formula:
    # √[(x2 - x1)^2 + (y2 - y1)^2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Let's test the function with an example
print(distance_between_two_points(5, 3, 8, 7))