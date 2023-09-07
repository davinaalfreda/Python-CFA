#!/usr/bin/env python

from multiprocessing.connection import answer_challenge
from optparse import Option
import random

def main():
   """Start a music guessing game."""
print("Guess the music.")
 
questions =  [
     "Guess the singer name song of Senorita",
     "Where did Troye Sivan born:",
     "Which year Dendelions song released ?: ",
     "Bloody Mary song from which movie ?: ",
     "Which year Heat Waves song released ?: ",
     "Guess the singer name song of Unstoppable:"    
      ]
options = [
      "A.Calvin Harris,Alica Keys","B.Shawn Mendes,Camila Cabello","C.Hank Williams,Katy Perry",
      "A.South Korea","B.South American","C.South African",
      "A.23 September 2017","B.15 July 2017","C.5 April 2017",
      "A.Wednesday","B.Halloween","C.Exorcist",
      "A.18 August 2020","B.29 June 2020","C.21 July 2020 ",
      "A.Sia","B.Tylor Swift","C.Katty Perry"]

answers = ["B", "C", "C", "A", "B", "A"]

guess =[]
score = 0
question_num = 0


for question in questions:
   print("------------------------------")
   print(question) 
   for option in options:[question_num]
   print(option)
    
   guess = input("Enter (A,B,C): ")
   guesses.append(guess)
   if guess == answers[question_num]:
       score += 1
       print(option)


   question_num += 1
guess == answers 
score += 1
  
print("CORRECT!")

print("INCORRECT")
print("{answer_challenge[score]}is the correct answer")
score += 1

print("---------------------------")
print("          RESULTS          ")
print("---------------------------")

print("answer: ",end="")
for answer in "answer":
   print (answer,end=" ")
   print()

   print("guesses:",end="")
for guess in "guesses":
   print(guess,end="")
   print()
main()
