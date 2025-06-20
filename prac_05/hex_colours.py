"""
Create a program that allows you to look up hexadecimal colour codes
"""

COLOUR_TO_HEX = {"absolutezero": "#0048ba", "acidgreen": "#b0bf1a", "aliceblue": "#f0f8ff",
                 "alizarincrimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc",
                 "antiqueahite": "#faebd7", "apricot": "#fbceb1", "aqua": "#00ffff"}

get_hex = input("Enter a colour name: ").lower()

while get_hex != "":
    try:
        print(f"{COLOUR_TO_HEX[get_hex]}")
    except KeyError:
        print("Invalid state")
    get_hex = input("Enter a colour name: ").lower()

