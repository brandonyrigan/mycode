#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests

URL= "https://opentdb.com/api.php?amount=5&category=27&difficulty=medium&type=multiple"

def main():

    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()
    
    ## loop through results
    for question in data["results"]:
        ## create variable for answers
        count = 1
        ## print the question
        print(question["question"])
        print(count, question["correct_answer"])
        count += 1
        for answer in question["incorrect_answers"]:
            print(count, answer)
            count += 1
        
        ## get user input for answer
        guess = input("what is the correct answer? ")

        if guess == "1":
            print("Correct!")
        else:
            print("Wrong Answer!")

if __name__ == "__main__":
    main()

