#!/usr/bin/env python3

def main():
    stop = True

    while stop:
        try:
            beers = int(input("How many bottles of beer? (1-100) (0 to quit) : "))
            if beers == 0:
                break
            elif beers > 100 or beers < 0:
                print("Must be between 1-100")
                continue
            else:
                for bottle in range(beers):
                    print(f"{beers} of beer on the wall!")
                    print(f"{beers} of beer on the wall! {beers} of bottles of beer! You take one day and pass it around!")
                    beers -= 1
        except Exception as err:
            print("Error:", err)

if __name__ == "__main__":
    main()
