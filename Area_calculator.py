print("=========================================\nWELCOME TO THE AREA CALCULATOR PROGRAM!📐\n=========================================")
shape = int(input('\nPlease select a shape to calculate the area:\n\n1. Circle\n2. Rectangle\n3. Triangle\n4. Square\n\nEnter the number corresponding to your choice: '))
if shape == 1:
    radius = float(input("\nEnter the radius of the circle: "))
    area = 3.14159 * radius ** 2
    print(f"\nThe area of the circle is: {area}")
elif shape == 2:
    length = float(input("\nEnter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"\nThe area of the rectangle is: {area:}")
elif shape == 3:
    base = float(input("\nEnter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"\nThe area of the triangle is: {area}")
elif shape == 4:
    side = float(input("\nEnter the side length of the square: "))
    area = side ** 2
    print(f"\nThe area of the square is: {area}")
else:
    print("\nInvalid choice. Please select a valid shape.")