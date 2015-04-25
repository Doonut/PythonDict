import random
import os
my_dict =   {
                "What is the base-2 number system called" : "binary",
                "What is the number system that uses the characters 0-F called" : "hexadecimal",
                "What is the 7-bit text encoding standard called" : "ascii",
                "What is the 16-bit text encoding standard called" : "unicode",
                "What is it called when a number is bigger than the maximum number that can be stored" : "overflow",
                "What are 8 bits refered to" : "byte",
                "What is 1024 bytes refered to" : "kilobyte",
                "A Picture Element. This is the smallest component of a bitmapped image" : "pixel",
                "What is a continuously changing wave, such as natural sound called" : "analog",
                "What is the number of times per second that a wave is measured called" : "sample rate",
                "What is a binary representation of a program called" : "machine code",
                "What does CPU stand for" : "central processing unit",
                "What is the MOST commonly used Object-Oriented programming language in the world" : "C",
                "What computer program is used to convert assembly language into machine language" : "compiler",
                "What is the time required for the fetching and execution of data of a simple machine instruction called" : "CPU cycle",
                "What access method is used for obtaining a record from a cassette tape" : "sequential",
                "The term referring to the evacuation of content or data to some part of the machine is called" : "dump",
                "What is the common boundary between two systems is called" : "interface"
		}

print("=======================")
print("Computer Revision quiz")
print("=======================")

playing = True

while playing == True:
    score = 0
    print("There are " + str(len(my_dict)) + " questions.")
    num = int(input("\nHow many questions would you like? : "))
    print("\n(all answers should be typed in lowercase!)")
    for i in range(num):
        question = (random.choice(list(my_dict.keys())))
        answer = my_dict[question]
        print("\nQuestion " + str(i+1) )
        print(question + "?")
        guess = input("> ") #this is just your attempts at the question
        if guess.lower() == answer.lower():
            print("Correct!")
            score += 1 #adds to your score
        else:
            print("Nope!")

    print("\nYour final score was " + str(score))

    again = input("Enter any key to play again, or 'q' to quit.")
    if again.lower() == 'q':
        playing = False
