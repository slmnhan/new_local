import math
def distance_between_two_points(x1, y1, x2, y2):

# We know that the distance between two ponts is calculated by using the formula square root of  (x1-x1)^2 + (y2-y2)^2
#  so know iam going to return the mathemaitcal equasion of this by putiing values in this formula
    return math.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )
# i hope this function will calculate the distance between two points
#  Now let's run this function and see if it works?
#  there is a thing in python that before running of the code we run predictoin in our brain and that is what give the programmer confidence to run the code
print(distance_between_two_points(5, 3, 8, 7))
