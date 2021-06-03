print("*****************Welcome to Hand Cricket*****************")
import random

toss = int(input("toss to win, 0 for heads & 1 for Tails  :"))
coin_toss = random.randint(0,1)
game = 0
if toss==coin_toss :
  print("you won the Toss! ")
  batorball = int(input("0 for Bating and 1 for Balling  :"))
  if batorball == 0:
    game += 1
else:
  print("You loss the Toss ")
  cpu=random.randint(0,1)
  if cpu == 0 :
    print("They choose to Bating First") 
  else:
    print("They choose to Balling First")
    game += 1
cpu_scores= 0
player_scores= 0
ball1=0
ball2=0
# 1nd Inning starting
if game == 1:
  while True:
    if ball1==60:
      print("1st inning is over now")
      print(f"Your Total runs is {player_scores}")
      print(f"CPU need to make {player_scores+1} runs to win in 60 Balls")
      break
    cpu_ball= random.randint(1,6)
    hit=int(input("Hit the Ball: "))
    if hit == cpu_ball:
      print("OUT! OUT! OUT!,You are Out")
      print(f"Your Total runs is {player_scores}")
      print(f"CPU need to make {player_scores+1} runs to win in 60 Balls")
      break
    else:
      player_scores += hit
      ball1 += 1
      print(f"Total ball: {ball1}")
      print(f"Total Runs: {player_scores}")
      print(f"You:{hit}")
      print(f"CPU:{cpu_ball}")
else:
  while True:
    if ball2==60:
      print("1st inning is over now")
      print(f"CPU Total runs is {cpu_scores}")
      print(f"You need to make {cpu_scores+1} runs to win in 60 Balls")
      break
    cpu_bat= random.randint(1,6)
    ball=int(input("Throw the Ball: "))
    if cpu_bat == ball:
      print("OUT! OUT! OUT!,CPU is Out")
      print(f"CPU Total runs is {cpu_scores}")
      print(f"You need to make {cpu_scores+1} runs to win in 60 Balls")
      break
    else:
      cpu_scores += cpu_bat
      ball2 += 1
      print(f"Total ball: {ball2}")
      print(f"Total Runs: {cpu_scores}")
      print(f"CPU:{cpu_bat}")
      print(f"You:{ball}")
# 2nd Inning starting
if game == 1:
  while True:
    if ball2==60 and cpu_scores<player_scores:
      print("You Won Congratulations!")
      print(f"You beat CPU by {player_scores-cpu_scores}")
      break
    elif cpu_scores>player_scores:
      print("You Loss, Game Over")
      print(f"CPU Won the Game by {60-ball2}")
      print("Better Luck Next Time")
      break
    cpu_bat_2= random.randint(1,6)
    ball_2=int(input("Throw the Ball: "))
    if cpu_bat_2 == ball_2:
      print("OUT! OUT! OUT!,CPU is Out")
      print("You Won Congratulations!")
      print(f"You beat CPU by {player_scores-cpu_scores}")
      break
    if cpu_bat_2==ball_2 and cpu_scores==player_scores:
      print("WOW, It's DRAW")
      print("What a wonderfull Game!")
    else:
      cpu_scores += cpu_bat_2
      ball2 += 1
      print(f"Runs Target: {player_scores+1}")
      print(f"Total ball: {ball2}")
      print(f"Total Runs: {cpu_scores}")
      print(f"CPU:{cpu_bat_2}")
      print(f"You:{ball_2}")
if game == 0:
  while True:
    if ball1==60 and cpu_scores>player_scores:
      print("You Loss, Game Over")
      print(f"CPU beat You by {player_scores-cpu_scores}")
      print("Better Luck Next Time")
      break
    if cpu_scores<player_scores:
      print("You Won Congratulations!")
      print(f"You Won the Game by {60-ball2}")
      break
    cpu_ball_2= random.randint(1,6)
    hit_2=int(input("Hit the Ball: "))
    if cpu_ball_2== hit_2:
      print("OUT! OUT! OUT!,CPU is Out")
      print("You Loss, Game Over")
      print(f"CPU beat You by {cpu_scores-player_scores}")
      print("Better Luck Next Time")
      break
    if cpu_ball_2==hit_2 and cpu_scores==player_scores:
      print("WOW, It's DRAW")
      print("What a wonderfull Game!") 
    else:
      player_scores += hit_2
      ball1 += 1
      print(f"Runs Target: {cpu_scores+1}")
      print(f"Total ball: {ball1}")
      print(f"Total Runs: {player_scores}")
      print(f"You:{hit_2}")
      print(f"CPU:{cpu_ball_2}")
