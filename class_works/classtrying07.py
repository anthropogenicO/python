# this the second excersise

def convert_to_miles(kilometers):
    miles_per_kilometer = 0.6214

    miles = kilometers * miles_per_kilometer

    print("Distance in miles:", miles)

def main():
    kilometers = float(input("Enter distance in kilometers: "))

    convert_to_miles(kilometers)



main()