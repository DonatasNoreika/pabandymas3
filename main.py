number = float(input("Enter a float number: "))

ndig = int(input("Enter ndigits: "))

if ndig == 0:
    print(f"Your rounded number is: {int(round(number, ndig))}")
else:
    print(f"Your rounded number is: {round(number, ndig)}")
