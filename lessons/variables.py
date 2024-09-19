# Declaration of a variable syntax:
# <name>: <type> = <value>
# students: int = 300
# message: str = “Howdy!”

# Update a variable:
# <name> = <new value>
# students = 325
# message = “See ya!”


def less_than_ten(num: int) -> None:
    """Tell me if num is less than 10"""
    dub: int = num * 2
    dub = dub = dub - 1
    print(dub)
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("Have a nice day!")


less_than_ten(num=5)


def get_weather_report(weather: str = input("What is the weather?")) -> str:
    """Tells people what to do in case of rainy, cold, or hot weather"""
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()
