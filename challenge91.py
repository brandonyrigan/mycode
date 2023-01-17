#!/usr/bin/env python3

import requests
import wget

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    #print(pokeapi)
    
    img_url = pokeapi["sprites"]["front_default"]
    print(img_url)

    for move in pokeapi["moves"]:
        print(move["move"]["name"])

    game_count = 0
    for game in pokeapi["game_indices"]:
        game_count += 1

    print(len(pokeapi["game_indices"]))
    print(game_count)

    wget.download(img_url, "/home/student/static/")

main()

