import time
import random

hand = input("Choose Rock, Paper, Scissors. ")

a = random.choice(["Rock", "Paper", "Scissors"])

time.sleep(1)
print('Rock')
time.sleep(1)
print('Paper')
time.sleep(1)
print('Scissors')
time.sleep(1)
print('Says SHOOT')
print(hand + ' vs ' + a)





if hand == "Rock" and a == "Rock":
	print('Tie!')
if hand == "Paper" and a == "Paper":
	print('Tie!')
if hand == "Scissors" and a == "Scissors":
	print('Tie!')

if hand == "Rock" and a == "Paper":
	print('You lose!')
if hand == "Rock" and a == "Scissors":
	print('You win!')

if hand == "Paper" and a == "Scissors":
	print('You lose!')
if hand == "Paper" and a == "Rock":
	print('You win!')

if hand == "Scissors" and a == "Rock":
	print('You lose!')
if hand == "Scissors" and a == "Paper":
	print('You win!')