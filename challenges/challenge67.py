#!/usr/bin/env python3

def main():
    count = 0
    with open("dracula.txt", "r") as file:
        with open("vampytimes.txt", "w") as vampirefile:
            for line in file:
                if "vampire" in line.lower():
                    print(line)
                    count += 1
                    vampirefile.write(line)
    print(count)

if __name__ == "__main__":
    main()

