def hypot():
    """
    This function calculates the hypotenuse of a right triangle given the lengths of the other two sides.
    """
    import math
    a = float(input("Enter length of side a: "))
    b = float(input("Enter length of side b: "))
    c = math.sqrt(a**2 + b**2)
    print(f"The length of the hypotenuse is: {c}")