#lets do the class excersie now



def getkilometers():
    kilometers = float(input("Enter the distance in kilometers: "))
    return kilometers


def showmiles(kilometers):
    miles = kilometers * 0.6214
    print(f"{kilometers:.2f} kilometers is equal to {miles:.2f} miles.")


def main():
    distancekilometers = getkilometers()
    print(showmiles(distancekilometers))

    main()