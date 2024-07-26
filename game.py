# :)
import os
from getpass import getpass  

# Method to clear the terminal
def clear_terminal():
  os.system('cls' if os.name == 'nt' else 'clear') 

# Player class 
class Player:
  def __init__(self, name, HP, ITL, PWR, database):
    self.name = name
    self.HP = HP
    self.ITL = ITL
    self.PWR = PWR
    self.action = " "
    self.database = database # The database was an initial idea 

# Method to display player stats
  def printStats(self):
    print(f'Name: {self.name}\nHP: {self.HP}\nITL: {self.ITL}')
  
  # Methods for player actions
  def defend(self):
      self.action = "defend"
  
  def attack(self):
      self.action = "attack"
  
  def research(self, database):
      self.action = "research"
      # if database.data >= 5:
      #   database.data -= 5
      self.ITL += 5
      # else:
      #     database.data = 0
      #     self.ITL += database.data


# Database class | not in use right now
class Database:
  def __init__(self, name, data):
    self.name = name
    self.data = data
  def printStats(self):
    print(f'Name: {self.name}\nITL: {self.data}\n')


# Method for player interaction| "1" = attack, "2" = "defend", "3" = research
def resolution(player1, player2):
    clear_terminal()
    if player1.action ==  "1":
        if player2.action == "2":
            
            player1.ITL = max(player1.ITL - 5, 5) # Can change to 'min' to have it reset ITL instead  
        if player2.action == "3":
            player2.HP -= player1.ITL
            player2.ITL += 5
            player1.ITL = 5
        if player2.action == "1":
           damage = player1.ITL - player2.ITL
           if player1.ITL == player2.ITL:
              player1.ITL = 5
              player2.ITL = 5
           elif player1.ITL > player2.ITL:
            player2.HP -= abs(damage)
            player1.ITL = 5
            player2.ITL = 5
           else:
            player1.HP -= abs(damage)
            player1.HP -= player2.ITL
            player2.HP -= player1.ITL
            player1.ITL = 5
            player2.ITL = 5
    if player1.action == "3":
        if player2.action == "1":
          player1.ITL += 5
          player1.HP -= player2.ITL
          player2.ITL = 5
        if player2.action == "3":
            player1.ITL += 5
            player2.ITL += 5
        if player2.action == "2":
            player1.ITL += 5
            # 
    if player1.action == "2":
        if player2.action == "1":
          player2.ITL = max(player2.ITL - 5, 5) # Can change to 'min' to have it reset ITL instead  
         
         
        if player2.action == "3":
            # 
            player2.ITL += 5
        if player2.action == "2":
            print("Both Players defended")
            # 
            # 
    player1.action = None
    player2.action = None    
    
# Main method. Get player input, loops until a player reaches 0 HP
def main(player1, player2):
    while player1.HP > 0 or player2.HP > 0:
      options = ["1","2", "3"]
      while player1.action not in options:
        player1.action = getpass(prompt = ("Player 1 - Select Move: 1) Attack. 2) Defend. 3)Research."))
      while player2.action not in options:
       player2.action = getpass(prompt = ("Player 2 - Select Move: 1) Attack. 2) Defend. 3)Research."))
      resolution(player1, player2)
      player1.printStats()
      player2.printStats()
    
# TODO: Handle the winning scenarios TODO 
      # if player1.HP <= 0:
      #   print("Player 2 wins!")
      # else:
      #   print("Player 1 wins!")
      


# main_db = Database("main", 50)


# Initializing Players and the DB's| anything database related isnt used (anymore)
p1_database = Database("player1", 100)
player1 = Player("Player 1", 30, 5, 5, p1_database)

p2_database = Database("Player 2", 100)
player2 = Player("Player 2", 30, 5, 5, p2_database)

main(player1, player2)

