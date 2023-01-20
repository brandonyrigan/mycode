#!/usr/bin/env python3

def main():
    willExit = "y"
    while willExit != "n":
        char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk): ").capitalize()

        char_stat = input("What statistic do you want to know about? (real name, powers, archenemy): ").lower()

        marvelchars= {
            "Starlord":
            {"real name": "peter quill",
            "powers": "dance moves",
            "archenemy": "Thanos"},

            "Mystique":
            {"real name": "raven darkholme",
            "powers": "shape shifter",
            "archenemy": "Professor X"},

            "Hulk":
            {"real name": "bruce banner",
            "powers": "super strength",
            "archenemy": "adrenaline"}
        }
    
        print(f"{char_name.capitalize()}'s {char_stat} is: {marvelchars[char_name][char_stat].title()}")

        willExit = input("Do you want to try another input? y/n: ").lower()

main()
