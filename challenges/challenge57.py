#!/usr/bin/env python3

import html

def main():

    trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }
    
    question = trivia["question"]
    correct_answer = html.unescape(trivia["correct_answer"])
    wrong_answer1 = html.unescape(trivia["incorrect_answers"][0])
    wrong_answer2 = html.unescape(trivia["incorrect_answers"][1])
    wrong_answer3 = html.unescape(trivia["incorrect_answers"][2])

    print(question)
    print("A", correct_answer)
    print("B", wrong_answer1)
    print("C", wrong_answer2)
    print("D", wrong_answer3)

    guess = input("Select the correct answer to the trivia question (A, B, C, D): ")
    if guess == "A":
        print("You got it correct!")
    else:
        print("Wrong answer..")

if __name__ == "__main__":
    main()

