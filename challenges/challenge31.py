#!/usr/bin/env python3

import random

wordbank= ["indentation", "spaces"] 

tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

wordbank.append(4)

num = int(input(f"Enter a number between 1 and {len(tlgstudents)}: ")) - 1
student_name = tlgstudents[num]


print(student_name + " always uses " + str(wordbank[2]) + " " + wordbank[1] + " to indent.")

name = random.choice(tlgstudents)
print(f"{name}")
