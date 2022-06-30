""" Convert height (in feet and inches) to centimeters """
def height_to_centimeters(h_ft, h_inch):
    h_inch += h_ft * 12
    h_cm = h_inch * 2.54
    return h_cm


# input height in feet
h_ft = int(input("Feet: "))

# input height in inches
h_inch = int(input("Inches: "))

# printing result
print(f'Your height is {height_to_centimeters(h_ft, h_inch):0.2f} cm')

