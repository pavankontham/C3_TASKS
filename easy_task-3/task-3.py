def classify_color():
    red=int(input("Enter the RGB value of red: "))
    green=int(input("Enter the RGB value of green: "))
    blue=int(input("Enter the RGB value of blue: "))
    if red >= 200 and green <= 50 and blue <= 50:
        print("The flag is red.")
    elif red <= 50 and green <= 50 and blue >= 200:
        print("The flag is blue.")
    elif red <= 50 and green >= 200 and blue <= 50:
        print("The flag is green.")
    else:
        print("The flag is unknown.")

# Shri Ram uses the classify_color() function to help his friend find the flags.

classify_color()

# Shri Ram's friend is able to find the flags with Shri Ram's help.
