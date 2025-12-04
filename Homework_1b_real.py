from math import pi

print("Python can do your Geometry calculations for you!")
print("")
radius=input("Enter circle radius: ")

radius = float(radius)
circumference = 2 * pi * radius
area = pi * radius * radius

print("Circumference of the circle is ", circumference)
print("Rounded to an easier number is %.2f" %circumference)
print("")
print("Area of the circle is ", area)
print("Rounded to and easier number is %.2f" %area)
print("")

length = float(input("Enter rectangle length: "))
height = float(input("Enter rectangle height: "))

area = length * height
perimeter = length * 2 + height * 2

print("Perimeter of the rectangle is ", perimeter)
print("Rounded to an easier number is %.2f" %perimeter)
print("")
print("Area of the rectangle is ", area)
print("Rounded to an easier number is %.2f" %area)
print("")
print("CONGRATULATIONS! Geometry homework done thanks to Python!")