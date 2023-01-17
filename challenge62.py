#!/usr/bin/env python3

def main():
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    for animal in farms[0]["agriculture"]:
        print(animal)

    farm = int(input("choose a farm: 1) NE Farm, 2) W Farm, 3) SE Farm :")) - 1

    for animal in farms[farm]["agriculture"]:
        print(animal)

if __name__ == "__main__":
    main()
