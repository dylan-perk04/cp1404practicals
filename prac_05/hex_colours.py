"""
CP1404 Practical
Program to display hex-code of specified colour
"""

COLOUR_TO_HEX_CODE = {
    "absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff", "alizarin crimson": "#e32636",
    "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc", "apricot": "#fbceb1", "aqua": "#00ffff", "army "
                           "green": "#4b5320"}

print(COLOUR_TO_HEX_CODE)

colour = input("Enter colour: ").lower()
while colour != "":
    try:
        print(f"The hex code for {colour} is {COLOUR_TO_HEX_CODE[colour]}")
    except KeyError:
        print("Invalid colour")
    colour = input("Enter colour: ").lower()
